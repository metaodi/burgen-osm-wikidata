import json
import sys
import traceback
import os
from SPARQLWrapper import SPARQLWrapper, JSON

def query(q, endpoint='https://query.wikidata.org/sparql'):
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(q)
    sparql.setReturnFormat(JSON)
    results = sparql.queryAndConvert()
    return results['results']['bindings']

if __name__ == "__main__":
    try:
        API_ENDPOINT = os.getenv('WIKIDATA_API_ENDPOINT', 'https://query.wikidata.org/sparql')
        query_str = "".join(sys.stdin.readlines())

        r = query(query_str, API_ENDPOINT)
        print(json.dumps(r, sort_keys=True, indent=2))
    except Exception as e:
        print("Error: %s" % e, file=sys.stderr)
        print(traceback.format_exc(), file=sys.stderr)
        sys.exit(1)
