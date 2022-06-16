nombre = "cancion"
milista =list (nombre)
def Palabra (a):
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
milista2= Palabra(milista)
print (milista)