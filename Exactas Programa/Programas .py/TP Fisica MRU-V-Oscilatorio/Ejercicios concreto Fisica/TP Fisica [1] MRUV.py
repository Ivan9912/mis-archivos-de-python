# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:48:41 2018

@author: Iván A. Maidana
"""

import matplotlib . pyplot as plt




TIEMPO_INICIAL = 0                  ###            # REPOSO.
TIEMPO_FIN = 15                     ###            # TIEMPO FINAL DEL OBJETO.

PASO_GRAF = 1                                   # DATOS PARA HACER EL GRAFICO.
PASO_TABLA = 1                                     # DATOS PARA HACER LA TABLA.

TIEMPO_GRAF = TIEMPO_INICIAL
TIEMPO_TABLA = TIEMPO_INICIAL

MASA = 1                            #              # MASA CONSTANTE.
FUERZA = 2                          #              # FUERZA CONSTANTE.

VEL = 5                             #              # VELOCIDAD CONSTANTE DEL OBJETO.
X0 = 30                             ###            # POSICION INICIAL. 
X1 = []                             #              # POSICION FINAL. 
VEL_0 = 0
VEL_1 = int( VEL+ (FUERZA / MASA) * TIEMPO_GRAF)     ###

ACEL = int (FUERZA / MASA)                         # SI DA 0 DE FUERZA SE CREA MRU. (F=ma. Newton)
# OPCIONAL ACEL = ((VEL_1-VEL_0)/(TIEMPO_FIN-TIEMPO_INICIAL))
Segundero = []


while TIEMPO_GRAF <= TIEMPO_FIN :
    Segundero.append ( TIEMPO_GRAF )
    VEL_1 = VEL * TIEMPO_GRAF
    ACEL_2 = (ACEL * (TIEMPO_GRAF**2) / 2)
    X_FIN = X0 + VEL_1 + ACEL_2
    X1.append (int (X_FIN))
    TIEMPO_GRAF = TIEMPO_GRAF + PASO_GRAF    

plt. plot (Segundero , X1, color = 'r' )
plt.legend (["MRU-V dundión: x(t)"])
plt.title ("2- MRU-V (Vehiculo)")
plt. show ()
print ("")

print ("","","","",""," Movimiento Rectilineo Uniforme es una función Lineal.")
print ("","","","",""," Movimiento Rectilineo Uniforme Variado es una función") 
print ("","","","","","","Cuadrática.")
print ("")
print ("","Tiempo(Seg)","","Dist(Mts)","","Veloc(Mts/Seg)","", "Acel(mts/seg**2)")
print ("")
while TIEMPO_TABLA <= TIEMPO_FIN:
    Velocidad_Seg = int (VEL * TIEMPO_TABLA)
    ACEL_3 = (ACEL * (TIEMPO_TABLA**2) / 2)
    DIST =  int (X0 + Velocidad_Seg +  ACEL_3)
    TIEMPO_TABLA = TIEMPO_TABLA + PASO_TABLA
    print ("","","","","",TIEMPO_TABLA-PASO_TABLA,"","","","","","","","", DIST,"","","","","","","","","","","","", Velocidad_Seg,"","","","","","","","","","","","","","","","",ACEL) 
print ("")




