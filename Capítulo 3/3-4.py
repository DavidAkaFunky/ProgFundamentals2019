#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:30:56 2019

@author: ist195550
"""

def area_circulo (r):
    if not (isinstance (r,int) or isinstance (r,float)) or r <= 0:
        raise ValueError ("O raio tem de ser um número positivo!")
    return r * r * 3.14

def area_coroa (r1,r2):
    return abs (area_circulo (r1) - area_circulo (r2))