#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:19:42 2016

@author: yannick
"""

#import sys
#
#with open(sys.argv[1], "r") as fichier_lu:
#    CONTENU = fichier_lu.readlines()
#
#a = CONTENU[0].strip("\n\r\t ")
#b = CONTENU[1].strip("\n\r\t ")

#for i in range(0,len(a)-len(b)+1):
#    if a[i:].startswith(b):
#        print i+1,

a = "GATATATGCATATACTT"
b = "ATAT"

i = 0

while 1:
    try:
        location = a[i:].index(b)   #check on i
        print  location + i + 1,    #our result
        i += location + 1           #new i, the intermediates are avoided
    except:
        break                       #if no result


