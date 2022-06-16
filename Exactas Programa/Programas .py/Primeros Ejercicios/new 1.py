def Palabra (a):
    i=0
    while i< len(a):
        if a[i]== 'a':
            milista[len (milista)-6]='-'
        elif a[i]== 'e':
            milista[len (milista)]='-'
        elif a[i]== 'i':
            milista[len (milista)]='-'
        elif a[i]== 'o':
            milista[len (milista)]='-'
        elif a[i]== 'u':
            milista[len (milista)]='-'
        i=i+1
    return a
a="Cancion"
milista=list (a)
print (Palabra(a))
print (milista)