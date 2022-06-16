# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 18:47:17 2018

@author: Kalexa
"""
import random

CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM = 30
PAQUETE_DE_FIGUS = []
CANTIDAD_DE_FIGUS_PARA_1_PAQUETE = 5


for i in range (CANTIDAD_DE_FIGUS_PARA_1_PAQUETE):
    dado = random.randint (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
    PAQUETE_DE_FIGUS.append (dado)
    print ("dado:", dado)
    print ("")  
print ("lista :", PAQUETE_DE_FIGUS)
print ("")
#hola = PAQUETE_DE_FIGUS
#print ("jeijo:", hola)
#print ("")

#------------------------------------------------------------------------------
Album = [0]*CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM
print ("Album:", Album)
print ("")
def palabra (h):
    k=0
    while k < len (h):
        if h[k] != 0:
            Album [k] = h [k]
        elif h [6-1] ==0:
            Album [6-1]=0
        k = k+1
    return h

jojo = palabra (PAQUETE_DE_FIGUS)
print ("juajua:", jojo)
print ("")
                


