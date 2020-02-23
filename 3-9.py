#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:49:40 2019

@author: ist195550
"""
def is_primo (n):
    if not isinstance (n,int) or n <= 1:
        raise ValueError ("O número não é um inteiro maior que 1!")
    from math import sqrt
    i = 2
    while i <= sqrt (n):
        if n % i == 0:
            return False
        i += 1
    return True

def n_esimo_primo (n):
    numero = 2
    i = 2
    while i <= n:
        numero += 1
        if is_primo (numero):
            i += 1
    return numero