# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:18:39 2018

@author: Kalexa
"""

import random
import numpy as np
def jugada (x):
    count=0
    album_lleno = list (range (1, posiciones +1))
    while all(x) != all (album_lleno):
        paquete = [0]*5
        dado = random.randint(1, posiciones)

        #while all (paquete) ==0:
        paquete.append(random.randint (1, posiciones))
        paquete.append(random.randint (1, posiciones))
        paquete.append(random.randint (1, posiciones))
        paquete.append(random.randint (1, posiciones))
        paquete.append(random.randint (1, posiciones))
        print (paquete)
        count = count +1
        if x[dado -1]==0:
            x [dado -1]=0
    return count

repeticiones = []
posiciones =669
album = [0]*posiciones
x= jugada(album)
rep=10
for i in range (rep):
     repeticiones.append(x)
promedio =np.mean(repeticiones)