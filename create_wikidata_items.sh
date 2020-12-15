#!/bin/bash
set -e
set -o pipefail

./generate_csv.sh > missing_wikidata.csv
./add_to_wikidata.py -f missing_wikidata.csv
