def mezcla(A, B):
    dicc = {}
    keysA = A.keys()
    keysB = B.keys()
    for i in keysA:
        dicc[i] = [A[i]]
    for keyB,valeB in B.items():
        if keyB in dicc.keys():
            dicc[keyB].append(valeB)
        else:
            dicc[keyB]=[valeB]
    for clave,valor in dicc.items():
        if len(valor)>1:
            dicc[clave]=tuple(valor)
        elif len(valor)==1:
            dicc[clave]=valor[0]
    return dicc


#print(mezcla({'a': 1}, {'b': 2}), {'a': 1, 'b': 2})
print(mezcla({'a':1,'e':2}, {'a':1,'b':2}), {'a':(1,1),'b':2,'e':2})
#print(mezcla({}, {}), {})
#print(mezcla({1:2,2:3,3:4}, {1:1,2:2,3:3}), {1:(2,1),2:(3,2),3:(4,3)})

