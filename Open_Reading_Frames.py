#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 11:40:28 2016

@author: yannick
"""

import sys
import re

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

SEQ = ""
for elta in CONTENU:
    if ">" not in elta and elta != "":
        SEQ += elta.strip("\n\r\t ")

CHAINES = [SEQ]

DICO = {
    'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
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

CHAINES.append(SEQ.replace("A","t").replace("C","g").replace("G","c") \
           .replace("T","a").upper() [::-1] )

r = "ATG"
TROUVE = []

for entries in CHAINES:
    ATG = re.finditer(r, entries)

    for elt in ATG:
        s = elt.start()
        PROT = ""
        for i in xrange(s, len(entries)-2, 3):
            mot = entries[i:i+3]
            if DICO[mot] == "Stop" and PROT not in TROUVE:
                TROUVE.append(PROT)
                print PROT
                break
            if DICO[mot] != "Stop":
                PROT += DICO[mot]
            else:
                break












