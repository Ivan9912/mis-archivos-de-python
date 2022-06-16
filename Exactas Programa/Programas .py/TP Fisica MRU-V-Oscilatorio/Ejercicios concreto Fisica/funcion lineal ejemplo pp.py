# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 16:44:36 2018

@author: Kalexa
"""

import matplotlib . pyplot as plt
#import numpy as np
# Primero voy a crear tres listas vacias
v1 = []
v2 = []
v3 = []
# Despues creo una variable que llamo numero y empieza siendo cero
numero = 0
numero_final = 10
paso = 0.01
# v1 va a ser una lista de 11 numeros ordenados del 0 al 10
# v2 va a ser el cuadrado de v1
while numero <= numero_final :
    v1. append ( numero ) # agarro v1 , le agrego al final el valor de numero
    v2. append ( numero ** 2) # agarro v2 , le agrego al final numero al cuadrado
    v3. append ( numero ** 3) # idem , al cubo
    numero = numero + paso # numero va saltando de dos en dos
# Grafico v2 en funcion de v1
# Esto deberia ser una funcion cuadratica ya que punto a punto v2=v1 ^2
plt. plot (v1 , v2 , ".")
plt. plot (v1 , v3 , ".")
# Muestro lo que grafico en pantalla
plt. show ()
# Primero puntos , despues afinar la grilla , y despues sacar el "."

