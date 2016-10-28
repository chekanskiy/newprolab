#!/usr/bin/python
from __future__ import print_function
import sys
import re
import urlparse
# urllib.parse
import urllib


def url2domain(url):
    try:
        a = urlparse.urlparse(urllib.unquote(url.strip()))
        if (a.scheme in ['http','https']):
            b = re.search("(?:www\.)?(.*)",a.netloc).group(1)
            if b is not None:
                return str(b).strip()
            else:
                return ''
        else:
            return ''
    except:
        return


def filter_category(domain):
    cat_1_Autouser = [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru']
    cat_2_Cultureuser = [u'postnauka.ru', u'plantarium.ru', u'lensart.ru']
    cat_3_Traveluser = [u'pass.rzd.ru', u'rzd.ru', u'vokrug.tv']
    cat_4_Sickuser = [u'apteka.ru', u'doctor.ufacity.info', u'womanhit.ru']
    categories = cat_1_Autouser + cat_2_Cultureuser + cat_3_Traveluser + cat_4_Sickuser
    if domain in categories:
        return 1
    else:
        return 0


for line in sys.stdin:
    try:
        uid, ts, link = line.strip().split()
        if uid == "-" or "http" not in link:  # skip links without http and no user_id
            continue
        else:
            domain = url2domain(link)
            if not filter_category(domain):
                continue

    except ValueError:
        try:
            uid, link = line.strip().split()
            if uid == "-" or "http" not in link:  # skip links without http and no user_id
                continue
            else:
                domain = url2domain(link)
                if not filter_category(domain):
                    continue
        except ValueError:
            continue
            # print(line)
            # print(sys.exc_info())

    print("\t".join([str(uid), str(domain), str(int(1))]))
