"""Count local DBpedia resources and predicates with bounded memory."""
from collections import Counter
import csv
import json
from pathlib import Path
import tempfile
import time
import zlib


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'data' / 'dbpedia'
OUTPUT = ROOT / 'EDA' / 'data'


def main():
    started = time.monotonic()
    predicates = Counter()
    literal_counts = Counter()
    examples = {}
    files = []
    pending = {}
    with tempfile.TemporaryDirectory(prefix='dbpedia_stats_') as temporary:
        partitions = [Path(temporary) / f'{i}.txt' for i in range(128)]
        streams = [path.open('wb') for path in partitions]

        def flush():
            buffers = [bytearray() for _ in streams]
            for uri, flags in pending.items():
                buffers[zlib.crc32(uri) % len(streams)].extend(
                    str(flags).encode() + b'\t' + uri + b'\n'
                )
            for stream, buffer in zip(streams, buffers):
                stream.write(buffer)
            pending.clear()

        try:
            for path in sorted(DATA.glob('*.ttl')):
                count = 0
                with path.open('rb') as source:
                    for line_number, line in enumerate(source, 1):
                        line = line.strip()
                        if not line or line.startswith(b'#'):
                            continue
                        # These specific DBpedia dumps use one full-IRI triple per line.
                        parts = line.split(None, 2)
                        if (len(parts) != 3 or not parts[0].startswith(b'<')
                                or not parts[0].endswith(b'>')
                                or not parts[1].startswith(b'<')
                                or not parts[1].endswith(b'>')
                                or not parts[2].endswith(b'.')):
                            raise ValueError(f'Unexpected dump syntax: {path}:{line_number}')
                        subject, predicate, obj = parts
                        subject = subject[1:-1]
                        predicate = predicate[1:-1]
                        pending[subject] = pending.get(subject, 0) | 1
                        predicates[predicate] += 1
                        examples.setdefault(predicate, obj[:-1].strip().decode('utf-8'))
                        if obj.startswith(b'<'):
                            end = obj.index(b'>')
                            resource = obj[1:end]
                            pending[resource] = pending.get(resource, 0) | 2
                        elif obj.startswith(b'"'):
                            literal_counts[predicate] += 1
                        else:
                            raise ValueError(f'Unexpected object: {path}:{line_number}')
                        count += 1
                        if len(pending) >= 100_000:
                            flush()
                files.append({'file': path.name, 'statements': count, 'bytes': path.stat().st_size})
                print(f'{path.name}: {count:,} statements ({time.monotonic() - started:.0f}s)', flush=True)
            flush()
        finally:
            for stream in streams:
                stream.close()

        totals = Counter()
        for partition in partitions:
            resources = {}
            with partition.open('rb') as stream:
                for line in stream:
                    flag, uri = line.rstrip(b'\n').split(b'\t', 1)
                    resources[uri] = resources.get(uri, 0) | int(flag)
            totals['distinct_resource_nodes'] += len(resources)
            for uri, flags in resources.items():
                totals['distinct_subjects'] += bool(flags & 1)
                totals['distinct_resource_objects'] += bool(flags & 2)
                if uri.startswith(b'http://dbpedia.org/resource/'):
                    totals['dbpedia_resources'] += 1
                    totals['dbpedia_subjects'] += bool(flags & 1)
                    if uri.startswith(b'http://dbpedia.org/resource/Category:'):
                        totals['category_resources'] += 1
            partition.unlink()

    with (OUTPUT / 'dbpedia_predicates.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=[
            'predicate', 'statements', 'resource_statements', 'literal_statements', 'example_object'
        ])
        writer.writeheader()
        for predicate, count in sorted(predicates.items()):
            literals = literal_counts[predicate]
            writer.writerow({
                'predicate': predicate.decode('utf-8'), 'statements': count,
                'resource_statements': count - literals, 'literal_statements': literals,
                'example_object': examples[predicate],
            })
    summary = {
        **totals, 'distinct_predicates': len(predicates),
        'statements': sum(predicates.values()),
        'literal_statements': sum(literal_counts.values()),
        'files': files,
        'count_definition': 'Resources are distinct full IRIs occurring as subjects or resource objects; predicate-only IRIs and literal values are excluded. Statement counts include repeated triples across files.',
    }
    (OUTPUT / 'dbpedia_statistics.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
