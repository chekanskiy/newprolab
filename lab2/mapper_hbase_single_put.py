#!/usr/bin/python
from __future__ import print_function
import sys
import happybase

# connection = happybase.Connection('cluster2.newprolab.com')
connection = happybase.Connection('10.63.0.70')
table = connection.table('sergey.chekanskiy')
col_name = 'data:url'

for line in sys.stdin:
    try:
        uid, ts, link = line.strip().split()
        uid = int(uid)
        ts = int(float(ts) * 1000)
    except ValueError:
        # raise
        continue
    if uid % 256 == 205:
        table.put(str(uid), {col_name: str(link)}, ts)  # TS MUST BE INT
        print(str(uid) + " " + str(link) + " " + str(ts))
