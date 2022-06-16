"""
Created on Sat Jul 26 20:49:41 2018

@author: Ivan A. Maidana
"""

#------------------------------------------------------------------------------
print ("------------------------------------------------------------------------------------------------------------")
k = 1
while k <= 14:
    print (k)
    k =k+1
print ("------------------------------------------------------------------------------------------------------------")
print ("")
#------------------------------------------------------------------------------
Palabra = "Exactas Porgrama está bastante bueno"  
milista =list (Palabra)  
def Palabra2 (a): 
    i=0
    while i< len(a):  
        if a[i]== 'a':   
             milista [i] ='-'
        elif a[i]== 'e':
            milista [i] ='-'
        elif a[i]== 'i':
           milista [i] ='-'
        elif a[i]== 'o':
            milista [i] ='-'
        elif a[i]== 'u':
            milista [i] ='-'
        else:            
            milista [i] = a[i]
        i=i+1            
    return a             
milista2= Palabra2(milista) 
milista3= "" 
uala = milista3.join (milista2) 
print ("Oración sin Vocales:", uala)
print ("------------------------------------------------------------------------------------------------------------")
print ("")
#------------------------------------------------------------------------------
import random
import numpy as np
a = np.arange(10)
print ("1- Esto hace el np arange:", a)
print ("")
hola_3=len (a)
print ("2- Esto hace el len en a:", hola_3)
print ("")
hola_4=a [1:6]
print ("3- Acá coloca del 0 hasta el 6, sin incluir el número 6 y el 0:", hola_4)
print ("")
hola_5=random.shuffle (a)
print ("4- Esto hace el shuffle:", a)
print ("")
hola = np.mean (a)
print ("5- Acá saca el promedio de los 10:", hola)
print ("")
hola_6= int (hola)
print ("6- acá utilizo el int para hacerlo entero:" ,hola_6)
print ("")
hola_7= float (hola)
print ("7- acá utilizo el int para hacerlo racional:" ,hola_7)
print ("")
hola_2 = random.randint (1,11)
print ("8- Esto hace el Randint:" ,hola_2)
print ("")
numero_2 =(sum(a))
print ("9- Suma de todos los número que componen 'a':", numero_2)
print ("")
jojo = np.empty (15, dtype=int)
print ("10- Lo que hace empty:", jojo)
print ("")
sobre = random.sample (range (6), 1)
print ("11- Esto hace sample:", sobre)
print ("------------------------------------------------------------------------------------------------------------")
print ("")
#------------------------------------------------------------------------------
loste = []
for v in range (10):
    k = 0
    while k <= 5:
        loste.append (k)
        #print (k)
        k =k+1
print ("lista:", loste)
print ("------------------------------------------------------------------------------------------------------------")
print ("")
#------------------------------------------------------------------------------










