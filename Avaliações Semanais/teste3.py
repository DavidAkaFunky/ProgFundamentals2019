#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:09:06 2019

@author: ist195550
"""

def conta_maiores (tuplo, num):
    if not (isinstance (tuplo, tuple) and isinstance (num, int)):
        raise ValueError
    else:
        n = 0
        for i in tuplo:
            if not isinstance (i, int):
                raise ValueError
            else:
                if num > i:
                    n += 1
        return n