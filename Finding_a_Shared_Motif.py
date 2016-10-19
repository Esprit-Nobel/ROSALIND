#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:30:26 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

ARRAY_OF_SEQS = []
SEQ = ""
for elt in CONTENU[1:]:
    LINE = elt.strip("\n\r\t ")
    if ">" not in LINE:
        SEQ += LINE
    if ">" in LINE or elt == CONTENU[-1]:
        ARRAY_OF_SEQS.append(SEQ)
        SEQ = ""

FIRST_SEQ = ARRAY_OF_SEQS[0]
SET_SEQ = set(ARRAY_OF_SEQS[1:])


SIZE_FIRST = len(FIRST_SEQ)                     #
KMERS = set()                                   # which
for START in xrange(SIZE_FIRST-1):              #
    for END in xrange(START+2, SIZE_FIRST+1):   # are
        KMERS.add(FIRST_SEQ[START:END])         #
        END += 1                                # k-mers?
    START += 1                                  #

ABSENT = set()                                  #
for MER in KMERS:                               # where
    for SEQ in SET_SEQ:                         #
        if MER not in SEQ:                      # aren't
            ABSENT.add(MER)                     #
            break                               # they?

PRESENT = set.difference(KMERS,ABSENT)
PRESENT_SORTED = sorted(PRESENT,key=lambda x:len(x))

print PRESENT_SORTED[-1]
