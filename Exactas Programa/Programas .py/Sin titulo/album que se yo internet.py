# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:57:39 2018

@author: Kalexa
"""

import random
import numpy as np
import matplotlib.pyplot as plt
sobre = random.sample (range(669), 5)
print ("Sobre de figuritas:", sobre)
print ("")
dado = random.randint (1, 6)
print ("Dado:", dado)
print ("")
FIGURITAS_POR_PAQUETE = 5
FIGURITAS_POR_ALBUM = 669
CANTIDAD_DE_CORRIDAS = 1000
simulacion = np.empty (CANTIDAD_DE_CORRIDAS)
#print ("cantidad de corridas:", simulacion)
for i in range (CANTIDAD_DE_CORRIDAS):
    album = np.zeros (FIGURITAS_POR_ALBUM, dtype=int)
    cantidad_de_sobres = 0
    #len (album [album == 0]) > 0
    while min (album) == 0:
        sobre = random.sample (range (FIGURITAS_POR_ALBUM), FIGURITAS_POR_PAQUETE)
        album [sobre] += 1
        cantidad_de_sobres += 1
        simulacion [i] = cantidad_de_sobres

sobres_promedio = simulacion.mean()
#---------------------------------------------------------------
plt.hist (simulacion, bins = 50)
plt.axvline (sobres_promedio, color = 'r')
plt.legend (["%.2f sobres" % sobres_promedio])
plt.title ("Cantidad de sobres en promedio para llenar 1 albúm")
plt.show()
