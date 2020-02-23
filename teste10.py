#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:43:33 2019

@author: ist195550
"""

class urna:
    
    def __init__ (self, candidatos):
        self.candidatos = candidatos
        self.res = {}
        for cand in self.candidatos:
            self.res[cand] = 0
        self.res["Nulos"] = 0
        
    def vota (self, voto):
        if voto in self.candidatos:
            self.res[voto] += 1
        else:
            self.res["Nulos"] += 1
            
    def resultados(self):
        vencedor = ""
        votos_vencedor = 0
        for cand in self.res:
            if cand != "Nulos" and self.res[cand] > votos_vencedor:
                vencedor = cand
                votos_vencedor = self.res[cand]
            print (str(cand) + ": " + str(self.res[cand]))
        print ("Vencedor: " + str(vencedor))