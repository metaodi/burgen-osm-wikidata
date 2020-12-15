#!/bin/bash

set -e
set -o pipefail

cat overpass_castle_query.txt | ./overpass.py | ./parse_osm_data.py | ./generate_wd_query.py | ./parse_wikidata_query.py
