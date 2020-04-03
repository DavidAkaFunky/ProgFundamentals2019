#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:46:14 2019

@author: ist195550
"""

def procura (word, fich):
    if type(word) != str or type(fich) != str:
        raise ValueError ("")
    else:
        with open(fich) as f:
            linhas = f.readlines()
        for linha in linhas:
            if word in linha:
                print (word)