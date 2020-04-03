#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:23:15 2019

@author: ist195550
"""

def junta_ordenados (l1, l2):
    if not (isinstance (l1, list) and isinstance (l2, list)):
        raise ValueError ("Nao esta definido")
    if l1 == [] or l2 == []:
        return l1 + l2
    if l1[0] <= l2[0]:
        return [l1[0]] + junta_ordenados (l1[1:], l2)
    else:
        return [l2[0]] + junta_ordenados (l1, l2[1:])