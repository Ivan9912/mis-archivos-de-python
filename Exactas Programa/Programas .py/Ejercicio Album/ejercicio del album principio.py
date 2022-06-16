# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:11:05 2018

@author: Kalexa
"""

import random
import numpy as np
def jugada (x):
    count =0
    album_lleno = [1,2,3,4,5,6]
    while all (x) != all (album_lleno):
        dado = random.randint(1,6)
        count = count +1
        if x[dado -1]==0:
            x [dado -1]=dado
    return count
album = [0,0,0,0,0,0]
x= jugada (album)
repeticiones = []
rep = 1000
for i in range (rep):
    repeticiones.append (x)
promedio = np.mean(repeticiones)
resultado = int (promedio)
print ("El promedio de paquetes de figuritas a comprar es:", resultado)