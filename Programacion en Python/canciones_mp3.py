
def planifica(canciones,cds,tam):
    posibles = todas(canciones)
    posibles = caben(posibles, tam)
    #grabamos los cds
    auxtam=tam*cds
    mejor = obtenmejor(posibles)
    listade=[]
    while(auxtam-sum(posibles[mejor])>=0 and len(posibles)!=0):
        auxtam-=sum(posibles[mejor])
        listade.append(posibles[mejor])
        posibles = eliminapistas(posibles[mejor], posibles)
        mejor = obtenmejor(posibles)
    return listade

def eliminapistas(selec, posible):
    pos=[]
    for i in posible:
        esta=0
        for cancion in selec:
            if cancion in i:
                esta+=1
        if esta==0:
            pos.append(i)
    return pos

#print(eliminapistas([10,15], [[], [10], [15], [20], [8], [10, 15], [10, 8], [15, 8]]))

def todas(canciones):
    posibles=[]
    for i in range(len(canciones)):
        posibles+=combinations(i,canciones)
    return posibles

def combinations(N, iterable):
    if not N:
        return [[]]
    if not iterable:
        return []

    head = [iterable[0]]
    tail = iterable[1:]
    new_comb = [ head + list_ for list_ in combinations(N - 1, tail) ]

    return new_comb + combinations(N, tail)

#obtiene el mejor **** hay que corregirla para que escoja la que sume mas y mas larga sea
def obtenmejor(soluciones):
    maximo=0
    indice=0
    for i in range(len(soluciones)):
        if maximo < sum(soluciones[i]):
            maximo = sum(soluciones[i])
            indice= i
    return indice

#deja solamente las soluciones que caebn segun la capacidad
def caben(todas,capacidad):
    sol=[]
    for i in range(len(todas)):
        suma = sum(todas[i])
        if  suma <= capacidad and todas[i] not in sol:
            sol.append(todas[i])
    return sol

print(planifica([10,15,20,8],2,25))
