#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:05:34 2019

@author: ist195550
"""

def conta_duplicados (fich):
    f = open(fich)
    d = {}
    l = f.readline()
    linhas = 0
    while l != "":
        linhas += 1
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                if l[i] not in d:
                    d[l[i]] = 1
                else:
                    d[l[i]] += 1
        l = f.readline()
    f.close()
    return (linhas, d)