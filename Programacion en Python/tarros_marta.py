def permutaciones(ar_list):
    if not ar_list:
        yield []
    else:
        for a in ar_list[0]:
            for prod in permutaciones(ar_list[1:]):
                yield [a,]+prod

def creasublistas(L,n):
    lista=[]
    for i in range(0,len(L)-n+1):
        lista.append(L[i:i+n])
    if len(L)%2!=0 and n%2==0:
        lista.append([L[-1]])
    return lista

def sublistas(L):
    lista=[]
    for i in range(1,len(L)):
        lista.append(creasublistas(L,i))
    lista.append(L)
    return lista

def posibles(L):
    sub=(sublistas(L))
    total=sub[0]
    for i in sub:
        if type(i[0])!=int:
            total+=list(permutaciones(i))
    return sorted(total)

def tarros_necesarios(lp,capacidad):
    todas=posibles(lp)
    soluciones = caben(todas,capacidad)
    listadetarros=[]
    auxcap = capacidad
    while (len(lp)>0 and len(soluciones)>1):
        #cojo el mejor y lo saco de la lista de mejores
        imejor=obtenmejor(soluciones)
        mejor = soluciones[imejor]
        soluciones.pop(imejor)
        #meto los elementos en un tarro, osea, los quito de la lista original
        tarro = []
        for i in mejor:
            if i in lp:
                posicion = lp.index(i)
                cosa = lp.pop(posicion) # lo cojo de la lista de pesos
                tarro.append(cosa)# lo meto en el tarro
        if len(tarro)>0:
            listadetarros.append(tarro)
    return listadetarros

def obtenmejor(soluciones):
    maximo=0
    indice=0
    for i in range (len(soluciones)):
        if maximo< sum(soluciones[i]):
            maximo=sum(soluciones[i])
            indice= i
    return i

def caben(todas,capacidad):
    sol=[]
    for i in range(len(todas)):
        sumas = sum(todas[i])
        if sumas<=capacidad:
            sol.append(todas[i])
    return sol

print(tarros_necesarios([10,15,20,8],25))#3
print(tarros_necesarios([1,3,10,15,4,10],25)) #2
print(tarros_necesarios([10,24,16,19],25)) #4

