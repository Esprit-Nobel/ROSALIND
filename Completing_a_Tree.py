#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:58:02 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()
    CONTENU = [ elt.rstrip("\n\r\t ") for elt in CONTENU ]

print int( CONTENU[0] ) - len(CONTENU[1:]) -1


