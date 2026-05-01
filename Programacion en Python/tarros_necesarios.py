
def tarros_necesarios(lp, capacidad):
    todas = todasper(lp)
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

#hace todas las permutaciones posibles de elementos
def todasper(lp):
    todas=[]
    permutaciones=[]
    for i in range(len(lp)):
        permutaciones+=(list(permutations(lp,i)))
    for lista in permutaciones:
        if len(lista)==1:
            todas.append(tuple(sorted(lista)))
        elif tuple(sorted(lista)) not in todas:
            todas.append(tuple(sorted(lista)))
    print(todas)
    return todas


#print (tarros_necesarios([10,15,20,8],25))#3
print (tarros_necesarios([1,3,10,15,4,10],25)) #2
#print (tarros_necesarios([10,24,16,19],25)) #4
