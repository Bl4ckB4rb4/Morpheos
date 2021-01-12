#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import browser_cookie3
from collections import Counter

try:
    cjf = browser_cookie3.firefox()
except:
    print("No se puede acceder a las cookies del firefox")
    cjf = []
try:
    cjc = browser_cookie3.chrome()
except:
    print("No se puede acceder a las cookies del Chrome")
    cjc = []

domainsf = []
domainsc = []
for c in cjf:
    domainsf.append(c.domain)
for c in cjc:
    domainsc.append(c.domain)

# Counter sumariza las ocurrencias de la lista generada y en forma de dict
# nos devuelve el dominio como key y las ocurencias como value
print(Counter(domainsf))

print("Cantidad de cookies en firefox : {}".format(len(domainsf)))
print("Cantidad de cookies en chrome : {}".format(len(domainsc)))
