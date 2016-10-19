#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:49:09 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.read().strip("\n\r\t ").split()

print "\n".join(word + " " + str(CONTENU.count(word)) for word in set(CONTENU))

