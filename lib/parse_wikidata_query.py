#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import traceback
import os
import time
from wikidata import query

current_query = ''
try:
    for line in sys.stdin:
        line = line.strip()
        if line == '-' * 20:
            result = query(current_query)
            print(current_query)
            print('')
            print("Result:")
            print(result)
            print('-' * 20)
            time.sleep(20) # avoid rate-limit of API
            current_query = ''
            continue
        current_query += f"{line}\n"
except Exception as e:
    print("Error: %s" % e, file=sys.stderr)
    print(traceback.format_exc(), file=sys.stderr)
    sys.exit(1)
