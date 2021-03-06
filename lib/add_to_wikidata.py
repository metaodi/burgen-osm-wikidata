#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create new wikidata items based on given CSV file

Usage:
  update_wikidata.py --file <path-to-file> 
  update_wikidata.py (-h | --help)
  update_wikidata.py --version

Options:
  -h, --help                  Show this screen.
  --version                   Show version.
  -f, --file <path-to-file>   Path to the CSV file.

"""
import wikidata as wd
import os
import sys
import csv
import re
from pprint import pprint
from docopt import docopt
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

arguments = docopt(__doc__, version='Create new wikidata items 1.0')


def skip_item():
    reply = str(input('Create wikidata item [Y/n]: ')).lower().strip()
    return False if reply[:1] == 'n' else True

def map_wd_types(row):
    types = []
    if row['site_type'] == 'fortification':
        types.append({'id': 'Q57821', 'desc': 'fortification'})
    if row['historic'] == 'archaeological_site':
        types.append({'id': 'Q839954', 'desc': 'archaeological site'})
    if row['historic'] == 'castle':
        types.append({'id': 'Q23413', 'desc': 'castle'})
    if row['historic'] == 'tower':
        types.append({'id': 'Q12518', 'desc': 'tower'})

    if re.search(r'ruine', row['name'], flags=re.I):
        types.append({'id': 'Q17715832', 'desc': 'castle ruin'})

    if re.search(r'(Burgstall|Burgstelle)', row['name'], flags=re.I):
        types.append({'id': 'Q1015644', 'desc': 'Burgstall'})

    if re.search(r'(Warte)', row['name'], flags=re.I):
        types.append({'id': 'Q2549943', 'desc': 'Warte'})

    return types


api_url = os.getenv('WIKIDATA_API_URL')
username = os.getenv('BOT_NAME'),
password = os.getenv('BOT_PASSWORD'),
wd = wd.Wikidata(username, password, api_url)

osm_csv = arguments['--file']
with open(osm_csv, 'r') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(f"OSM: https://openstreetmap.org/{row['type']}/{row['id']}") 
        print(f"Name: {row['name']}") 
        print(f"Lat/Lon: {row['lat']} {row['lon']}") 
        print(f"Historic: {row['historic']}") 
        print(f"Site type: {row['site_type']}") 
        print('-' * 10)
        types = map_wd_types(row)
        print(f"Wikidata instance of: {[i['desc'] for i in types]}")

        if not skip_item():
            continue
        # TODO
        print("Creating a new wikidata item")
        print("") 

        # create a new item
        result = wd.create_item(row['name'])
        item = result['entity']['id']
        print(f"New page created: https://wikidata.org/wiki/{item}")

        # instance of
        for t in types:
            wd.create_item_claim(item, 'P31', t['id']) # instance of

        # country
        switzerland = 'Q39'
        wd.create_item_claim(item, 'P17', switzerland)

        # coordinate location
        wd.create_coord_claim(item, 'P625', row['lat'], row['lon'])

        pprint(wd.get_item(item))
        print("") 
        print("") 

# sandbox item
#item = 'Q15397819'
