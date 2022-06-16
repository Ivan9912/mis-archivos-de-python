# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:40:52 2018

@author: Kalexa
"""

 #if repeticiones [album]==0:
        #repeticiones [album]= album
    #else:
    #repeticiones.append (album)
        
        #if rep< len [repeticiones]:
    print ("Este es el range:", rep)
    print ("")
    #return rep
    #lol =
print ("repeticiones:", repeticiones)
print ("")
#lolol= jugada_2 (repeticiones)
print ("rep 2:" , repeticiones)
print ("")
promedio = np.mean(repeticiones)
resultado = int (promedio)
print (repeticiones)
print ("")
print ("El promedio de paquetes de figuritas a comprar es:", resultado)
 

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
        print ("jijo:", simulacion[i])
sobres_promedio = simulacion.mean()
print ("promedio:", sobres_promedio)