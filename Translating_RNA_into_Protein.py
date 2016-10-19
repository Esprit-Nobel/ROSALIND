#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:40:21 2016

@author: yannick
"""

rep = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
       "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
       "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
       "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
       "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
       "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
       "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
       "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
       "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
       "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
       "UAA": "", "CAA": "Q", "AAA": "K", "GAA": "E",
       "UAG": "", "CAG": "Q", "AAG": "K", "GAG": "E",
       "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
       "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
       "UGA": "", "CGA": "R", "AGA": "R", "GGA": "G",
       "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

for elt in CONTENU:
    LINE = elt.strip("\n\r\t ")

PROT = ""

for i in xrange(0, len(LINE), 3):
    PROT += rep[ LINE[i:i+3] ]

print PROT