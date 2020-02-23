#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:20:46 2019

@author: ist195550
"""

class racional:
    def __init__ (self,num,den):
        if den == 0:
            raise ValueError ("Nao se divide por 0!")
        self.num = num
        self.den = den
        
    def numerador(self):
        return self.num
    
    def denominador(self):
        return self.den
    
    def __eq__ (self,r):
        return self.num * r.denominador() == self.den * r.numerador()
    
    def __repr__ (self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__ (self,r):
        return racional(self.num * r.denominador() + self.den * r.numerador(), self.den + r.denominador())