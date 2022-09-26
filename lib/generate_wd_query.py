#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import traceback
import os

__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(),
        os.path.dirname(__file__)
    )
)

def remove_clutter(name):
    new_name = name.replace('Burgstelle', '')
    new_name = name.replace('Burg', '')
    new_name = name.replace('Schloss', '')
    new_name = name.replace('Ruine', '')
    new_name = name.replace('Torre', '')
    new_name = name.replace('Chateau', '')
    new_name = name.replace('Château', '')

    return new_name.strip()

try:
    base_query = ''
    wd_query = os.path.join(__location__, '..', 'queries', 'wikidata_castle_query.overpassql')
    with open(wd_query, 'r') as f:
        base_query = f.read()
    for line in sys.stdin:
        name = line.split(',')[0]
        name = remove_clutter(name)
        query = base_query.replace('{osm_name}', name)
        print(query)
        print('-' * 20)

except Exception as e:
    print("Error: %s" % e, file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
    sys.exit(1)
