# Dataset example samples

One real sample from each dataset or benchmark task used in the GeoRDF2Vec analysis is shown below. These examples illustrate the data formats.

KGBench and DBpedia samples come from the local repository data. GEval samples come from the public Evaluation-Framework repository, with original column names and string values preserved. Classification and regression examples are listed separately even when their source tables overlap.

The country-boundary sample comes from the current OpenDataSoft API; it is not a verified copy of the historical snapshot used by the paper authors. Benchmark target meanings and units are not inferred.

## KGBench dmg777k

[Source](https://github.com/pbloem/kgbench-loader)

One labeled training entity with its outgoing triples.

Local source: `ignore/GeoRDF2Vec/data/kgbench_dmg777k/training.int.csv`, `ignore/GeoRDF2Vec/data/kgbench_dmg777k/nodes.int.csv`, `ignore/GeoRDF2Vec/data/kgbench_dmg777k/full_triple_set.csv`.

```json
{
  "index": 278120,
  "class": 4,
  "annotation": "iri",
  "entity": "https://data.labs.pdok.nl/rce/id/monument/24248",
  "outgoing_triples": [
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://dbpedia.org/ontology/city",
      "object": "http://sws.geonames.org/2751792/"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://dbpedia.org/ontology/codeNationalMonument",
      "object": "24248"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://purl.org/dc/terms/description",
      "object": "Pand onder vernieuwde kap. Rechte kroonlijst verkropt boven de vier pilasters der grote orde met composietkapitelen, die de gevel rythmeren."
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "object": "http://bag.basisregistraties.overheid.nl/bag/id/geometry/48351F80CC0B87FE2E4ABF0E7C4847CA"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://www.opengis.net/ont/geosparql#hasGeometry",
      "object": "https://data.labs.pdok.nl/.well-known/genid/75a71f8a-395c-11e8-a9a5-54e1adc08017"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://www.opengis.net/ont/geosparql#sfWithin",
      "object": "https://data.labs.pdok.nl/cbs/id/gemeente/GM0080"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://www.w3.org/2000/01/rdf-schema#seeAlso",
      "object": "https://data.labs.pdok.nl/rce/id/monument/24248"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://www.w3.org/2006/vcard/ns#hasStreetAddress",
      "object": "Korfmakersstraat"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://www.w3.org/2006/vcard/ns#postal-code",
      "object": "8911 LA"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://www.w3.org/2006/vcard/ns#street-address",
      "object": "Korfmakersstraat 15 te Leeuwarden"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "http://xmlns.com/foaf/0.1/depiction",
      "object": "https://data.labs.pdok.nl/rce/id/image/20132586"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "https://data.labs.pdok.nl/rce/def/huisnummer",
      "object": "15"
    },
    {
      "subject": "https://data.labs.pdok.nl/rce/id/monument/24248",
      "predicate": "https://data.labs.pdok.nl/rce/def/huisnummerCompleet",
      "object": "15"
    }
  ]
}
```

## DBpedia 2016-04 English

[Source](https://downloads.dbpedia.org/2016-04/core/geo_coordinates_mappingbased_en.ttl.bz2)

One entity with its geographic RDF statements.

Local source: `ignore/GeoRDF2Vec/data/dbpedia/geo_coordinates_mappingbased_en.ttl`.

```json
{
  "entity": "http://dbpedia.org/resource/Algeria",
  "rdf_statements": [
    "<http://dbpedia.org/resource/Algeria> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing> .",
    "<http://dbpedia.org/resource/Algeria> <http://www.w3.org/2003/01/geo/wgs84_pos#lat> \"36.7\"^^<http://www.w3.org/2001/XMLSchema#float> .",
    "<http://dbpedia.org/resource/Algeria> <http://www.w3.org/2003/01/geo/wgs84_pos#long> \"3.216666666666667\"^^<http://www.w3.org/2001/XMLSchema#float> .",
    "<http://dbpedia.org/resource/Algeria> <http://www.georss.org/georss/point> \"36.7 3.216666666666667\"."
  ]
}
```

## GEval AAUP ? Classification

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Classification/data/AAUP.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q1565621",
  "FICE": "1061",
  "College_name": "Alaska Pacific University",
  "State": "AK",
  "Type": "IIB",
  "Average_salary_full_professors": "454",
  "Average_salary_associate_professors": "382",
  "Average_salary_assistant_professors": "362.0",
  "rating": "382",
  "Average_compensation_full_professor": "567",
  "Average_compensation_associate_professors": "485",
  "Average_compensation_assistant_professors": "471.0",
  "Average_compensation_all_ranks": "487",
  "Number_of_full_professors": "6",
  "Number_of_associate_professors": "11",
  "Number_of_assistant_professors": "9",
  "Number_of_instructors": "4",
  "Number_of_faculty_all_ranks": "32",
  "DBpedia_URI": "http://dbpedia.org/resource/Alaska_Pacific_University",
  "label": "medium",
  "label_comp": "medium",
  "id": "1",
  "DBpedia_URI15": "http://dbpedia.org/resource/Alaska_Pacific_University",
  "YAGO_URI15": "http://yago-knowledge.org/resource/Alaska_Pacific_University",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6QLMMFZWWYK7KBQWG2LGNFRV6VLONF3GK4TTNF2HS==="
}
```

## GEval Cities ? Classification

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Classification/data/Cities.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q24639",
  "id": "1.0",
  "city_name": "Vancouver",
  "DBpedia_URI": "http://dbpedia.org/resource/Vancouver",
  "rating": "106.0",
  "label": "high",
  "DBpedia_URI15": "http://dbpedia.org/resource/Vancouver",
  "YAGO_URI15": "http://yago-knowledge.org/resource/Vancouver",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6VTBNZRW65LWMVZA===="
}
```

## GEval Forbes ? Classification

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Classification/data/Forbes.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q26463",
  "id": "1",
  "Company": "Industrial and Commercial Bank of China",
  "Industry": "Major Banks",
  "Country": "China",
  "rating": "237.3",
  "Sales": "134.8",
  "Profits": "37.8",
  "Assets": "2813.5",
  "Rank": "1",
  "DBpedia_URI": "http://dbpedia.org/resource/Industrial_and_Commercial_Bank_of_China",
  "label": "high",
  "DBpedia_URI15": "http://dbpedia.org/resource/Industrial_and_Commercial_Bank_of_China",
  "YAGO_URI15": "",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6SLOMR2XG5DSNFQWYX3BNZSF6Q3PNVWWK4TDNFQWYX2CMFXGWX3PMZPUG2DJNZQQ===="
}
```

## GEval MetacriticAlbums ? Classification

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Classification/data/MetacriticAlbums.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q7913484",
  "id": "1.0",
  "album": "Van Lear Rose",
  "artist": "Loretta Lynn",
  "date": "27-Apr-04",
  "rating": "97.0",
  "DBpedia_URI": "http://dbpedia.org/resource/Van_Lear_Rose",
  "label": "good",
  "DBpedia_URI15": "http://dbpedia.org/resource/Van_Lear_Rose",
  "YAGO_URI15": "http://yago-knowledge.org/resource/Van_Lear_Rose",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6VTBNZPUYZLBOJPVE33TMU======"
}
```

