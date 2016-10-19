#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:47:52 2016

@author: yannick
"""

import sys
from math import factorial as fac

with open(sys.argv[1]) as f:
    k, n = map(int, f.next().split())

orgs = 2 ** k

print sum(3. ** (orgs - ni) / (fac(ni) * fac(orgs - ni))
        for ni in xrange(n, orgs+1)) * fac(orgs) / 4. ** orgs



