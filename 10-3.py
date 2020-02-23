#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:27:43 2019

@author: ist195550
"""

def inverte (file1, file2):
    with open(file1) as f:
        linhas = f.readlines()
    invertido = []
    for linha in linhas:
        invertido = [linha] + invertido
    with open(file2, "w") as f:
        f.writelines (invertido)