## GEval MetacriticMovies ? Classification

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Classification/data/MetacriticMovies.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q238245",
  "Movie": "4 Months, 3 Weeks and 2 Days",
  "Release date": "1/23/2008 0:00",
  "DBpedia_URI": "http://dbpedia.org/resource/4_Months,_3_Weeks_and_2_Days",
  "label": "good",
  "id": "1601",
  "rating": "97",
  "DBpedia_URI15": "http://dbpedia.org/resource/4_Months,_3_Weeks_and_2_Days",
  "YAGO_URI15": "",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6NC7JVXW45DIOMWF6M27K5SWK23TL5QW4ZC7GJPUIYLZOM======"
}
```

## GEval cities2000AndCountries_cluster ? Clustering

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Clustering/data/cities2000AndCountries_cluster.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "DBpedia_URI": "http://dbpedia.org/resource/Crespano_del_Grappa",
  "cluster": "1",
  "DBpedia_URI_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6Q3SMVZXAYLON5PWIZLML5DXEYLQOBQQ===="
}
```

## GEval citiesAndCountries_cluster ? Clustering

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Clustering/data/citiesAndCountries_cluster.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "DBpedia_URI": "http://dbpedia.org/resource/Crespano_del_Grappa",
  "cluster": "1",
  "DBpedia_URI_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6Q3SMVZXAYLON5PWIZLML5DXEYLQOBQQ===="
}
```

## GEval citiesMoviesAlbumsCompaniesUni_cluster ? Clustering

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Clustering/data/citiesMoviesAlbumsCompaniesUni_cluster.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "DBpedia_URI": "http://dbpedia.org/resource/Alaska_Pacific_University",
  "cluster": "1",
  "DBpedia_URI_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6QLMMFZWWYK7KBQWG2LGNFRV6VLONF3GK4TTNF2HS==="
}
```

## GEval teams_cluster ? Clustering

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Clustering/data/teams_cluster.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "DBpedia_URI": "http://dbpedia.org/resource/Cuba_national_basketball_team",
  "cluster": "1",
  "DBpedia_URI_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6Q3VMJQV63TBORUW63TBNRPWEYLTNNSXIYTBNRWF65DFMFWQ===="
}
```

## GEval AAUP ? Regression

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Regression/data/AAUP.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q1565621",
  "FICE": "1061",
  "College_name": "Alaska Pacific University",
  "State": "AK",
  "Type": "IIB",
  "Average_salary_full_professors": "454",
  "Average_salary_associate_professors": "382",
  "Average_salary_assistant_professors": "362.0",
  "rating": "382",
  "Average_compensation_full_professor": "567",
  "Average_compensation_associate_professors": "485",
  "Average_compensation_assistant_professors": "471.0",
  "Average_compensation_all_ranks": "487",
  "Number_of_full_professors": "6",
  "Number_of_associate_professors": "11",
  "Number_of_assistant_professors": "9",
  "Number_of_instructors": "4",
  "Number_of_faculty_all_ranks": "32",
  "DBpedia_URI": "http://dbpedia.org/resource/Alaska_Pacific_University",
  "label": "medium",
  "label_comp": "medium",
  "id": "1",
  "DBpedia_URI15": "http://dbpedia.org/resource/Alaska_Pacific_University",
  "YAGO_URI15": "http://yago-knowledge.org/resource/Alaska_Pacific_University",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6QLMMFZWWYK7KBQWG2LGNFRV6VLONF3GK4TTNF2HS==="
}
```

