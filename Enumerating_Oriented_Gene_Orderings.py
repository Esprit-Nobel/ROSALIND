#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:29:21 2016

@author: yannick
"""

import sys
import itertools

with open(sys.argv[1], "r") as fichier_lu:
    VALEUR = int( fichier_lu.read() )

p = itertools.permutations( \
            [x for x in xrange(-VALEUR,VALEUR+1) \
            if x != 0 ] \
            , VALEUR) \

pp = [ y for y in p \
      if set(range(1, VALEUR+1)) == set(map(abs,y)) \
      ]

lili = [ elt for elt in pp]

print len(lili)

for elta in lili:
    for eltb in elta:
        print eltb,
    print





