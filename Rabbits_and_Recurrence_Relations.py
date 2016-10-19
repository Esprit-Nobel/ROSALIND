#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:16:39 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

for elt in CONTENU:
    lili = elt.split()
    n = int(lili[0])
    k = int(lili[1])

a = 1
b = 1

for i in range(3,n+1):
    a,b = b,(k*a+b)

print b