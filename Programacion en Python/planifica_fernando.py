# practica4
def planifica(L, m, k):
    caben=cabenendisco(L,k)
    listadiscos=[]
    while len(listadiscos) < m:
        graba = 0
        mejor = tomarmejor(caben)
        listadisco = []
        for cancion in caben[mejor]:
            if cancion in L:
                listadisco.append(L.index(cancion))
            else:
                graba+=1
        if graba == 0:
            for i in listadisco:
                L[i] = "*"
            listadiscos.append(tuple(listadisco))
        caben.pop(mejor)
    return listadiscos

def combinations(N, L):
    if not N:
        return [[]]
    if not L:
        return []
    head = [L[0]]
    tail = L[1:]
    new_comb = [head + list_ for list_ in combinations(N - 1, tail)]
    return new_comb + combinations(N, tail)

def todaslascombinaciones(canciones):
    posibles = []
    for i in range(len(canciones)):
        posibles += combinations(i, canciones)
    return posibles

def cabenendisco(posibles,k):
    solucion = []
    suma = 0
    posibles=todaslascombinaciones(posibles)
    for i in range(len(posibles)):
        suma = sum(list(posibles[i]))
        if suma <= k:
            solucion.append(posibles[i])
    return solucion

def tomarmejor(caben):
    maximo=0
    longitud=0
    posicion=0
    for i in range(len(caben)):
        if maximo<sum(caben[i]):
                maximo=sum(caben[i])
    for j in range(len(caben)):
        if maximo == sum(caben[j]) and longitud<len(caben[j]):
            posicion=j
    return posicion

def tomarmejorconrep(caben):
    maximo=0
    longitud=0
    posicion=0
    for i in range(len(caben)):
        if longitud<len(caben[i]):
                longitud=len(caben[i])
    for j in range(len(caben)):
        if longitud == len(caben[j]) and maximo<sum(caben[j]):
            posicion=j
    return posicion


print(planifica([10, 15, 20, 8],2,25))
print(planifica([10, 15],2,25))
print(planifica([10, 25, 15],2,25))
print(planifica([10, 1, 2, 3, 15, 4, 25, 15, 1],2,25))


# Descomenta la siguiente línea y la última para ejecutar las pruebas
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
# main(argv=['first-arg-is-ignored'], exit=False)