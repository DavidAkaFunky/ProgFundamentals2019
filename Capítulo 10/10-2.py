#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:22:40 2019

@author: ist195550
"""

def conta_vogais (filename):
    f = open (filename)
    d = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    l = f.readline()
    while l != "":
        for char in l:
            if char in d:
                char += 1
    f.close()
    return d