# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

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
