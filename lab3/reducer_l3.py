#!/usr/bin/python
from __future__ import print_function
import sys
prev_key = None


def reduce(key, values):  # Key = uid
    # try:
    categories = [0, 0, 0, 0]
    cat_1_Autouser = [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru']
    cat_2_Cultureuser = [u'postnauka.ru', u'plantarium.ru', u'lensart.ru']
    cat_3_Traveluser = [u'pass.rzd.ru', u'rzd.ru', u'vokrug.tv']
    cat_4_Sickuser = [u'apteka.ru', u'doctor.ufacity.info', u'womanhit.ru']

    for cat in cat_1_Autouser:
        if len(str(values.pop(cat, 0))) >= 10:
            categories[0] = 1
    for cat in cat_2_Cultureuser:
        if len(str(values.pop(cat, 0))) >= 10:
            categories[1] = 1
    for cat in cat_3_Traveluser:
        if len(str(values.pop(cat, 0))) >= 10:
            categories[2] = 1
    for cat in cat_4_Sickuser:
        if len(str(values.pop(cat, 0))) >= 10:
            categories[3] = 1

    out = [int(key)] + categories
    out = [str(x) for x in out]
    print("\t".join(out))
    # except:
    #     print(values)

values = {}
for line in sys.stdin:
    key, domain, value = line.strip().split("\t")
    if key != prev_key and prev_key is not None:
        reduce(prev_key, values)
        values = {}
    try:
        values[domain] += value
    except:
        values[domain] = value
    prev_key = key

if prev_key is not None:
    reduce(prev_key, values)

