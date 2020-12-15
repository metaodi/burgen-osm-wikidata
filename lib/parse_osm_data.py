#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import traceback
import os
import json

try:
    json_str = "".join(sys.stdin.readlines())
    osm_data = json.loads(json_str)
    for elem in osm_data['elements']:
        data = [
            elem.get('tags', {}).get('name', ''),
            elem.get('type', ''),
            str(elem.get('id','')),
            str(elem.get('lat', elem.get('center', {}).get('lat', ''))),
            str(elem.get('lon', elem.get('center', {}).get('lon', ''))),
            elem.get('tags', {}).get('historic', ''),
            elem.get('tags', {}).get('site_type', ''),
        ]
        print(",".join(data))

except Exception as e:
    print("Error: %s" % e, file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
    sys.exit(1)
