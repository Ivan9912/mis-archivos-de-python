# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 01:00:10 2018

@author: Kalexa
"""
import matplotlib.pyplot as plt

V1 = []
V2 = []




def holis (a):
    c = 0
    
    count = 0
    while  c <= a:
        V1.append (count)
        count = count + 1
        V2.append (c)

        

    while  c >= a: 
        V2.append (c)

    return c
Hola = holis (100)


            
    
    
    
print (V1)
              
#plt. plot (V1 , V2, color = 'r' )
#plt.legend (["v2"])
#plt.title ("3- Movimiento Oscilatorio (Vehiculo)")
#plt. show ()
#print ("")
