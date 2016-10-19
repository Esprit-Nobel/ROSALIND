#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:49:18 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    SEQ = "".join(x.strip("\n\r\t ") for x in FILE.readlines()[1:])

SEQ_INV = SEQ.replace("A","t").replace("C","g").replace("G","c") \
           .replace("T","a").upper()

for i in xrange(len(SEQ)):
    for j in xrange(i+2, len(SEQ)):

        if SEQ[i:j] == SEQ_INV[j:i:-1]:
            print i+1, j-i+1
        if j-i > 12:
            break

