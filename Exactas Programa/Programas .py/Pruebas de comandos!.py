# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:11:31 2018

@author: Kalexa
"""
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
print ("")

 
