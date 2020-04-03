#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:13:50 2019

@author: ist195550
"""

def apenas_digitos_impares (n):
    if not (isinstance (n, int) and n >= 0):
        raise ValueError ("Nao definido")
    elif n == 0:
        return 0
    elif n % 2 != 0:
        return apenas_digitos_impares (n // 10) * 10 + n % 10
    else:
        return apenas_digitos_impares (n // 10)