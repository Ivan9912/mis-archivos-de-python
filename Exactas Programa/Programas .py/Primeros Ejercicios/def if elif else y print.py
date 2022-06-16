def k(a):
    if a==2:
        res=a*a+1
    elif a==3:
        res=a+a-1
    elif a==7:
        res=a*a+5
    elif a==11:
        res=a*(a-2)+9
    else:
        res=a*a-2
    return res
prueba= k(14)
print (prueba)