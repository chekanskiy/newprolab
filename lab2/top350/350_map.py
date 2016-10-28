#!/usr/bin/python
from __future__ import print_function
import sys

top_350_dict = {}
for line in sys.stdin:
    link, cnt = line.strip().split("\t")
    if len(top_350_dict) >= 4000:
        min_cnt = min(top_350_dict.keys())
        if cnt > min_cnt:
            del top_350_dict[min_cnt]
            top_350_dict[cnt] = link
    else:
        top_350_dict[cnt] = link

for key in top_350_dict.keys():
    print("\t".join([top_350_dict[key], key]))
