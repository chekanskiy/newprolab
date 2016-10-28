#!/usr/bin/python
from __future__ import print_function
import sys

for line in sys.stdin:
    try:
        uid, ts, link = line.strip().split()
        if uid == "-":
            continue

    except ValueError:
        try:
            uid, link = line.strip().split()
            if uid == "-" or "http" not in link:
                continue
        except ValueError:
            continue
            # print(line)
            # print(sys.exc_info())

    print("\t".join([str(link), str(int(1))]))
