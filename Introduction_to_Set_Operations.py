#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 15:52:21 2016

@author: yannick
"""

import sys

with open(sys.argv[1], "r") as FILE:
    CONTENU = [ elt.rstrip("\n\r\t ") \
               for elt in FILE.readlines() if elt != "" ]

n = int( CONTENU[0] )
s1 = set( int( elt ) for elt in CONTENU[1].replace("{",""). \
             replace("}","").split(", ") )
s2 = set( int( elt ) for elt in CONTENU[2].replace("{",""). \
             replace("}","").split(", ") )
s3 = set( elta for elta in xrange(1, n+1) )

print "{" + ", ".join( str( elt ) for elt in s1 | s2) + "}"
print "{" + ", ".join( str( elt ) for elt in s1 & s2) + "}"
print "{" + ", ".join( str( elt ) for elt in s1 - s2) + "}"
print "{" + ", ".join( str( elt ) for elt in s2 - s1) + "}"
print "{" + ", ".join( str( elt ) for elt in s3 - s1) + "}"
print "{" + ", ".join( str( elt ) for elt in s3 - s2) + "}"
