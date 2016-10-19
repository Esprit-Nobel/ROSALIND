#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:38:35 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    SEQ = [LINE.strip("\n\r\t ") for LINE in fichier_lu if LINE != ""]

aa = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2, \
      'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4, \
      'A': 4, 'D': 2, 'E': 2, 'G': 4}

TOT = 3

for elt in SEQ[0]:
    TOT *= aa[elt]

print TOT % 1000000







