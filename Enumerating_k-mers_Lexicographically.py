#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:46:47 2016

@author: yannick
"""

import sys
import itertools
with open(sys.argv[1], "r") as fichier_lu:
    READ = fichier_lu.readlines()
    LINES = [ elt.strip("\n\r\t ") for elt in READ ]

alphabet = sorted( LINES[0].split() )
N = int(LINES[1])

for elt in itertools.product(alphabet, repeat=N):
    print "".join(map(str,  elt))