## GEval Cities ? Regression

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Regression/data/Cities.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q24639",
  "id": "1.0",
  "city_name": "Vancouver",
  "DBpedia_URI": "http://dbpedia.org/resource/Vancouver",
  "rating": "106.0",
  "label": "high",
  "DBpedia_URI15": "http://dbpedia.org/resource/Vancouver",
  "YAGO_URI15": "http://yago-knowledge.org/resource/Vancouver",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6VTBNZRW65LWMVZA===="
}
```

## GEval Forbes ? Regression

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Regression/data/Forbes.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q26463",
  "id": "1",
  "Company": "Industrial and Commercial Bank of China",
  "Industry": "Major Banks",
  "Country": "China",
  "rating": "237.3",
  "Sales": "134.8",
  "Profits": "37.8",
  "Assets": "2813.5",
  "Rank": "1",
  "DBpedia_URI": "http://dbpedia.org/resource/Industrial_and_Commercial_Bank_of_China",
  "label": "high",
  "DBpedia_URI15": "http://dbpedia.org/resource/Industrial_and_Commercial_Bank_of_China",
  "YAGO_URI15": "",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6SLOMR2XG5DSNFQWYX3BNZSF6Q3PNVWWK4TDNFQWYX2CMFXGWX3PMZPUG2DJNZQQ===="
}
```

## GEval MetacriticAlbums ? Regression

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Regression/data/MetacriticAlbums.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q7913484",
  "id": "1.0",
  "album": "Van Lear Rose",
  "artist": "Loretta Lynn",
  "date": "27-Apr-04",
  "rating": "97.0",
  "DBpedia_URI": "http://dbpedia.org/resource/Van_Lear_Rose",
  "label": "good",
  "DBpedia_URI15": "http://dbpedia.org/resource/Van_Lear_Rose",
  "YAGO_URI15": "http://yago-knowledge.org/resource/Van_Lear_Rose",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6VTBNZPUYZLBOJPVE33TMU======"
}
```

## GEval MetacriticMovies ? Regression

[Source](https://raw.githubusercontent.com/mariaangelapellegrino/Evaluation-Framework/master/evaluation_framework/Regression/data/MetacriticMovies.tsv)

One entity with the original benchmark columns.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Original field names and string values are preserved; no target meanings or units are inferred.

```json
{
  "Wikidata_URI15": "http://www.wikidata.org/entity/Q238245",
  "Movie": "4 Months, 3 Weeks and 2 Days",
  "Release date": "1/23/2008 0:00",
  "DBpedia_URI": "http://dbpedia.org/resource/4_Months,_3_Weeks_and_2_Days",
  "label": "good",
  "id": "1601",
  "rating": "97",
  "DBpedia_URI15": "http://dbpedia.org/resource/4_Months,_3_Weeks_and_2_Days",
  "YAGO_URI15": "",
  "DBpedia_URI15_Base32": "NB2HI4B2F4XWIYTQMVSGSYJON5ZGOL3SMVZW65LSMNSS6NC7JVXW45DIOMWF6M27K5SWK23TL5QW4ZC7GJPUIYLZOM======"
}
```

## OpenDataSoft World Administrative Boundaries

[Source](https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/world-administrative-boundaries/records?limit=1)

One country or territory, including its complete boundary geometry.

Retrieved: 2026-11-13T13:21:55.707970+00:00

Current public-source record; not a verified copy of the snapshot accessed by the paper authors on 2024-12-20.

```json
{
  "geo_point_2d": {
    "lon": -171.85265966247346,
    "lat": -9.195175351076909
  },
  "geo_shape": {
    "type": "Feature",
    "geometry": {
      "coordinates": [
        [
          [
            -171.84375999999992,
            -9.21082999999993
          ],
          [
            -171.84805999999992,
            -9.21888999999993
          ],
          [
            -171.8588599999999,
            -9.209649999999954
          ],
          [
            -171.8627199999999,
            -9.180899999999951
          ],
          [
            -171.8524299999999,
            -9.17062999999996
          ],
          [
            -171.8441899999999,
            -9.191109999999924
          ],
          [
            -171.84375999999992,
            -9.21082999999993
          ]
        ]
      ],
      "type": "Polygon"
    },
    "properties": {}
  },
  "iso3": "TKL",
  "status": "NZ Non-Self-Governing Territory",
  "color_code": "TKL",
  "name": "Tokelau",
  "continent": "Oceania",
  "region": "Polynesia",
  "iso_3166_1_alpha_2_codes": "TK",
  "french_short": "Tokelau"
}
```
