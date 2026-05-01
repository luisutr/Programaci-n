def mezcla(A,B):
    clavea = list(A.keys())
    claveb = list(B.keys())
    clave = clavea + claveb
    mezcla= {}
    for i in clave:
        if i not in list(mezcla.keys()):
            if i in list(A.keys()):
                mezcla[i]=A[i]
            else:
                mezcla[i]=B[i]
        else:
            if i in list(A.keys()):
                mezcla[i]=(mezcla[i], B[i])
            else:
                mezcla[i]=(mezcla[i], A[i])
    return (mezcla)


print(mezcla({'a':1}, {'b':2}), {'a':1,'b':2})
print(mezcla({'a':1,'e':2}, {'a':1,'b':2}), {'a':(1,1),'b':2,'e':2})
print(mezcla({}, {}), {})
print(mezcla({1:2,2:3,3:4}, {1:1,2:2,3:3}), {1:(2,1),2:(3,2),3:(4,3)})