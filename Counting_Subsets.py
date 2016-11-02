#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:28:01 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    CONTENU = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() if elt != "" ]

print 2 ** int( CONTENU[0] ) % 1000000