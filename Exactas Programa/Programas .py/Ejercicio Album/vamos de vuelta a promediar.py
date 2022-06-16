# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:49:58 2018

@author: Kalexa
"""

import random
import numpy as np
#cantidad_figuritas_paquete= 5
total_de_figuritas = 6
repe= 10
album_lleno = np.arange (1, total_de_figuritas + 1)
#print ("Album lleno referencia:", album_lleno)
rep = []
for i in range (repe):
    #print ("jeje:", i)
    def jugada (album):
        count =0
        while all (album) != all (album_lleno):
            dado = random.randint (1, total_de_figuritas)
        #print ("Dado:", dado)
        #print ("")
            count = count + 1
        #print ("count:", count)
            if album [dado -1] == 0:
                album [dado -1] = dado
        return count
    album_por_llenar = [0] * total_de_figuritas
#------------------------------------------------------------------------------    
    #print ("Resultado del album sin completar:", album_por_llenar)
    #print ("")
    album = jugada (album_por_llenar)
    
    print ("Cantidad de figuritas que se necesito para completar el Album:", album)
    #print ("")
    #print ("Resultado del Album completo:", album_por_llenar)
    #print ("")


    #if rep (len (rep)) == 0:
        #rep (album) = album
    rep.append (album)
    print ("Total:" , rep)
promedio = np.mean (rep, dtype = int)
print ("Este es el promedio, al fin:", promedio)


#------------------------------------------------------------------------------
