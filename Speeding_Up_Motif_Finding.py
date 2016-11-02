#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:00:27 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    ARRAY = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() if elt != "" ]

STR = "".join(elt for elt in ARRAY[1:])

B_A = [0]*len(STR)
bord = 0

for last in range(1,len(STR)) : # on prend une lettre de plus a droite

# etape 3
    while ( bord > 0 and STR[bord] != STR[last] ) :
    # on ne vient la que si ya deja un bord et que ca ne matche plus
    # on boucle tant que ca ne matche pas
        bord = B_A[bord-1]
    # on matche en sens inverse
    # penser a la double symetrie pour comprendre
    # les bords ont des bords propres :o)

# etape 1
    if STR[bord] == STR[last] :
    # on compare 2 lettres
    # on compare l'allongement du bord en comparant une lettre de plus à droite
    # ca matche donc bord +1
        bord += 1
    # ici bord et last s'incrémentent donc en même tps

# etape 2
    B_A[last] = bord
    # on stocke la longueur du bord à la bonne position
    # si rien ne matche alors 0
    # ensuite on teste la lettre suivante

print " ".join( str(elt) for elt in B_A)



