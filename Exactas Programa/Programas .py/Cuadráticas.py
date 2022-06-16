# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:48:41 2018

@author: Iván A. Maidana
"""

import matplotlib . pyplot as plt
#------------------------------------------------------------------------------
JE = []
Xinicial = -10                           
Xfinal = 10                                   
#------------------------------------------------------------------------------                                       
TIEMPO_GRAF = Xinicial
TIEMPO_TABLA = Xinicial

GMF = 2  # GRADO MAYOR DE LA FUNCIóN.
#------------------------------------------------------------------------------

A = 6

B = 2

C = -3

#------------------------------------------------------------------------------
PASO_GRAF = 0.01   
PASO_TABLA = 1

Segundero = []
regis = []
Raiz = ((B**2)-(4*A*C))

if A and Raiz >0 :
    Raiz_0 = (Raiz**0.5)
   #print (Raiz_0)
    Raiz_1 = ((-(B))+ Raiz_0)/(2* A)
    regis.append (Raiz_1)
    #---------------------------------
    Raiz_2 = ((-(B))- Raiz_0)/(2* A)
    regis.append (Raiz_2)
#------------------------------------------------------------------------------
while TIEMPO_GRAF <= Xfinal :
    Segundero.append ( TIEMPO_GRAF )
    Y =  A *(TIEMPO_GRAF ** GMF) + (B * TIEMPO_GRAF )+ C
    Ye = int (Y)
    JE.append (Ye)
    if A and Raiz >0 : 
        TIEMPO_GRAF = TIEMPO_GRAF + PASO_GRAF  
    else:
        TIEMPO_GRAF = TIEMPO_GRAF + 1
#------------------------------------------------------------------------------
plt. plot (Segundero , JE, color = 'r' )
plt.legend (["F (x) = ax^2 +bx + c"])
plt.title ("Función Cuadrática")
plt. show ()
#------------------------------------------------------------------------------
print ("")
print ("","","","","","","","","","","","F(x) =","(",A,".X )^",GMF,"+ (",B,".X)","+",C)
print ("")
if A == 0:
    if B == 0:
        if C == 0:
            print ("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
            print ("lll LA FUNCIÓN NO EXISTE WEY! - Ó ES UNA CONSTANTE CON VALOR CERO lll")
            print ("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
            print ("")
#------------------------------------------------------------------------------
if Raiz <0:
    print ("","","","Raices NO EXISTE! (porque da negativo):", Raiz)  
    print ("")
    #--------------------------------------------------------------------------
if A and Raiz  >0 :
    print ("","","","Completo:",regis)
    print ("")
    print ("","","","X1 =", int (Raiz_1))
    print ("")
    print ("","","","X2 =", int (Raiz_2))
    print ("")
    #--------------------------------------------------------------------------
if A and B >0:
    regis_vertice = []
    Xv = (-B) / (2*A)
    Yv = A *(Xv ** GMF) + (B * Xv )+ C
    print ("","","","VÉRTICE =","(",Xv,";",Yv,")",)
    print ("")
    #--------------------------------------------------------------------------
if A >=0: 
    ORD_O = A *(0 ** GMF) + (B * 0 )+ C
    XRaiz = ((-C)/B)
    print ("","","","Ord. al Origen =",ORD_O)
    print ("")
    if A <=0:
        print ("","","","Raiz =","","","","","","","","","", XRaiz)
        print ("")
        #----------------------------------------------------------------------
#------------------------------------------------------------------------------
Segundero2 = []
Jo = []
#------------------------------------------------------------------------------
print ( "","","","","","","","","","En X" ,"","","","","","","En Y")
print ("")
#------------------------------------------------------------------------------
while TIEMPO_TABLA <= Xfinal :
    Segundero2.append ( TIEMPO_TABLA )
    J = A *(TIEMPO_TABLA ** GMF) + (B * TIEMPO_TABLA )+ C
    Yi = int (J)
    Jo.append (Yi)
    print ("","","","","","","","","","","","",TIEMPO_TABLA,"","","","","","","","", J)
    TIEMPO_TABLA = TIEMPO_TABLA + PASO_TABLA 
#------------------------------------------------------------------------------




