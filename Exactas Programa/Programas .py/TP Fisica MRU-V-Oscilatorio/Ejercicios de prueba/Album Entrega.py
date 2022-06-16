# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:06:58 2018
Exactas Programa
@author: Ivan A. Alejandro
"""

import random
import numpy as np
#------------------------------------------------------------------------------
CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM = 669
CANTIDAD_DE_FIGUS_PARA_1_PAQUETE = 10
VECES_QUE_SE_COMPLETARON_LOS_ALBUNES = 1000
CANT_D_PAQ_Q_VOY_A_KERER = 5                        #Cantidad de figus que voy a querer generar.
PAQUETE_DE_FIGUS = []                               #vacio, a llenar previamente
REGISTRO_DE_LAS_REPETICIONES = []
ALBUM_A_LLENAR_OTRAVEZ = [0]*CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM
ALBUM_LLENO = np.arange (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM+ 1)
#------------------------------------------------------------------------------
#-------------------ACÁ ARRANCA EL PROGRAMA 'A'--------------------------------

for repetir in range (VECES_QUE_SE_COMPLETARON_LOS_ALBUNES):
    def JUGADA (ALBUM):
        COUNT = 0
        while all (ALBUM) != all (ALBUM_LLENO):
            DADO = random.randint (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
            COUNT = COUNT + 1
            if ALBUM [DADO -1] == 0:
                ALBUM [DADO -1] = DADO
        return COUNT
    ALBUM_POR_LLENAR = [0] * CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM
    ALBUM = JUGADA (ALBUM_POR_LLENAR)
    REGISTRO_DE_LAS_REPETICIONES.append (ALBUM)
#------------------------------------------------------------------------------    
print ("--------------------------------------------------------------------------------------------------------------")
print ("","","","","","","","","","","Este es el ejercicio original a completar, lo llamaré A.")
print ("")
#print ("A- Esta es la lista de la cantidad de figuritas que cada uno necesito")   ---OPCIONAL---
#print ("","","","para compltarla:") 
#print ("","","",REGISTRO_DE_LAS_REPETICIONES)
print ("-----------------------------------------------------------------------")    
print ("B- Esta es la cantidad de figuritas para completar el album:","","","","","", CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
print ("-----------------------------------------------------------------------")    
print ("C- Esta es la cantidad de las personas que completaron su album:","", VECES_QUE_SE_COMPLETARON_LOS_ALBUNES)
print ("-----------------------------------------------------------------------")
#------------------------------------------------------------------------------
PROMEDIO = np.mean (REGISTRO_DE_LAS_REPETICIONES, dtype = int)
print ("D- Este es el promedio del punto C- :","","","","","","","","","","","","","","","","","","","","","","","","","","","","", PROMEDIO+1)
print("-----------------------------------------------------------------------")
#------------------------------------------------------------------------------
def CANTIDAD (promedio_obtenido, CANTIDAD_QUE_TIENE_UN_PAQUETE):
    PAQUETES_A_COMPRAR = promedio_obtenido / CANTIDAD_QUE_TIENE_UN_PAQUETE
    return PAQUETES_A_COMPRAR
PAQUETES_1 = CANTIDAD (PROMEDIO, CANTIDAD_DE_FIGUS_PARA_1_PAQUETE)
PAQUETES_2 = int (PAQUETES_1)
print ("E- Cantidad que se deben de comprar de paquetes")
print ("","","","de figuritas, para completar 1 album:","","","","","","","","","","","","","","","","","","","","","","","","","", PAQUETES_2+1)
print ("-----------------------------------------------------------------------")
def COSTO (PAQUETES_A_COMPRAR, PRECIO_UNIDAD_PAQUETES):
    PESOS_ARG = PAQUETES_A_COMPRAR * PRECIO_UNIDAD_PAQUETES
    return PESOS_ARG
COSTO_1 = COSTO (PAQUETES_2, 14)
COSTO_2 = int (COSTO_1)
print ("F- Cantidad de dinero a gastar para completa el album:","","","","","","","","","","$", COSTO_2+1)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
print ("--------------------------------------------------------------------------------------------------------------")
print ("","","","","","","","","","","Este programa crea un paquete de 5 figuritas, lee cada una de ellas, y las posiciona en el") 
print ("","","","","","","","","","","","album.lo llamaré B.")
print ("")
for uno in range (CANTIDAD_DE_FIGUS_PARA_1_PAQUETE):
    DADO = random.randint (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
    PAQUETE_DE_FIGUS.append (DADO)
    
print (uno+1,"figus",":", PAQUETE_DE_FIGUS)
print ("")

PAQUETE_DE_FIGUS_VISUALIZAR = PAQUETE_DE_FIGUS
k = 0
while k <= (CANTIDAD_DE_FIGUS_PARA_1_PAQUETE -1) :
    k = k+1
    FIGUS_IND = PAQUETE_DE_FIGUS_VISUALIZAR[k-1]
    print ("Figu Núm.",k,"",":",FIGUS_IND)
    if ALBUM_A_LLENAR_OTRAVEZ [FIGUS_IND-1] == 0:
        ALBUM_A_LLENAR_OTRAVEZ [FIGUS_IND -1] = FIGUS_IND

print ("")
print ("Album con figus 'pegadas':")
print (ALBUM_A_LLENAR_OTRAVEZ)
print ("")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
print ("--------------------------------------------------------------------------------------------------------------")
print ("","","","","","","","","","","Este programa crea 'n' veces paquetes que sea requerido de 'm' cantidad de figuritas. Lo llamaré C.")
print ("")

def GENERADOR_DE_PAQUETES (CANTIDAD_DE_PAQUETES_A_GENERAR):
    M = 0
    elrepe = int (CANTIDAD_DE_PAQUETES_A_GENERAR +1 /2)       #Esto se me ocurrio de tanto intentar y ver reiterativamente los resultados.
    while M <= CANTIDAD_DE_PAQUETES_A_GENERAR:
        for keseyo in range (elrepe):
            PAQUETE_DE_FIGUS = []
            for keseyo_2 in range (CANTIDAD_DE_FIGUS_PARA_1_PAQUETE):
                dado = random.randint (1, CANTIDAD_DE_FIGUS_PARA_COMPLETAR_ALBUM)
                PAQUETE_DE_FIGUS.append (dado)
                M = M + 1
            print ("Paquete", keseyo+1,":" ,PAQUETE_DE_FIGUS)  #Se me ocurrió añadir esto para que quede mas cool.
            print ("")
    return elrepe

CANT_FIGUS = GENERADOR_DE_PAQUETES (CANT_D_PAQ_Q_VOY_A_KERER) 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
print ("--------------------------------------------------------------------------------------------------------------")

"""
 Me gustó bastante hacer este ejercicio, solo que por temas de tiempo no creo poder "ensambrar" estas 3 partes (A, B y c)
para poder completar con lo opcional del ejercicio dado de Album. 
 Muchos 'prints' para que el Out quede más prolijo, nada más.
"""