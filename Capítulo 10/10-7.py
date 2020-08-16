#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:58:22 2019

@author: ist195550
"""

def ordena_ficheiro (ficheiro):
    if type (ficheiro) != str:
        raise ValueError ("")
    else:
        with open(ficheiro) as f:
            orig = f.readlines()
        for linha in sorted (orig):
            print (linha)