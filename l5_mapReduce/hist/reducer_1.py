#!/usr/bin/python
from __future__ import print_function
import sys
prev_key = None
marks = []


def print_res(key, values):
    avg = sum(values)/len(values)
    print("{0}\t{1}".format(round(avg, 1), 1))  # просто выдаем, что с таким средним нашелся 1 чел

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
