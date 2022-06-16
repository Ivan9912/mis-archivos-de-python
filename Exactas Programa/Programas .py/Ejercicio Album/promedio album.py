# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:34:37 2018

@author: Kalexa
"""

import random
import numpy as np
cantidad_figuritas_paquete= 5
album_lleno= np.arange(1,7)
print ("Album lleno referencia:", album_lleno)
def jugada (album):
    count =0
    while all (album) != all (album_lleno):
        dado = random.randint(1,6)
        print ("Dado:", dado)
        print ("")
        count = count +1
        print ("count:", count)
        if album [dado -1]==0:
            album [dado -1]=dado
    return count
album_por_llenar = [0]*6
album = jugada (album_por_llenar)
print ("")
print ("Cantidad de figuritas que se necesito para completar el Album:", album)
print ("")
print ("Resultado del Album completo:", album_por_llenar)
print ("")
#print ("Resultado de x:" ,x)
#print ("")
#------------------------------------------------------------------------------

repeticiones = []

#def jugada_2 (otro):
    #while all(repeticiones) != 
for rep in range (10):
    album2 = jugada (album_por_llenar)
    cantidad_de_sobres = 0
    while min (album2) == 0:
        sobre = random.sample (range (album_lleno), cantidad_figuritas_paquete)
        #print ("sobre:", sobre)
        album2 [sobre] += 1
        #print ("Album:", album)
        cantidad_de_sobres += 1
        #print ("cantidad de sobres:", cantidad_de_sobres)
        repeticiones [rep] = cantidad_de_sobres
        print ("jijo:", repeticiones [rep])
sobres_promedio = repeticiones.mean()
print ("promedio:", sobres_promedio)
   