#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:47:14 2019

@author: ist195550
"""

class fila:
    
    #Construtores
    def __init__ (self):
        """Fila: --> Fila"""
        self.f = []
        
    def copia(self):
        cp = fila()
        for el in self.f:
            cp.coloca(el)
        return cp
    
    
    #Seletores    
    def inicio (self):
        """Inicio: Fila --> Inteiros"""
        try:
            return self.f[0]
        except IndexError:
            print ("Primeiro: A fila nao tem elementos")
            
    def comprimento (self):
        """Comprimento: Fila --> Inteiro"""
        return len(self.f)
    
    #Modificadores
    def coloca (self, elemento):
        """Coloca: Fila X Universal --> Fila"""
        self.f.append(elemento)
        
    def retira (self):
        """Retira: Fila --> Fila"""
        try:
            self.f.pop(0)
            return self
        except IndexError:
            print ("Retira: A fila nao tem elementos")
            
    def vazia (self):
        return len(self.f) == 0
    
    def __repr__ (self):
        f = "<<"
        if self.f != []:
            for i in range(len(self.f)-1):
                f += str (self.f[i]) + " "
            f += str (self.f[-1])
        f += "<<"
        return f
    
    #Outros
    def soma_elementos (self):
        fila_nova = self.copia()
        soma = 0
        while not fila_nova.vazia():
            soma += fila_nova.inicio()
            fila_nova.retira()
        return soma