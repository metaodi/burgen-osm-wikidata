#!/bin/bash
set -e
set -o pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

temp_file=$(mktemp)
function cleanup {
  rm ${temp_file}
  exit $?
}
trap "cleanup" EXIT

$DIR/lib/generate_csv.sh > ${temp_file}
$DIR/lib/add_to_wikidata.py -f ${temp_file}
