# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 20:49:41 2018

@author: Kalexa
"""

import random

CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM = 30
CANTIDAD_DE_FIGUS_PARA_1_PAQUETE = 5
hola_2 = []
CANTIDAD_DE_FIGUS_COMPRADAS = 5
count = 0
for g in range (CANTIDAD_DE_FIGUS_COMPRADAS):
    PAQUETE_DE_FIGUS = []
    hola_2.append (PAQUETE_DE_FIGUS)
    for i in range (CANTIDAD_DE_FIGUS_PARA_1_PAQUETE):
        dado = random.randint (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
        PAQUETE_DE_FIGUS.append (dado)
        #print ("dado:", dado)
        #print ("")
    count = count + 1
hola = PAQUETE_DE_FIGUS
#print ("lista :", hola)
#print ("")
print ("lista :", hola_2)
print ("")     
print ("paquetes que se compraron:", count)
print ("")     











"""
def palabra (h):
    k=0
    while k < len (h):
         
for v in range (5):
    k = 1
    while k <= 5:
        print (k)
        k =k+1
"""