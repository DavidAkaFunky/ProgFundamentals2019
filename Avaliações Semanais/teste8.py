#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:56:46 2019

@author: ist195550
"""

def soma_valores (dic):
    soma = 0
    for chave in dic:
        if isinstance(dic[chave], list):
            for num in dic[chave]:
                soma += num
        elif isinstance(dic[chave], int):
            soma += dic[chave]
    return soma