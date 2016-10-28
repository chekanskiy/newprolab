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
                return 'N/A'
        else:
            return 'N/A'
    except:
        return 'N/A'


def filter_category(domain, uid):
    cat_1_Autouser = [u'cars.ru', u'avto-russia.ru', u'bmwclub.ru']
    auto_domain = 0
    auto_user = 0
    if domain in cat_1_Autouser:
        auto_domain = 1
    if int(uid) in list(auto_users):
        auto_user = 1
    return [auto_domain, auto_user]

auto_users = []
with open('lab03_users.txt', 'r') as f:
    for line in f.readlines():
        # try:
        uid, auto, _, _, _ = line.split("\t")
        if int(auto) == 1:
            auto_users.append(int(uid))
        # except:
        #     continue


# auto_users = pd.read_csv('lab03_users.txt', delimiter='\t', header=None, names=['uid','auto', 1,2,3,4])
# auto_users = auto_users[auto_users.auto == 1]

for line in sys.stdin:
    try:
        uid, ts, link = line.strip().split()
        if uid == "-" or "http" not in link:  # skip links without http and no user_id
            continue
    except ValueError:
        try:
            uid, link = line.strip().split()
            if uid == "-" or "http" not in link:  # skip links without http and no user_id
                continue
        except ValueError:
            continue

    domain = url2domain(link)
    if domain == 'N/A':
        continue
    out_list = filter_category(domain, uid)
    print("\t".join([str(domain), str(int(1)), str(out_list[0]), str(out_list[1])]))
