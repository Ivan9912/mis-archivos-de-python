# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 22:45:06 2018

@author: Ivan A. Maidana
"""
import matplotlib.pyplot as plt
import math

V1 = []
V2 = []

TIEMPO_INICIAL = 0   
TIEMPO_FINAL = 16                             
PASO_GRAF = 1
TIEMPO_GRAF = TIEMPO_INICIAL

K = 5
MASA = 1
X0 = 0
X1 = 0.7
X2 = 1
X3 = 1.5

V0 = 0

pi_0 = math.pi
Holisss = math.sin (150)
print ("jojis:", holisss
#ACEL = int (FUERZA / MASA)                         # SI DA 0 DE FUERZA SE CREA MRU. (F=ma. Newton)

      
T = (6.283185 * ((MASA / K)** 0.5))
A = X1* ((-( 6.283185 / T)) **2)
#print (A)
F = MASA * A 
#print (F)
Vf = (int (V0 + (A * TIEMPO_FINAL)))
#print ("velo final:", Vf)
Xc = (MASA * A)/ -K
#print ("JEEJ:", Xc)

def Acel (X, V, Tf) :
    TIEMPO_GRAF = TIEMPO_INICIAL

    for i in range (Tf):
        V1.append (Tf)
        #A = (int(X0 + (V * TIEMPO_GRAF)))
        #B = (int(-K * X1))
        #VEL_1 = V * TIEMPO_GRAF
        ACEL_2 = (A * (Tf**2) / 2)
        X_FIN = X0 + Vf + ACEL_2
        #X_FIN_2 = 
        print ("Acele", X_FIN)
        V2.append (X_FIN)
        
        TIEMPO_GRAF += PASO_GRAF
        
    return X_FIN
Aceleración = Acel (X1, Vf, TIEMPO_FINAL)
print ("Acel:", Aceleración)

plt. plot (V1 , V2, color = 'r' )
plt.legend (["v2"])
plt.title ("3- Movimiento Oscilatorio (Vehiculo)")
plt. show ()
print ("")