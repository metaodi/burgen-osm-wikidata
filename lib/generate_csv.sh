#!/bin/bash
set -e
set -o pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "name,type,id,lat,lon,historic,site_type"
cat $DIR/../queries/overpass_castle_query.txt | $DIR/overpass.py | $DIR/parse_osm_data.py
