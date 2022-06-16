
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:48:41 2018

@author: Iván A. Maidana
"""

import matplotlib . pyplot as plt



JE = []
Xinicial = 0                           
Xfinal = 10                                   
PASO_GRAF = 1   
PASO_TABLA = 1                                         

TIEMPO_GRAF = Xinicial
TIEMPO_TABLA = Xinicial

M = -20
B = 0

Segundero = []

while TIEMPO_GRAF <= Xfinal :
    Segundero.append ( TIEMPO_GRAF )
    Y = (M * TIEMPO_GRAF) + B
    Ye = int (Y)
    JE.append (Ye)
    TIEMPO_GRAF = TIEMPO_GRAF + PASO_GRAF  


plt. plot (Segundero , JE, color = 'r' )
plt.legend (["F (x) = mx + b"])
plt.title ("Función Lineal")
plt. show ()
print ("")
print ("","","","","","","","","","","","","","","F(x) =", M,"x + ",B)
print ("")
Segundero2 = []
Jo = []
while TIEMPO_TABLA <= Xfinal :
    Segundero2.append ( TIEMPO_TABLA )
    J = (M * TIEMPO_TABLA) + B
    Yi = int (J)
    Jo.append (Yi)
    print ("","","","","","","","","","","","X = ",TIEMPO_TABLA,"","","","","","","","","Y = ", J)
    TIEMPO_TABLA = TIEMPO_TABLA + PASO_TABLA 
