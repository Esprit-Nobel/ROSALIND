#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:45:07 2016

@author: yannick
"""

import sys
import math

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines() [1:]
    STR = "".join( elt.rstrip("\n\r\t ") for elt in CONTENU )

TOT = long( math.factorial(STR.count("A")) ) * \
        long( math.factorial(STR.count("C")) )

print TOT

