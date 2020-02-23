#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:50:25 2019

@author: ist195550
"""

def corta (file_in, file_out, n):
    if type(file_in) != str or type(file_in) != str or type(n) != int or n < 0:
        raise ValueError ("")
    else:
        with open(file_in) as f:
            f_in = f.read()
        out = ""
        for i in range(n+1):
            out += f_in[i]
        with open(file_out, "w") as f:
            f.write(out)