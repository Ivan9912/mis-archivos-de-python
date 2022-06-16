# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:42:06 2018

@author: Kalexa
"""

import random
import numpy as np

CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM = 30
CANTIDAD_DE_FIGUS_PARA_1_PAQUETE = 5
PAQUETE_DE_FIGUS = [] #vacio, a llenar previamente
ALBUM_A_LLENAR_OTRAVEZ = [0]*CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM
print (ALBUM_A_LLENAR_OTRAVEZ)
print ("")
ALBUM_LLENO = np.arange (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM+ 1)
print (ALBUM_LLENO)
print ("")
#Album = 

for uno in range (CANTIDAD_DE_FIGUS_PARA_1_PAQUETE):
    DADO = random.randint (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
    PAQUETE_DE_FIGUS.append (DADO)
    
print ("jeje:", PAQUETE_DE_FIGUS)
print ("")

#while all (ALBUM_A_LLENAR_OTRAVEZ) != all (ALBUM_LLENO):
PAQUETE_DE_FIGUS_VISUALIZAR = PAQUETE_DE_FIGUS
k = 0
while k <= 4:
    k = k+1
    FIGUS_IND = PAQUETE_DE_FIGUS_VISUALIZAR[k-1]
    print ("ohsi:", FIGUS_IND)
    if ALBUM_A_LLENAR_OTRAVEZ [FIGUS_IND-1] == 0:
        ALBUM_A_LLENAR_OTRAVEZ [FIGUS_IND -1] = FIGUS_IND
print ("Lectura de cada uno:", PAQUETE_DE_FIGUS_VISUALIZAR[k-1])
print ("")
print (ALBUM_A_LLENAR_OTRAVEZ)
print ("")


