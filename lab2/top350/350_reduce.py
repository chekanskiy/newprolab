#!/usr/bin/python
from __future__ import print_function
import sys

# top_350_dict = {}
# for line in sys.stdin:
#     key, link, value = line.strip().split("\t")
#     top_350_dict[value] = link
# bottom = sorted(top_350_dict.keys(), reverse=1)[350:]
# for item in bottom:
#     top_350_dict.pop(item, None)
#
# for key in top_350_dict.keys():
#     print("\t".join([key, top_350_dict[key]]))
#     print("\t".join([link, str(int(float(value)))]))

prev_key = None


def print_res(key, values):
    sum_ = sum(values)
    print("{0}\t{1}".format(key, round(sum_, 0)))

values = []
for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key != prev_key and prev_key is not None:
        print_res(prev_key, values)
        values = []
    values.append(float(value))
    prev_key = key

if prev_key is not None:
    print_res(prev_key, values)
