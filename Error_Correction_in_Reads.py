#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:00:30 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines() [1::2]
    CONTENU = [ elt.strip("\n\r\t ") for elt in CONTENU ]

for elta in CONTENU:
    REVERSE = [ elta.replace("A","t").replace("C","g").replace("G","c") \
               .replace("T","a").upper() [::-1] for elta in CONTENU ]

RECONNUS = set()
ALONE = []

for eltb in CONTENU:
    if CONTENU.count(eltb) >= 2 or eltb in REVERSE:
        RECONNUS.add(eltb)
    else:
        ALONE.append(eltb)

for eltc in ALONE:
    pas = 0
    for eltd in list(RECONNUS) + REVERSE:
        tmp = [ c==v for c, v in zip(eltc, eltd) ]
        if tmp.count(0) == 1 :
            PROCHE = eltd
            print eltc + "->" + PROCHE
            pas = 1
            break

