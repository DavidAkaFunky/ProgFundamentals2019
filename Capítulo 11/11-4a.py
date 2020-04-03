#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:33:25 2019

@author: ist195550
"""

class conjunto:
    def __init__ (self, *els):
        self.data = []
        for el in els:
            if el not in self.data:
                self.data.append(el)
                
    def __repr__ (self):
        out = "{"
        for el in self.data[:-1]:
            out += str(el) + ","
        if len(self.data) != 0:
            out += str(self.data[-1])
        out += "}"
        return out