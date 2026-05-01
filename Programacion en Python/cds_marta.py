def combinaciones(canciones):
    posibles=[]
    for i in range(len(canciones)):
        posibles+=combina(i,canciones)
    return posibles

def combina(N, lista):
    if N==0:
        return [[]]
    if len(lista)==0:
        return []
    elegido = [lista[0]]
    resto = lista[1:]
    combi = []
    for i in combina(N - 1, resto):
        combi.append(elegido+i)
    return combi + combina(N, resto)

def obtenmejor(soluciones):
    maximo = 0
    longitud = 0
    posicion = 0
    for i in range(len(soluciones)):
        if maximo < sum(soluciones[i]):
            maximo = sum(soluciones[i])
    for j in range(len(soluciones)):
        if maximo == sum(soluciones[j]) and longitud < len(soluciones[j]):
            posicion = j
    return posicion

def caben(todas,R):
    sol=[]
    for i in range(len(todas)):
        sumas = sum(todas[i])
        if sumas<=R:
            sol.append(todas[i])
    return sol

def copialista(L):
    lista=[]
    for i in L:
        lista.append(i)
    return lista

def planifica(L, m, k):
    if sum(L)<=k:
        lista=[]
        for i in range(len(L)):
            lista.append(i)
        return [tuple(lista), ()]
    todas=combinaciones(L)
    soluciones = caben(todas,k)
    listacds=[]
    copia = copialista(L)
    ncds= m
    while (ncds>0):
        imejor=obtenmejor(soluciones)
        mejor = soluciones[imejor]
        soluciones.pop(imejor)
        tarro = []
        usada=0
        for cancion in mejor:
            veces = 0
            for CD in listacds:
                if L.index(cancion) in CD:
                    veces+=1
            if veces >= L.count(cancion):
                usada+=1
        if usada==0:
            for i in mejor:
                if i in copia:
                    cosa = copia.index(i)
                    tarro.append(cosa)
                    copia[cosa] = "*"
            if len(tarro)>0:
                listacds.append(tuple(tarro))
            ncds-=1
    return (listacds)


#print(planifica([10, 15, 20, 8],2,25))
#print(planifica([10, 15],2,25))
#print(planifica([10, 25, 15],2,25))
#print(planifica([10, 1, 2, 3, 15, 4, 25, 15, 1],2,25))

from unittest import TestCase, main

class Test(TestCase):

    def test_planifica(self):
        m, k = 2, 25

        def check_planifica(L, n):
            D = planifica(L, m, k)
            self.assertEqual(sum(len(i) for i in D), n,
                             'planifica({},{},{}) debe guardar {} archivos. Devolvió {}.'.format(L, m, k, n, D))
            files = set(sum(D, tuple()))
            self.assertEqual(len(files), n,
                             'planifica({},{},{}) debe guardar {} archivos diferentes'.format(L, m, k, n))

        check_planifica([10, 15, 20, 8], 3)
        check_planifica([10, 15], 2)
        check_planifica([10, 25, 15], 3)
        check_planifica([10, 25, 15, 1], 3)
        check_planifica([10, 1, 2, 3, 15, 4, 25, 15, 1], 7)


# Si usas Jupyter o VSCode descomenta la última línea
# Si usas IDLE, Python o PyCharm descomenta la penultima
main()