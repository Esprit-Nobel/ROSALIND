#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 12:32:18 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

d = {}
TITLE = ""
SEQ = ""

for elt in CONTENU:
    LINE = elt.strip("\n\r\t ")
    if ">" not in LINE:
        SEQ += LINE

    if ">" in LINE or elt == CONTENU[-1]:
        if TITLE == "":
            TITLE = LINE [1:]
        else:
            d[TITLE] = SEQ
            TITLE = LINE [1:]
            SEQ = ""

for c,v in d.items():
    d[c] = round( ((v.count("G")+v.count("C"))/float(len(v)))*100 ,6)

for c,v in d.items():
    if v == max(d.values()):
        print c
        print v
