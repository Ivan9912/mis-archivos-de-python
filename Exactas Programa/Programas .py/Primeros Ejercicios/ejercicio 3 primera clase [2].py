nombre = "cancion"
milista =list (nombre)
def Palabra (a):
    i=0
    while i< len(a):
        if a[i]== 'a':
             milista [i] ='-'
             print (milista [i])
        elif a[i]== 'e':
            milista [i] ='-'
            print (milista [i])
        elif a[i]== 'i':
           milista [i] ='-'
           print (milista [i])
        elif a[i]== 'o':
            milista [i] ='-'
            print (milista [i])
        elif a[i]== 'u':
            milista [i] ='-'
            print (milista [i])
        else:
            milista [i] = a[i]
            print (milista [i])
        i=i+1
    return a
milista2= Palabra(milista)