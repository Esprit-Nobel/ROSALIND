#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:40:11 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

for elt in CONTENU:
    LINE = elt.strip("\n\r\t ")
    PARA = LINE.split()
    a = int(PARA[0])
    b = int(PARA[1])
    c = int(PARA[2])
    d = int(PARA[3])
    e = int(PARA[4])
    f = int(PARA[5])

print (a*4 + b*4 + c*4 + d*3 + e*2) /float(2)

