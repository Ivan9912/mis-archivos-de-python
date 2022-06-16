# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:48:41 2018

@author: Kalexa
"""

import matplotlib . pyplot as plt

V1 = []
V2 = []

TIEMPO_INICIAL = 0              # REPOSO.
TIEMPO_FIN = 60                 # TIEMPO FINAL DEL OBJETO.

TIEMPO_GRAF = TIEMPO_INICIAL
TIEMPO_TABLA = TIEMPO_INICIAL
NUM_DIV_V2_POSICION_LIST = 20   # Dividiendo este número a V2 obtendrémos la cantidad exacta de posiciones reales en V1.

X0 = 60                         # POSICION INICIAL. 
VEL = 80                        # VELOCIDAD CONSTANTE DEL OBJETO.

PASO_GRAF = 0.01
PASO_TABLA = 1

while TIEMPO_GRAF <= TIEMPO_FIN :
    V1.append ( TIEMPO_GRAF )
    VEL_0 = VEL * TIEMPO_GRAF        
    V2.append (int ( X0 + VEL_0 ))
    TIEMPO_GRAF = TIEMPO_GRAF + PASO_GRAF  

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

CANT_LIST_V2 = int ((len (V2)/NUM_DIV_V2_POSICION_LIST))
print ("")
print ("","","","","","","","","","","","","", CANT_LIST_V2,"Posiciones en la lista")
print ("")



