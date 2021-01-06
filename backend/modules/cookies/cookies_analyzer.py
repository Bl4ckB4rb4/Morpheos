#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import browser_cookie3
import requests
import re

cj = browser_cookie3.firefox()
print(cj)

for c in cj:
    print("Cookie : {}".format(c))
    print()

# url = 'https://github.com/'
#
# r = requests.get(url, cookies=cj)
# print(r.text)
