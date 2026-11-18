"""Run from the repository root to count distinct subjects per RDF type."""
from collections import Counter
import csv
from glob import glob
import os
import tempfile
import zlib


def main():
    type_ids = {}
    counts = Counter()
    predicate = b'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>'
    with tempfile.TemporaryDirectory(prefix='dbpedia_types_') as temporary:
        paths = [os.path.join(temporary, f'{i}.tsv') for i in range(128)]
        streams = [open(path, 'wb') for path in paths]
        buffers = [bytearray() for _ in paths]
        buffered = 0

        def flush():
            for stream, buffer in zip(streams, buffers):
                stream.write(buffer)
                buffer.clear()

        def write_subject(subject, types):
            nonlocal buffered
            buffer = buffers[zlib.crc32(subject) % len(buffers)]
            buffer.extend(subject + b'\t' + b','.join(str(value).encode() for value in sorted(types)) + b'\n')
            buffered += 1
            if buffered == 100_000:
                flush()
                buffered = 0

        try:
            for path in sorted(glob('data/dbpedia/*.ttl')):
                last_subject = None
                last_types = set()
                with open(path, 'rb') as stream:
                    for line in stream:
                        if predicate not in line:
                            continue
                        subject, relation, obj = line.split(None, 2)
                        if relation != predicate:
                            continue
                        type_uri = obj[1:obj.index(b'>')]
                        if type_uri not in type_ids:
                            type_ids[type_uri] = len(type_ids)
                        subject = subject[1:-1]
                        if last_subject is not None and subject != last_subject:
                            write_subject(last_subject, last_types)
                            last_types = set()
                        last_subject = subject
                        last_types.add(type_ids[type_uri])
                if last_subject is not None:
                    write_subject(last_subject, last_types)
                print(f'Scanned {path}', flush=True)
            flush()
        finally:
            for stream in streams:
                stream.close()

        for path in paths:
            subjects = {}
            with open(path, 'rb') as stream:
                for line in stream:
                    subject, types = line.rstrip(b'\n').split(b'\t', 1)
                    subjects.setdefault(subject, set()).update(map(int, types.split(b',')))
            for types in subjects.values():
                counts.update(types)
            os.remove(path)

    with open('EDA/data/dbpedia_type_counts.csv', 'w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['type', 'node_count'])
        writer.writeheader()
        writer.writerows(sorted([
            {'type': uri.decode('utf-8'), 'node_count': counts[type_id]}
            for uri, type_id in type_ids.items()
        ], key=lambda row: (-row['node_count'], row['type'])))
    print(f'Saved distinct entity counts for {len(type_ids)} types.', flush=True)


if __name__ == '__main__':
    main()
