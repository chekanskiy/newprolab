#!/usr/bin/python
from __future__ import print_function
import sys
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
