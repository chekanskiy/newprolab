#!/usr/bin/python
from __future__ import print_function
import sys
prev_key = None


def reduce(key, values):  # Key = url

    cnt = values['val']
    auto = values['autodomen']
    cnt_autousers = values['autouser']

    out = [key, cnt, auto, cnt_autousers]
    out = [str(x) for x in out]

    print("\t".join(out))


values = {}
for line in sys.stdin:
    try:
        key, value, autodomen, autouser = line.strip().split("\t")
        if key != prev_key and prev_key is not None:
            reduce(prev_key, values)
            values = {}

        values['val'] = values.get('val', int(0)) + int(value)
        values['autodomen'] = autodomen
        values['autouser'] = values.get('autouser', 0) + int(autouser)

        prev_key = key

    except:
        # pass
        print(line)
        print(sys.exc_info())

if prev_key is not None:
    reduce(prev_key, values)

