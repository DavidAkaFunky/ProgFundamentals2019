#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:17:22 2019

@author: ist195550
"""

# a/b -> {"n": a, "d": b}

def cria_racional (n,d):
    if not isinstance (n,int) or not isinstance(d,int) or d<=0:
        raise ValueError ("Oops...")
        
def num(r):
    return r["n"]

def den(r):
    return r["d"] 

def eh_racional(arg):
    return isinstance (arg,dict) and len(arg)==2 and "n" in arg and "d" in arg and isinstance (num(r), int) and isinstance (den(r), int) and den (r) > 0

def eh_racional_zero (arg):
    return eh_racional (arg) and num(arg) == 0

# a/b == c/d -> a*d == b*c

def racionais_iguais (r1, r2):
    return num(r1)*den(r2) == num(r2)*den(r1)

# "a/b"
    
def escreve_racional(r):
    if eh_racional_zero (r):
        return "0"
    return str(num(r)) + "/" + str(den(r))

# a/b * c/d = a*b/c*d
    
def produto_racionais(r1,r2):
    return cria_racional (num(r1) * num(r2), den(r1) * den(r2))