#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:18:43 2016

@author: yannick
"""

import sys
import math

with open(sys.argv[1], "r") as fichier_lu:
    CONTENU = fichier_lu.readlines()
    NUM = CONTENU[0].strip("\n\r\t ").split()

TOT = ( math.factorial( long(NUM[0]) ) / \
        math.factorial( long(NUM[0])-long(NUM[1]) ) ) \
         % 1000000

print TOT


