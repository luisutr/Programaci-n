def num_tarros(L,R):
    R=25
    maximo=0
    posibles=todascompesos(L)
    caben=cabentarro(posibles,R)
    usados=[]
    while len(L)>0:
        m=pillamejor(caben)
        mejor=caben[m]
        esta=0
        for j in mejor:
            if (j in usados and j not in L) or (mejor.count(j)>L.count(j)):
                esta+=1
        if esta ==0:
            maximo+=1
            caben.pop(m)
            for i in mejor:
                usados.append(L.pop(L.index(i)))
        else:
            caben.pop(m)
    return maximo

def pillamejor(caben):
    maximo=0
    posicion=0
    for i in range(len(caben)):
        if maximo<sum(caben[i]):
            maximo=sum(caben[i])
            posicion=i
    return posicion

def combinations(N,L):
    if not N:
        return [[]]
    if not L:
        return []
    head = [L[0]]
    tail = L[1:]
    new_comb = [ head + list_ for list_ in combinations(N - 1, tail) ]
    return new_comb + combinations(N, tail)


def todascompesos(L):
    posibles=[]
    for i in range(len(L)):
        for i in combinations(i,L):
            posibles.append(i)
    return posibles

def cabentarro(posibles,R):
    solucion=[]
    suma=0
    for i in range(len(posibles)):
        if posibles[i] != []:
            p = posibles[i]
            suma = sum(posibles[i])
            if suma <=R:
                solucion.append(posibles[i])
    return solucion

print(num_tarros([10,15,20,8], 25))
print(num_tarros([1, 3, 10, 15, 4, 10], 25))
print(num_tarros([10, 24, 16, 19], 25))
