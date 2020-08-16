#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:16:47 2019

@author: ist195550
"""

class estacionamento:
    def __init__ (self,lotacao):
        self.lotacao = lotacao
        self.ocup = 0
    def entra(self):
        if self.ocup == self.lotacao:
            raise ValueError ("Estacionamento cheio")
        else:
            self.ocup += 1
    def sai(self):
        if self.ocup == 0:
            raise ValueError ("Estacionamento vazio")
        else:
            self.ocup -= 1
    def lugares(self):
        return self.lotacao - self.ocup