#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:57:14 2019

@author: ist195550
"""

def prod_cubos (lst):
    def transforma (lst, fn):
        if lst == []:
            return lst
        else:
            return [fn(lst[0])] + transforma (lst[1:], fn)
    def acumula (lst, fn):
        if len(lst) == 1:
            return lst[0]
        else:
            return fn(lst[0], acumula(lst[1:], fn))
    return acumula(transforma(lst, lambda x: x**3), lambda x, y: x*y)