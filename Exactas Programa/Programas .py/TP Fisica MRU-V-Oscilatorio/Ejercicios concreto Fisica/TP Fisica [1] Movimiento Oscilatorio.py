# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:48:41 2018

@author: Iván A. Maidana
"""

import matplotlib . pyplot as plt

V1 = []
V2 = []
V = []
T = []
X = []

TIEMPO_INICIAL = 0                                 # REPOSO.
TIEMPO_FIN = 15                                    # TIEMPO FINAL DEL OBJETO.

PASO_GRAF = 0.01
PASO_TABLA = 1

TIEMPO_GRAF = TIEMPO_INICIAL
TIEMPO_TABLA = TIEMPO_INICIAL

X0 = 30                                            # POSICION INICIAL. 
VEL = 5                                           # VELOCIDAD CONSTANTE DEL OBJETO.
K = 5

while TIEMPO_GRAF <= TIEMPO_FIN :
    V1.append ( TIEMPO_GRAF )
    VEL_0 = VEL * TIEMPO_GRAF  
    
    def Acel (X, V, T) :
        A = (int ((- K) * VEL_0 ))
        return A
    Aceleración = Acel (1, 0, 0)
    print ("Acel:", Aceleración)
    
    V2.append (int ( X0 + VEL_0 ))
    TIEMPO_GRAF = TIEMPO_GRAF + PASO_GRAF    

"""
def Acel (X, V, T) :
    A = (- K) * V2
    return A

Aceleración = Acel (1, 0, 0)
print ("Acel:", Aceleración)
"""

plt. plot (V1 , V2, color = 'r' )
plt.legend (["v2"])
plt.title ("1- MRU (Vehiculo)")
plt. show ()
print ("")

print ("","","Tiempo(Seg.)""","","","","Distancia(Mts)","","","","Velocidad(Mts/Seg.)")
print ("")
while TIEMPO_TABLA <= TIEMPO_FIN:
    Velocidad_Seg = int (VEL * TIEMPO_TABLA)
    DIST =   X0 + Velocidad_Seg 
    TIEMPO_TABLA = TIEMPO_TABLA + PASO_TABLA
    print ("","","","","","","",TIEMPO_TABLA-PASO_TABLA,"","","","","","","","","","","","","","", DIST,"","","","","","","","","","","","","","","","","","", Velocidad_Seg)   


