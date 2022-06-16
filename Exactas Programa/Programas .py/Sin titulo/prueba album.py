# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 01:21:13 2018

@author: Kalexa
"""

import random
import numpy as np
#b = list(range(len ([0]*100)))
#print ("hola mundo jeje :", b)
#print ("")
FIGURITAS_POR_PAQUETE = 5
FIGURITAS_POR_ALBUM = 50
CANTIDAD_DE_CORRIDAS = 10
#album = np.zeros (100)
#print ("Album:" , album)
simulacion = np.empty (CANTIDAD_DE_CORRIDAS)
#print ("simulacion:", simulacion)
for i in range (CANTIDAD_DE_CORRIDAS):
    album = np.zeros (FIGURITAS_POR_ALBUM, dtype=int)
    #print ("jojo i:", i)
    #print ("album2:", album)
    cantidad_de_sobres = 0 #= count
    #len (album [album == 0]) > 0
    while min (album) == 0:
        sobre = random.sample (range (FIGURITAS_POR_ALBUM), FIGURITAS_POR_PAQUETE)
        #print ("sobre:", sobre)
        album [sobre] += 1
        #print ("Album:", album)
        cantidad_de_sobres += 1
        #print ("cantidad de sobres:", cantidad_de_sobres)
        simulacion [i] = cantidad_de_sobres
        #print ("jijo:", simulacion[i])
sobres_promedio = simulacion.mean()
print ("promedio:", sobres_promedio)