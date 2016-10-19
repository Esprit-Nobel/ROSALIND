#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:12:01 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()
    for i in range(len(CONTENU)) :
        if ">" in CONTENU[i]:
            CONTENU[i] = "xxx"
        else:
            CONTENU[i] = CONTENU[i].strip("\n\r\t ")
    SEQS = ( "".join( elta for elta in CONTENU) ).split("xxx")

SEQ_1 = SEQS[1]
SEQ_2 = SEQS[2]

TRANSITION = 0
TRANVERSION = 0

for c, v in zip(SEQ_1, SEQ_2):
    if c != v:
        if c in "AG" and v in "TC" or c in "TC" and v in "AG":
            TRANVERSION += 1
        else:
            TRANSITION += 1

print TRANSITION / float(TRANVERSION)


