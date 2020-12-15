#!/bin/bash
set -e
set -o pipefail

temp_file=$(mktemp)
function cleanup {
  rm ${temp_file}
  exit $?
}
trap "cleanup" EXIT

./generate_csv.sh > ${temp_file}
./add_to_wikidata.py -f ${temp_file}
