import itertools
def planifica(L,m,k):
    grabados = []
    for p in range(m+1):
        lista = list(itertools.permutations(L,p))
        for i in lista:
            if sum(i) <= k:
                grabados.append(sorted(i))
    grabados = list(reversed(sorted(grabados)))
    solucion=seleccionamejores(grabados,m,k)
    copias = []
    for i in solucion:
        if m > 0:
            copias.append(i)
            m-=1
    indices=[]
    print(copias)
    for archivo in L:
        tupla=[]
        for copia in copias:
            if archivo in copia:
                if len(copia)==1:
                    tupla.append(L.index(archivo))
                if len(copia) > 1:
                    con = 0
                    while(con<len(copia)):
                        tupla.append(L.index(copia[con]))
                        con += 1
        if tuple(tupla) not in indices and tupla != []:
            indices.append(tuple(tupla))
    return indices

def seleccionamejores(L,m,k):
    mejores=[]
    for i in range(len(L)-1):
        suma = sum(L[i])
        siguiente = 1
        sumasig = sum(L[i+siguiente])
        while (suma >= sumasig and siguiente < len(L)):
            if suma>= sumasig:
                mayor=i
            else:
                mayor=siguiente
                suma = sumasig
            siguiente+=1
        if L[mayor] not in mejores:
            mejores.append(L[mayor])
    return mejores
print(planifica([10,15,20,8],2,25))