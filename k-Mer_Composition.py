#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:47:10 2016

@author: yannick
"""

import sys
import itertools
import re

with open(sys.argv[1], "r") as FILE:
    CONTENU = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() [1:] if elt != "" ]

STR = "".join( elta for elta in CONTENU)

for KM in itertools.product('ACGT', repeat=4):
    SEARCH = "".join(eltb for eltb in KM)
    print len( re.findall( r'(?=('+ \
                "".join(eltb for eltb in KM) \
                +'))', STR) ),



