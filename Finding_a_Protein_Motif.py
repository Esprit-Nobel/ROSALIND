#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:28:56 2016

@author: yannick
"""

import sys
from urllib import urlopen
import re

with open(sys.argv[1], "r") as fichier_lu:
    PROTS = [LINE.strip("\n\r\t ") for LINE in fichier_lu if LINE != ""]

uniprot = "http://www.uniprot.org/uniprot/%s.fasta"

find = r"(?=N[^P][ST][^P])"

for protein in PROTS:
    f = urlopen(uniprot % protein).read()
    f = ''.join(f.splitlines()[1:])

    lili = [ elt.start()+1 for elt in re.finditer(find,f) ]
    if lili:
        print protein
        print " ".join(map(str, lili)).rstrip("\n\r\t ")




