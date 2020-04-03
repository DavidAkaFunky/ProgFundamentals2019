#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 11:51:36 2019

@author: ist195550
"""

def produto_digitos (n, pred):
    def lista_digitos (n):
        def transforma (lst, fn):
            if lst == []:
                return lst
            else:
                return [fn(lst[0])] + transforma (lst[1:], fn)
        return transforma (list(str(n)), eval)
    def filtra(lst,tst):
        if lst == []:
            return lst
        elif tst(lst[0]):
            return [lst[0]] + filtra(lst[1:], tst)
        else:
            return filtra(lst[1:], tst)
    def acumula (lst, fn):
        if len(lst) == 1:
            return lst[0]
        else:
            return fn(lst[0], acumula(lst[1:], fn))
    return acumula(filtra(lista_digitos(n), pred), lambda x, y: x*y)