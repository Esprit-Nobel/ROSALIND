#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:00:45 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()
    SEQ = "".join( elt.strip("\n\r\t ") for elt in CONTENU[1:-2] )
    SEARCH = CONTENU[-1].strip("\n\r\t ")

x = 0
for letter in SEARCH:
    b = SEQ[x:].index(letter)
    print b + x + 1,
    x += b + 1

