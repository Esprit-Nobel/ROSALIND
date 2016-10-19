#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:31:36 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()

TABLEAU_PRINCIPAL = []
SEQ = ""
for elt in CONTENU[1:]:
    LINE = elt.strip("\n\r\t ")
    if ">" not in LINE:
        SEQ += LINE
    if ">" in LINE or elt == CONTENU[-1]:
        TABLEAU_PRINCIPAL.append(SEQ)
        SEQ = ""

COLS = []
for i in range(len(TABLEAU_PRINCIPAL[1])):
    temp = []
    for ENTRIES in TABLEAU_PRINCIPAL:
        temp.append(ENTRIES[i])
    COLS.append(temp)

A = [] ; C = [] ; G = [] ; T = [] ; CONS = ""
for elt in COLS:
    tp = 0
    A.append(elt.count("A"))
    if elt.count("A") > tp:
        tp = elt.count("A")
        tpl = "A"
    C.append(elt.count("C"))
    if elt.count("C") > tp:
        tp = elt.count("C")
        tpl = "C"
    G.append(elt.count("G"))
    if elt.count("G") > tp:
        tp = elt.count("G")
        tpl = "G"
    T.append(elt.count("T"))
    if elt.count("T") > tp:
        tp = elt.count("T")
        tpl = "T"
    CONS += tpl

print CONS

print "A:",
for elt in A:
    print elt,
print
print "C:",
for elt in C:
    print elt,
print
print "G:",
for elt in G:
    print elt,
print
print "T:",
for elt in T:
    print elt,
print
