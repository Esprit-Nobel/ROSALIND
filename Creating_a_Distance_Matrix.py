#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:26:13 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    CONTENU = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() if elt != "" ]
    for c in xrange(len(CONTENU)):
        if ">" in CONTENU[c]:
            CONTENU[c] = "xxx"
    FASTA = "".join(elta for elta in CONTENU).split("xxx") [1:]

def Dist(s1,s2):
    fit = [ c != v for c,v in zip(s1, s2) ].count(1)
    return round( fit / float(len(s1)) , 5)

for i in xrange(len(FASTA)):
    for j in xrange(len(FASTA)):
        print Dist(FASTA[i],FASTA[j]),
    print









