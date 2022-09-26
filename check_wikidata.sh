#!/bin/bash

set -e
set -o pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

cat $DIR/queries/overpass_castle_query.overpassql | $DIR/lib/overpass.py | $DIR/lib/parse_osm_data.py | $DIR/lib/generate_wd_query.py | $DIR/lib/parse_wikidata_query.py
