#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:59 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

a = CONTENU[0].strip("\n\r\t ")
b = CONTENU[1].strip("\n\r\t ")

print [ c == v for c,v in zip(a, b) ].count(False)
print sum( [ c != v for c, v in zip(a, b)] )
