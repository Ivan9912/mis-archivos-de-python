# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:47:27 2018

@author: Kalexa
"""

V1 = []
#V2 = []

#r = 0
def Acel (X, V, T) :
    i = 0
    while i <= T :
    
        V1.append (i)
        A = (int(30 + V*i))
        i=i+1
        
    return A
Aceleración = Acel (1, 5, 15)
print ("Acel:", Aceleración)