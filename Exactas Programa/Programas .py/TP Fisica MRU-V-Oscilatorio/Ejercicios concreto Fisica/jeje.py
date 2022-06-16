# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 12:10:59 2018

@author: Kalexa
"""

import matplotlib.pyplot as plt

V1 = []
V2 = []

TIEMPO_INICIAL = 0                                 # REPOSO.
TIEMPO_FIN = 15                                    # TIEMPO FINAL DEL OBJETO.

PASO_GRAF = 0.01
PASO_TABLA = 1

TIEMPO_TABLA = TIEMPO_INICIAL

K = 5
X0 = 0
Xfinal = 1                                            # POSICION INICIAL. 
VEL = 5                                           # VELOCIDAD CONSTANTE DEL OBJETO.




    
def Acel (X, V, Tf) :
    TIEMPO_GRAF = TIEMPO_INICIAL
    while TIEMPO_GRAF <= Tf :
    
        V1.append ( TIEMPO_GRAF )
        
        F = (Xfinal * (-K))
        
        V2.append (F)
        #print ("Posición Final:", Xf)
        TIEMPO_GRAF = TIEMPO_GRAF + PASO_GRAF
    return (F)
 
Posición_Final = Acel (Xfinal, VEL, TIEMPO_FIN)
print ("Posición Final:", Posición_Final)
ACELERACIÓN = (VEL/TIEMPO_FIN)
print ("Acelelación:" , ACELERACIÓN)
    
plt. plot (V1 , V2, color = 'r' )
plt.legend (["v2"])
plt.title ("1- MRU (Vehiculo)")
plt. show ()
print ("")
