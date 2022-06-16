# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 21:19:52 2018

@author: Kalexa
"""
#------------------------------------------------------------------------------
import random
import numpy as np
FIGURITAS_PARA_COMPLETAR_EL_ALBUM = 30
ALBUM_LLENO = np.arange (1, FIGURITAS_PARA_COMPLETAR_EL_ALBUM + 1)
VECES_QUE_SE_COMPLETARON_LOS_ALBUNES = 10
REGISTRO_DE_LAS_REPETICIONES = []
#------------------------------------------------------------------------------
for repetir in range (VECES_QUE_SE_COMPLETARON_LOS_ALBUNES):
    def JUGADA (ALBUM):
        COUNT = 0
        while all (ALBUM) != all (ALBUM_LLENO):
            DADO = random.randint (1, FIGURITAS_PARA_COMPLETAR_EL_ALBUM)
            COUNT = COUNT + 1
            if ALBUM [DADO -1] == 0:
                ALBUM [DADO -1] = DADO
        return COUNT
    ALBUM_POR_LLENAR = [0] * FIGURITAS_PARA_COMPLETAR_EL_ALBUM
    ALBUM = JUGADA (ALBUM_POR_LLENAR)
    REGISTRO_DE_LAS_REPETICIONES.append (ALBUM)
    #print ("3- Registro de las repeticiones:", REGISTRO_DE_LAS_REPETICIONES)
#------------------------------------------------------------------------------    
print ("--------------------------------------------------------------------------------------------------------------")
print ("1- Esta es la lista de la cantidad de figuritas que cada uno necesito")
print ("","","","para compltarla:") 
print ("","","",REGISTRO_DE_LAS_REPETICIONES)
print ("-----------------------------------------------------------------------")    
print ("2- Esta es la cantidad de figuritas para completar el album:","","","","","", FIGURITAS_PARA_COMPLETAR_EL_ALBUM)
print ("-----------------------------------------------------------------------")    
print ("3- Esta es la cantidad de las personas que completaron su album:","", VECES_QUE_SE_COMPLETARON_LOS_ALBUNES)
print ("-----------------------------------------------------------------------")
#------------------------------------------------------------------------------
PROMEDIO = np.mean (REGISTRO_DE_LAS_REPETICIONES, dtype = int)
print ("4- Este es el promedio del punto 3 :","","","","","","","","","","","","","","","","","","","","","","","","","","","","", PROMEDIO+1)
print("-----------------------------------------------------------------------")
#------------------------------------------------------------------------------
def CANTIDAD (promedio_obtenido, CANTIDAD_QUE_TIENE_UN_PAQUETE):
    PAQUETES_A_COMPRAR = promedio_obtenido / CANTIDAD_QUE_TIENE_UN_PAQUETE
    return PAQUETES_A_COMPRAR
PAQUETES_1 = CANTIDAD (PROMEDIO, 5)
PAQUETES_2 = int (PAQUETES_1)
print ("5- Cantidad que se deben de comprar de paquetes")
print ("","","","de figuritas, para completar 1 album:","","","","","","","","","","","","","","","","","","","","","","","","","", PAQUETES_2+1)
print ("-----------------------------------------------------------------------")
def COSTO (PAQUETES_A_COMPRAR, PRECIO_UNIDAD_PAQUETES):
    PESOS_ARG = PAQUETES_A_COMPRAR * PRECIO_UNIDAD_PAQUETES
    return PESOS_ARG
COSTO_1 = COSTO (PAQUETES_2, 14)
COSTO_2 = int (COSTO_1)
print ("6- Cantidad de dinero a gastar para completa el album:","","","","","","","","","","$", COSTO_2+1)
print ("--------------------------------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------
