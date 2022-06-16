# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 19:29:35 2018

@author: Kalexa
"""

import random
def jugada (posiciones):
    count=0
    i=0
posiciones =100
    for i in range (posiciones):
    album_lleno = list (range(1, posiciones +1))
    while all (album) != all (album_lleno):
        dado = random.randint (1, posiciones)
        count = count +1
        if album [dado -1]==0:
            album [dado -1]=dado
    return count
album = []
album.append (0)

print (jugada (album, 669))
