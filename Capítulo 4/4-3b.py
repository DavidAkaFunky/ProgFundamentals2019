#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:20:07 2019

@author: ist195550
"""

def implode (t):
    if not isinstance (t, tuple):
        raise ValueError ("Implode: elemento nao inteiro")
    else:
        res = 0
        for d in t:
            if not isinstance (d, int) and 0 <= d <= 9:
                raise ValueError ("Implode: elemento nao inteiro")
            else:
                res = res * 10 + d
                return res

tuplo = ("Insira um tuplo com digitos inteiros: ")
print (implode (tuplo))