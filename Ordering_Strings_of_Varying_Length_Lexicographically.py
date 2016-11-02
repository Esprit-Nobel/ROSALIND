#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:36:14 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    ARRAY = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() if elt != "" ]

alphabet = ARRAY[0].split()
nb = int( ARRAY[1] )

def generate(nb, h=""):
    print h
    if nb == 0:
        return
    for c in alphabet:
        generate(nb-1, h+c)

generate(nb)
