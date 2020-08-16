#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:04:29 2019

@author: ist195550
"""
def cria_lista_nums (n):
    if not (isinstance (n, int) and n > 0):
        raise ValueError ("Nao esta definido")
    else:
        lista = []
        for i in range(10):
            lista += [n * i]
        return lista