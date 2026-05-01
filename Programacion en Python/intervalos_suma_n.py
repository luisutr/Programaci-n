def intervalos_suma (n):
    soluciones=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            suma = i
            intervalo = []
            intervalo.append(i)
            while (suma+j)<=n:
                suma+=j
                intervalo.append(j)
            if sum(intervalo)==n and (sorted(intervalo) not in soluciones):
                soluciones.append(intervalo)
    return soluciones

#print(intervalos_suma(5))


def subintervalo_mayor(conjuntos):
    if len(conjuntos)==1:
        return conjuntos[0]
    existia=False
    conjuntosenteros=[]
    aux=0
    #creo una lista de los intervalos con todos sus numeros
    for conjunto in conjuntos:
        sublista=[]
        for i in range(conjunto[0],conjunto[1]+1):
            sublista.append(i)
        conjuntosenteros.append(sublista)
    conjuntosenteros = sorted(conjuntosenteros)
    aux = conjuntosenteros[0]
    conjuntointervalos=[]
    # ordenada la lista de intervalos, veo si algun intervalo se solapa y lo uno
    for i in range(1,len(conjuntosenteros)):
        if min(conjuntosenteros[i]) in aux:
                aux = aux+conjuntosenteros[i]
                conjuntointervalos.append(aux)
        else:
            conjuntointervalos.append(aux)
            conjuntointervalos.append(conjuntosenteros[i])
            aux= conjuntosenteros[i]
    pos=0
    aux = 0
    #una vez esta nueva lista ya preprada con los intervalos solapadps unidos, veo cual es la mas larga
    for x in range(len(conjuntointervalos)):
        if max(conjuntointervalos[x])-min(conjuntointervalos[x])>aux:
            aux=max(conjuntointervalos[x])-min(conjuntointervalos[x])
            pos=x
    return min(conjuntointervalos[pos]), max(conjuntointervalos[pos])






print(subintervalo_mayor(((1,4),(5,6))),(1,4))
print(subintervalo_mayor(((1,5),(4,6))),(1,6))
print(subintervalo_mayor(((5,7),(9,11),(2,5),(1,4),(4,6))),(1,7))
print(subintervalo_mayor(((4,6),)),(4,6))