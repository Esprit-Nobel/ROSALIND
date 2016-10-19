#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:48:13 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as READ:
    READ_2 = [ LINES.strip("\n\r\t ") for LINES in READ.readlines() ]
    for o in xrange(len(READ_2)):
        if ">" in READ_2[o]:
            READ_2[o] = "x_x_x"
    GLOBAL = "".join(tle for tle in READ_2)
    FINAL = GLOBAL.split("x_x_x") [1:]
    PATTERNS = set(FINAL[1:])

SEQUENCE = FINAL[0]

while len(PATTERNS) != 0 :
    for elt in PATTERNS:
        TO_DEL = 0
        for i in xrange((len(elt)/2)-1, len(elt)):
            if elt.startswith(SEQUENCE[-i:]):
                SEQUENCE += elt[i:]
                TO_DEL = 1
                break
        if TO_DEL == 0:
            for u in xrange((len(elt)/2)-1, len(elt)):
                if elt.endswith(SEQUENCE[:u]):
                    SEQUENCE = elt[:-u] + SEQUENCE
                    TO_DEL = 1
                    break
        if TO_DEL == 1:
            break
    if TO_DEL == 1:
        PATTERNS.remove(elt)

print SEQUENCE



