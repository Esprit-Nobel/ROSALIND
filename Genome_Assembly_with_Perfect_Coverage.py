#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:03:46 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    ARRAY = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() \
                if elt.rstrip("\n\r\t ") != "" ]

SEQ = ARRAY[0]
LR = len(ARRAY[0])-1
DICT = {}

for READ in ARRAY:
    DICT [ READ[:-1] ] = READ[-1]  # perfect coverage + de Bruijn

while 1:
    if SEQ[-LR:] == SEQ[:LR]:
        SEQ = SEQ[:-LR]
        break
    SEQ += DICT [ SEQ[-LR:] ]

print SEQ

