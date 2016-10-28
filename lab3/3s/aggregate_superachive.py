#!/usr/bin/python
from __future__ import print_function
import sys

url_count = 6571038.0  # from reduce_out_sum_rows
url_auto_user_count = 313527.0   # from reduce_out_sum_rows

for line in sys.stdin:
    try:
        url, cnt, is_auto, cnt_auto_users = line.strip().split("\t")
    except ValueError:
        print(sys.exc_info())

    numerator = (int(cnt_auto_users) / url_count)**2
    denominator = (int(cnt)/url_count) * (url_auto_user_count/url_count)
    # try:
    out = round(float(numerator/denominator), 20)
    # except:
    #     print(url, cnt)
    #     print(numerator, denominator_1, denominator_2)
    #     print(int(cnt), url_count, url_auto_user_count, url_count)
    #     print((int(cnt)/int(url_count))*(int(url_auto_user_count)/int(url_count)))
    #     exit()

    print("%s\t%.20f" % (url, out))
