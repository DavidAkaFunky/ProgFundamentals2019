#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:20:32 2019

@author: ist195550
"""

def conta_linhas (filename):
    f = open (filename)
    linhas = f.readlines ()
    f.close()
    total = 0
    for l in linhas:
        if l != "\n":
            total += 1
    return total