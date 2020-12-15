#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import traceback
import os
import requests
from SPARQLWrapper import SPARQLWrapper, JSON
from dotenv import load_dotenv, find_dotenv
from pprint import pprint
load_dotenv(find_dotenv())


class Wikidata(object):
    def __init__(self, username, password, endpoint='https://www.wikidata.org/w/api.php'):
        self.endpoint = endpoint
        self.session = requests.Session()
        self.login(username, password)

    def login(self, username, password):
        res = self.session.get(self.endpoint, params={
            'action': 'query',
            'meta': 'tokens',
            'type': 'login',
            'format': 'json',
        })
        tokens = res.json()['query']['tokens']

        res = self.session.post(self.endpoint, data={
            'action': 'login',
            'lgname': username,
            'lgpassword': password,
            'lgtoken': tokens['logintoken'],
            'format': 'json'
        })
        res.raise_for_status()
        login = res.json()
        return login

    def get_item(self, item):
        res = self.session.get(self.endpoint, params={
            'action': 'wbgetentities',
            'ids': item,
            'format': 'json',
        })
        res.raise_for_status()
        result = res.json()
        return result['entities'][item]

    def _csrf(self):
        res = self.session.get(self.endpoint, params={
            'action': 'query',
            'meta': 'tokens',
            'type': 'csrf',
            'format': 'json',
        })
        pprint(res)
        csrf = res.json()['query']['tokens']['csrftoken']
        return csrf

    def create_item(self, label):
        csrf = self._csrf()
        item = {
            'labels': {
                'de': {'language': 'de', 'value': label}
            }
        }
        data = {
            'action': 'wbeditentity', 
            'new': 'item', 
            'token': csrf, 
            'format': 'json', 
            'data': json.dumps(item)
        }
        pprint(data)
        res = self.session.post(self.endpoint, data=data)
        res.raise_for_status()
        result = res.json()
        return result

    def create_claim(self, item, claim, snaktype='value'):
        csrf = self._csrf()
        data = {
            'action': 'wbcreateclaim', 
            'entity': item, 
            'token': csrf, 
            'format': 'json', 
            'snaktype': snaktype
        }

        data.update(claim)
        if isinstance(data['value'], dict):
            data['value'] = json.dumps(data['value'])

        res = self.session.post(self.endpoint, data=data)
        res.raise_for_status()
        result = res.json()
        if result.get('error'):
            raise WikidataError(result.get('error'))
        return result

    def create_item_claim(self, item, prop, target):
        target_id = int(target.replace('Q', ''))
        claim = {
            'property':prop, 
            'value': {
                'entity-type':'item', 
                'numeric-id': target_id
            }
        }
        return self.create_claim(item, claim)

    def create_coord_claim(self, item, prop, lat, lon):
        claim = {
            'property':prop, 
            'value': {
                'latitude': lat, 
                'longitude': lon,
                'precision': 0.000001,
            }
        }
        return self.create_claim(item, claim)


class WikidataError(Exception):
    pass


def query(q, endpoint='https://query.wikidata.org/sparql'):
    agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    sparql = SPARQLWrapper(endpoint, agent=agent)
    sparql.setQuery(q)
    sparql.setReturnFormat(JSON)
    results = sparql.queryAndConvert()
    return results['results']['bindings']


if __name__ == "__main__":
    try:
        API_ENDPOINT = os.getenv('WIKIDATA_SPARQL_ENDPOINT', 'https://query.wikidata.org/sparql')
        query_str = "".join(sys.stdin.readlines())

        r = query(query_str, API_ENDPOINT)
        print(json.dumps(r, sort_keys=True, indent=2))
    except Exception as e:
        print("Error: %s" % e, file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        sys.exit(1)
