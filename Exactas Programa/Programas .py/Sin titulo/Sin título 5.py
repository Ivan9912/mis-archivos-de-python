# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:53:41 2018

@author: Kalexa
"""

import random
import numpy as np
def jugada_bis (posiciones):
    album = [0]*posiciones
    count = 0
    while sum (album)<posiciones:
        count =count+1
        dado = random.randint(1,posiciones+1)
        if posiciones[dado -1]==0:
            posiciones [dado -1]=dado
        print ("count:", count)
    return count
posiciones = 100
repeticiones = []
rep = 1000
x= jugada_bis (posiciones)
for i in range (rep):
    repeticiones.append (posiciones)
promedio = np.mean(repeticiones)
resultado = int (promedio)
print ("El promedio de paquetes de figuritas a comprar es:", resultado)
