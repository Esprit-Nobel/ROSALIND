#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:57:03 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    ARRAY = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() if elt != "" ]

ARRAY_1 = set( ARRAY )

for elt in ARRAY:
    ARRAY_1.add( elt.replace("A","t").replace("C","g").replace("G","c") \
                .replace("T","a").upper() [::-1] )

RES = set( (elta[:-1], elta[1:]) for elta in ARRAY_1 )

for etl in sorted(RES):
    print "(" + etl[0] + ", " + etl[1] + ")"
