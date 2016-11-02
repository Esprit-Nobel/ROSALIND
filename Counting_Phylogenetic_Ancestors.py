#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:42:54 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = [ elt.rstrip("\n\r\t ") \
               for elt in fichier_lu.readlines() if elt != "" ]

n = int( CONTENU[0] )

print n-2

