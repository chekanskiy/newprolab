#!/usr/bin/python
from __future__ import print_function
import sys
import happybase

# connection = happybase.Connection('cluster2.newprolab.com')
connection = happybase.Connection('10.63.0.70')
table = connection.table('sergey.chekanskiy')
col_name = 'data:url'
BATCH_CNT = 1000

cnt = 0
batch = table.batch()
for line in sys.stdin:
    try:
        uid, ts, link = line.strip().split()
        uid = int(uid)
        ts = int(float(ts) * 1000)
    except ValueError:
        # raise
        continue
    if uid % 256 == 205:
        print(str(cnt) + str(uid) + " " + str(link) + "_" + str(ts))
        batch.put(str(uid), {col_name: str(link)}, ts)
        cnt+=1
        if cnt % BATCH_CNT == 0:
            batch.send()
            batch = table.batch()
            print(str(cnt) + " batch sent")
        # print("\t".join([uid, ts, link]))
batch.send()
