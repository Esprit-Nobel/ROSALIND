#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:59:11 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    READ = fichier_lu.readlines() [1:]
    LINES = [ elt.strip("\n\r\t ") for elt in READ ]

DICO = {'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
        'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
        'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
        'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
        'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
        'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
        'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
        'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
        'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
        'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
        'TAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
        'TAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
        'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
        'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
        'TGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
        'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G' }

SEQ = ""
for ii in xrange(len(LINES)):
    ADD = LINES[ii]
    if ">" in ADD:
        break
    SEQ += ADD

for INTRON in LINES[ii+1::2]:
    SEQ = SEQ.replace(INTRON,"")

PROT = ""
for i in xrange(0,len(SEQ)-2,3):
    AA = DICO[ SEQ[i:i+3] ]
    if AA == "Stop":
        break
    PROT += AA

print PROT

