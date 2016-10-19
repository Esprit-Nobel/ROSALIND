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
    m = int(lili[1])

live = [1]*n
for i in range(2,n):
    live[i] = live[i-2] + live[i-1]
    if i>= m:
        live[i] -= live[i-m-1]

print live[-1]

