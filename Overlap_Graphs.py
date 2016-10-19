#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:19:18 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

DICO_SEQ = {}
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
            DICO_SEQ[TITLE] = SEQ
            TITLE = LINE [1:]
            SEQ = ""

#for TITLE1, SEQ1 in DICO_SEQ.items():
#    for TITLE2, SEQ2 in DICO_SEQ.items():
#        if TITLE1 != TITLE2:
#            if SEQ2[:3] == SEQ1[-3:]:
#                print TITLE1,TITLE2

for SEQ1 in DICO_SEQ:
    for SEQ2 in DICO_SEQ:
        if SEQ1 != SEQ2:
            if DICO_SEQ[SEQ2][:3] == DICO_SEQ[SEQ1][-3:]:
                print SEQ1,SEQ2
