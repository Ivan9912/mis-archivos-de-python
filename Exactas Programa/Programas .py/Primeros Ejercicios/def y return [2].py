ivan = []
kakita = []
soretin = []
gordapapa = []
ivan.append(9)
kakita.append(2)
soretin.append(7)
gordapapa.append(6)
ivan.append(2)
kakita.append(1)
soretin.append(8)
gordapapa.append(11)
def suma_jugadas (l):
    suma = 0
    for i in range (len(l)):
        suma = suma +l[i]
    return suma
SUMA_IVAN = suma_jugadas (ivan)
SUMA_KAKITA = suma_jugadas (kakita)
SUMA_SORETIN = suma_jugadas (soretin)
SUMA_GORDAPAPA = suma_jugadas (gordapapa)
print ("Ivancito tiene: ", SUMA_IVAN)
print ("La kakita tiene:", SUMA_KAKITA)
print ("El soretin tiene:", SUMA_SORETIN)
print ("La papa tiene:", SUMA_GORDAPAPA)