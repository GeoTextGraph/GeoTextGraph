"""Run from the repository root: python EDA/scripts/dbpedia_country_counts.py."""
from collections import defaultdict
import csv
from glob import glob
import json
import re
import unicodedata
from urllib.parse import unquote


def normalize(name):
    name = unicodedata.normalize('NFKD', unquote(name).replace('_', ' '))
    return re.sub(r'[^a-z0-9]', '', name.encode('ascii', 'ignore').decode().lower())


def main():
    with open('EDA/data/world_countries.geojson', encoding='utf-8') as stream:
        world = json.load(stream)
    names = {}
    map_names = {}
    for feature in world['features']:
        properties = feature['properties']
        code = properties['ADM0_A3']
        map_names[code] = properties['ADMIN']
        for field in ('ADMIN', 'NAME', 'NAME_LONG', 'NAME_EN', 'FORMAL_EN'):
            if properties.get(field):
                names[normalize(properties[field])] = code
    aliases = {
        'United_States': 'USA', 'United_Kingdom': 'GBR',
        'Republic_of_Ireland': 'IRL', 'Republic_of_the_Congo': 'COG',
        'Democratic_Republic_of_the_Congo': 'COD', 'Ivory_Coast': 'CIV',
        'East_Timor': 'TLS', 'Czech_Republic': 'CZE',
        'Republic_of_Macedonia': 'MKD', 'The_Bahamas': 'BHS',
        'The_Gambia': 'GMB', 'Vatican_City': 'VAT',
    }
    names.update({normalize(name): code for name, code in aliases.items() if code in map_names})
    subjects = defaultdict(set)
    predicate = b'<http://dbpedia.org/ontology/country>'
    for path in sorted(glob('data/dbpedia/*.ttl')):
        with open(path, 'rb') as stream:
            for line in stream:
                if predicate not in line:
                    continue
                subject, relation, obj = line.split(None, 2)
                if relation == predicate and obj.startswith(b'<'):
                    country = obj[1:obj.index(b'>')].decode('utf-8')
                    subjects[country].add(subject[1:-1])
        print(f'Scanned {path}', flush=True)

    mapped = defaultdict(set)
    records = []
    for uri, nodes in subjects.items():
        label = unquote(uri.rsplit('/', 1)[-1]).replace('_', ' ')
        code = names.get(normalize(label), '')
        records.append({'country_uri': uri, 'country': label, 'node_count': len(nodes), 'map_code': code})
        if code:
            mapped[code].update(nodes)
    records.sort(key=lambda row: (-row['node_count'], row['country']))
    with open('EDA/data/dbpedia_country_counts.csv', 'w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['country_uri', 'country', 'node_count', 'map_code'])
        writer.writeheader()
        writer.writerows(records)
    with open('EDA/data/dbpedia_country_map_counts.csv', 'w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['map_code', 'country', 'node_count'])
        writer.writeheader()
        writer.writerows(sorted([
            {'map_code': code, 'country': map_names[code], 'node_count': len(nodes)}
            for code, nodes in mapped.items()
        ], key=lambda row: -row['node_count']))
    print(f'{len(records)} country references; {len(mapped)} map regions; {sum(not row["map_code"] for row in records)} unmatched references.', flush=True)


if __name__ == '__main__':
    main()
