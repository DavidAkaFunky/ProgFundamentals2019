#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:15:49 2019

@author: ist195550
"""

numero = eval(input("Escreva um numero: "))
n = 0
num_novo = 0
while numero > 0:
    digito = numero % 10
    if digito % 2 == 1:
        if digito == 9:
            digito = 1
        else:
            digito = digito + 2
    else:
        if digito == 0:
            digito = 8
        else:
            digito = digito - 2
    numero = numero // 10
    num_novo = num_novo + digito * (10 ** n)
    n = n + 1
print ("O numero correspondente e:", num_novo)