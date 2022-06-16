Palabra = "cancion"  #Palabra que se la puede variar.
milista =list (Palabra)  #La palabra para cambiar caracteres se la separa.
def Palabra2 (a):  #Definimos una funcion.
    i=0
    while i< len(a):  #Registrara la palabra en toda su extencion si quedarse fuera de rango.
        if a[i]== 'a':   #If para condicionar.
             milista [i] ='-'
        elif a[i]== 'e':
            milista [i] ='-'
        elif a[i]== 'i':
           milista [i] ='-'
        elif a[i]== 'o':
            milista [i] ='-'
        elif a[i]== 'u':
            milista [i] ='-'
        else:            #Un else para que iguale la letra en caso de no ser una vocal.
            milista [i] = a[i]
        i=i+1            #Una vez que termina este bucle, se le suma 1 a la i.
    return a             #Va a sustituir "a" por "milista" una vez terminado los cambios de while.
milista2= Palabra2(milista) #Igualamos a= milista. y toda esta funcion sera etiquetado por milista2.
milista3= "" #Esto es para crear una variable para que me sirva en el join.
uala = milista3.join (milista2) #Uala sera la palabla cambiada y ya unida los caracteres.
print ("Palabra sin Vocales:", uala)