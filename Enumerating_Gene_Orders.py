#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:36:14 2016

@author: yannick
"""

import sys
import itertools

with open(sys.argv[1], "r") as fichier_lu:
    VALEUR = int( fichier_lu.read() )

p = itertools.permutations(xrange(1,VALEUR+1))

lili = [ elt for elt in p]

print len(lili)

for elta in lili:
    for eltb in elta:
        print eltb,
    print
