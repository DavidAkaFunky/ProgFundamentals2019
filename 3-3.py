#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:14:27 2019

@author: ist195550
"""
def area_circulo (r):
    if not (isinstance (r,int) or isinstance (r,float)) or r <= 0:
        raise ValueError ("O raio tem de ser um número positivo!")
    return r * r * 3.14