#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:13:20 2019

@author: ist195550
"""

def serie_geom (r, n):
    if not (isinstance (r, int) and n >= 0):
        raise ValueError ("Nao esta definido")
    i = 0
    total = 0
    while i <= n:
        total += r**i
        i += 1
    return total