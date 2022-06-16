ivan = []
kakita = []
soretin = []
gordapapa = []
elpeke = []
ivan.append(9)
kakita.append (8)
soretin.append(10)
gordapapa.append(6)
ivan.append(2)
kakita.append (5)
soretin.append(-10)
gordapapa.append(11)
def suma_jugadas (etiqueta):
    suma = 0
    i = 0
    while i<len(etiqueta):
        suma = suma + etiqueta[i]
        i = i+1
    return suma
if ivan != []:
    SUMA_IVAN = suma_jugadas (ivan)
else:
    SUMA_IVAN = -1
if kakita != []:
    SUMA_KAKITA = suma_jugadas (kakita)
else:
    SUMA_KAKITA = -1
if soretin != []:
    SUMA_SORETIN = suma_jugadas (soretin)
else:
    SUMA_SORETIN = -1
if gordapapa != []:
    SUMA_GORDAPAPA = suma_jugadas (gordapapa)
else:
    SUMA_GORDAPAPA = -1
if elpeke != []:
    SUMA_ELPEKE = suma_jugadas (elpeke)
else:
    SUMA_ELPEKE = -1
print ("Ivancito tiene: ", SUMA_IVAN)
print ("La kakita tiene:", SUMA_KAKITA)
print ("El soretin tiene:", SUMA_SORETIN)
print ("La papa tiene:", SUMA_GORDAPAPA)
print ("El pequeñin tiene:", SUMA_ELPEKE)