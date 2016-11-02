#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:18:15 2016

@author: yannick
"""

import sys
import math

with open(sys.argv[1], "r") as FILE:
    ARRAY = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() if elt != "" ]

for RATES in [ float( elt ) for elt in ARRAY[1].split() ]:
    PROB = (RATES / 2) ** sum( cg in ("G", "C") for cg in ARRAY[0] ) * \
        ( (1-RATES) / 2 ) ** sum( at in ("A", "T") for at in ARRAY[0] )
    print round( math.log10(PROB),3 ),
