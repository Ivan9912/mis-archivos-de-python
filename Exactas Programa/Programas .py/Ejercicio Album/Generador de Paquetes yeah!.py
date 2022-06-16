# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 22:44:34 2018

@author: Ivan A. Maidana
"""

import random

CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM = 30
CANTIDAD_DE_FIGUS_PARA_1_PAQUETE = 5
CANT_D_PAQ_Q_VOY_A_KERER = 5              #Cantidad de figus que voy a querer generar.

def GENERADOR_DE_PAQUETES (CANTIDAD_DE_PAQUETES_A_GENERAR):
    M = 0
    elrepe = int (CANTIDAD_DE_PAQUETES_A_GENERAR +1 /2) #Esto se me ocurrio de tanto intentar y ver reiterativamente los resultados.
    while M <= CANTIDAD_DE_PAQUETES_A_GENERAR:
        for keseyo in range (elrepe):
            PAQUETE_DE_FIGUS = []
            for keseyo_2 in range (CANTIDAD_DE_FIGUS_PARA_1_PAQUETE):
                dado = random.randint (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
                PAQUETE_DE_FIGUS.append (dado)
                #print ("dado:", dado)
                #print ("")
                M = M + 1
            print ("Paquete", keseyo+1,":" ,PAQUETE_DE_FIGUS) # se me ocurrió añadir esto para que quede mas cool.
            print ("")
    return elrepe

CANT_FIGUS = GENERADOR_DE_PAQUETES (CANT_D_PAQ_Q_VOY_A_KERER) 



"""
k = 1
while k <= 14:
    print (k)
    k =k+1
"""
