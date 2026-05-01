from itertools import permutations
def moch (lista,n, k):
    combinaciones=[]
    for i in range(len(lista)):
        combinaciones.append(list(permutations(lista,i)))
    #print list(reversed(combinaciones))
    listacd=[]
    for j in range(n):
        for combinacion in combinaciones:
            aux=0
            cancionselect=[]
            for canciones in combinacion:
                if sum(canciones)<=k and sum(canciones)>aux:
                    aux=sum(canciones)
                    cancionselect=list(canciones)
            listacd.append(cancionselect)
    return set(listacd)


print (moch([10,15,20,8],2,25))

