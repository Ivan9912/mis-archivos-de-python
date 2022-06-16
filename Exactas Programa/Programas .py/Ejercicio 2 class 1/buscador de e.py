# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 20:25:57 2018

@author: Kalexa
"""
#------------------------------------------------------------------------------
def Palabra (a):
    i = 0
    count = 0
    while i< len (a):
        if a[i]== 'e':
            count =count + 1
        i = i + 1
    return count
a = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeasdadsgewegfwegwwgwgwregwegsdgegrfgrg"
print ("-------------------------------------------------------------------------------")
print ("")
print (" "+ " "+ "Palabra sometido al análisis de la cantidad de \'e\':") 
print ("")
print ("")
print (" " + " " + "\"" + a + "\"")
print ("")
print ("")
print (" "+ " "+ " "+ " "+"Hay",Palabra (a), "de la letra 'e' dentro de la palabra escrita.")
print ("")
#------------------------------------------------------------------------------
N = 0
def Palabra (b):
    j = 0
    count = 0
    while j< len (b):
        if b[j]== '0':
            count =count + 1
        j = j + 1
    return count
b = "1232135035035035415043510350351035010"
print ("-------------------------------------------------------------------------------")
print ("")
print (" "+ " " + "Secuencia de números sometido al análisis de número " + "\'" + str(0) + "\'" + ":")
print ("")
print (" "+ " "+ "\"" + b + "\"")
print ("")
print (" "+ " "+" "+" "+"Hay",Palabra (b), "de '0' dentro de los números escritos.")
print ("")
print ("-------------------------------------------------------------------------------")
#------------------------------------------------------------------------------


