# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 20:51:11 2018

@author: Kalexa
"""

import matplotlib . pyplot as plt
#import numpy as np

v1 = []
v2 = []
v3 = []

número = 0
número_final = 10

while número <= número_final :
    v1.append ( número )        
    v2.append ( número ** 2)  # ** 2 = "Al cuadrado".
    v3.append ( número ** 3)  # ** 3 = "Al cubo".
    número = número + 0.01    # Número va saltando de 0,01 en 0,01.
                              # Gráfico v2 en funcion de v1.
                                
                              # Esto debería ser una función cuadrática _
                              # ya que punto a punto: v2= v1 ^ 2, Y v3= v1 ^ 3.

plt. plot (v1 , v2, color = 'r' )
plt. plot (v1 , v3, color = 'b' )
plt.legend (["v2"])
plt.title ("MRU")
plt. show ()



