# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:03:05 2018

@author: Kalexa
"""
import numpy as np
album_1 = []
album_2 = []
album_3 = []
album_4 = []
album_5 = []
album_6 = []
album_7 = []
album_8 = []
album_9 = []
album_10 = []
album_11 = []
jojo = []
#-----------------------------------------
album_1.append(11)
album_2.append(15)
album_3.append(17)
album_4.append(18)
album_5.append(15)
album_6.append(14)
album_7.append(11)
album_8.append(20)
album_9.append(17)
album_10.append(19)
album_11.append(25)
#------------------------------------------
jojo.append(album_1)
jojo.append(album_2)
jojo.append(album_3)
jojo.append(album_4)
jojo.append(album_5)
jojo.append(album_6)
jojo.append(album_7)
jojo.append(album_8)
jojo.append(album_9)
jojo.append(album_10)
jojo.append (album_11)


jojo = np.empty (10)
print (jojo)
promedio = np.mean(jojo)
print ("Este es el promedio total:", promedio)