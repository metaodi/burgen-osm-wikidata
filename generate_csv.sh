#!/bin/bash
set -e
set -o pipefail

echo "name,type,id,lat,lon,historic,site_type"
cat overpass_castle_query.txt | ./overpass.py | ./parse_osm_data.py
