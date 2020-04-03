#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:43:17 2019

@author: ist195550
"""

def lista_digitos (n):
    def transforma (lst, fn):
        if lst == []:
            return lst
        else:
            return [fn(lst[0])] + transforma (lst[1:], fn)
    return transforma (list(str(n)), eval)