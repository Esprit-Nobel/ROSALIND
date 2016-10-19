#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:18:54 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

for elt in CONTENU:
    LINE = elt.strip("\n\r\t ")
    PARA = LINE.split()
    k = int(PARA[0])
    m = int(PARA[1])
    n = int(PARA[2])

N = float(k+m+n)

r = 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) )

print r