def monedas(valor):
    coins = [2, 1, .5, .2, .1, .05, .02, .01]
    listaf = []
    for i in coins:
        count = 0
        while valor >= i:
            valor -= i
            count += 1
            if i > valor:
                listaf.append((count,i))
                count = 0
    return tuple(listaf)

def ordenar_indirecto(v):
    orden=[]
    for i in enumerate(v): 
        orden.append(i)
    pos = sorted(orden, key = lambda e:e[1])
    result = []
    for j, k in pos:
        result.append(j)
    return tuple(result)

def media(V):
    if len(V)>0:
        for i in V:
            return sum(V)/len(V)
    return 0    

def subintervalo_mayor(sec):
    if len(sec) == 2:
        sec1 = sec[0]
        sec2 = sec[1]
        for i in list(range(sec2[0],sec2[-1]+1)):
            if i not in list(range(sec1[0],sec1[-1]+1)):
                if len(list(range(sec1[0],sec1[-1]+1))) > len(list(range(sec2[0],sec2[-1]+1))):
                    return sec[0]
                return sec[1]
            l = []
            for j in sec:
                for k in j:
                    l.append(k)
            l.sort()
            return min(l),max(l)
    sec1, sec2 = separa(sorted(quita_rep(tupla_conjunto(sec))))
    if len(sec1) > len(sec2):
        return((int(sec1[0]), int(sec1[-1])))
    return((int(sec2[0]), int(sec2[-1])))

def quita_rep(sec):
    sec2 = []
    for i in sec:
        if i not in sec2:
            sec2.append(i)
    return sec2

def separa(s):
    tupla1 = []
    tupla2 = []
    s_llena = list(range(s[0],s[-1]+1))
    for a,b in zip(s, s_llena):
        if a == b:
            tupla1.append(a)
        else:
            if a not in tupla1:
                tupla2.append(a)
    return tupla1, tupla2

def tupla_conjunto(sec):
    intervalos = []
    conjunto = []
    for intervalo in sec:
        intervalo_menor = list(range(intervalo[0],intervalo[1]+1))
        intervalos.append(intervalo_menor)
    for i in intervalos:
        for j in i:
            conjunto.append(j)
    return(conjunto)

def rectangulo_maximo(m):
    l = []
    orden = []
    f = sorted(enumerate(list(m)), key=lambda e:e[0])
    for i,t in f:
        pos = sorted(enumerate(t), key = lambda e:e[0])
        for j,n in pos:
            if n == 0:
                if (j,i) not in l:
                    l.append((j,i))
    ult = l[-1]
    return l[0],(ult[0]+1,ult[1]+1)

def particion(L,k):
    pivot = L[k]
    l_menor = []
    l_superior = []
    for i in L:
        if i < pivot:
            l_menor.append(i)
        elif i > pivot:
            l_superior.append(i)
    return l_menor, pivot, l_superior

def max2(L):
    L.sort(reverse = True)    
    return (L[0], L[1])

import random
def seleccionar_rapido(L,k):
    if len(L) == 1:
        return L[0]
    pivot = random.choice(L)
    menores = []
    mayores = []
    for i in L:
        if L.index(i) < L.index(pivot):
            menores.append(i)
        elif L.index(i) > L.index(pivot):
            mayores.append(i)
    if len(menores) == L.index(pivot):
        L.sort()
        return L[k]
    elif len(menores) == L.index(pivot):
        return seleccionar_rapido(menores, k)
    else:
        k = k-len(menores)
        return seleccionar_rapido(mayores, k)

def mayoritario(E):
    E2 = []
    for i in E:
        if i not in E2:
            E2.append(i)
    e = {}
    for i in E2:
        e[i] = E.count(i)
    for k, v in e.items():
        if v >= len(E)/2:
            return k
    raise ValueError('')
    
def buscar_sumandos(V,x):
    v = sorted(enumerate(V), key = lambda e:e[0])
    for i,I in v:
        for j,J in v:
            if (i,I) != (j,J):
                if I+J == x:
                    return i,j
    raise ValueError('')
    
from unittest import TestCase, main
class Test(TestCase):
    def test_monedas(self):
        self.assertEqual(monedas(9.4), ((4, 2), (1, 1), (2, 0.2)))
        self.assertEqual(monedas(1.5), ((1, 1), (1, 0.5)))
        self.assertEqual(monedas(.01), ((1, 0.01),))
        self.assertEqual(monedas(0), tuple())

    def test_ordenar_indirecto(self):
        self.assertEqual(ordenar_indirecto((50, 98, 10, 63, 31, 25, 63, 74)),
                         (2, 5, 4, 0, 3, 6, 7, 1))
        self.assertEqual(ordenar_indirecto(tuple(range(1,10))), tuple(range(9)))
        self.assertEqual(ordenar_indirecto(tuple()), tuple())
        self.assertEqual(ordenar_indirecto((1,)), (0,))

    def test_media(self):
        self.assertEqual(media([1,2,4,8,16,32,64,128]), 31.875)
        self.assertEqual(media([2]), 2)
        self.assertEqual(media([]),0)
        self.assertEqual(media([1,5]), 3)

    def test_subintervalo_mayor(self):
        self.assertEqual(subintervalo_mayor(((1,4),(5,6))),(1,4))
        self.assertEqual(subintervalo_mayor(((1,5),(4,6))),(1,6))
        self.assertEqual(subintervalo_mayor(((5,7),(9,11),(2,5),(1,4),(4,6))),(1,7))
        self.assertEqual(subintervalo_mayor(((4,6),)),(4,6))

    def test_rectangulo_maximo(self):
        self.assertEqual(rectangulo_maximo(((1,0,0,1),(1,0,0,1),(0,0,0,1),(1,1,1,1))),
                         ((1,0),(3,3)))
        self.assertEqual(rectangulo_maximo(((1,0),(1,0))), ((1,0),(2,2)))
        self.assertEqual(rectangulo_maximo(((0,),)), ((0,0),(1,1)))
        self.assertEqual(rectangulo_maximo(((0,),)), ((0,0),(1,1)))
        
    def test_particion(self):
        def tp(L,k):
            a,b,c = particion(L,k)
            self.assertEqual(len(a) + len(c), len(L) - 1)
            self.assertTrue(all(e < b for e in a))
            self.assertTrue(all(e > b for e in c))
            self.assertEqual(b, L[k])
        tp([32, 17, 41, 18, 52, 98, 24, 65], 2)
        tp([52, 98, 24], 2)
        tp([52, 1, 98], 2)
        tp([52, 5, 1], 2)

    def test_seleccionar_rapido(self):
        self.assertEqual(seleccionar_rapido([5], 0), 5)
        from random import shuffle
        L = list(range(8))
        self.assertEqual(seleccionar_rapido(L, 3), 3)
        L = list(range(3,18))
        shuffle(L)
        self.assertEqual(seleccionar_rapido(L,3), 6)
        L = list(range(4,100,2))
        shuffle(L)
        self.assertEqual(seleccionar_rapido(L,5), 14)

    def test_max2(self):
        self.assertEqual(max2([1,2]), (2,1))
        from random import shuffle
        L = list(range(8))
        self.assertEqual(max2(L), (7,6))
        L = list(range(3,18))
        shuffle(L)
        self.assertEqual(max2(L), (17,16))
        L = list(range(4,100,2))
        shuffle(L)
        self.assertEqual(max2(L), (98,96))

    def test_mayoritario(self):
        self.assertEqual(mayoritario([1,1,2]), 1)
        self.assertEqual(mayoritario([1,2,2,1,3,1,1,1]), 1)
        self.assertEqual(mayoritario([1]), 1)
        with self.assertRaises(ValueError):
            mayoritario([1,2,3])

    def test_buscar_sumandos(self):
        def ts(V,x):
            i,j = buscar_sumandos(V, x)
            self.assertNotEqual(i,j)
            self.assertEqual(V[i]+V[j], x)
        ts([12, 4, 14, 17, 9], 13)
        ts([1, 1], 2)
        ts([1, 2, 1], 2)
        with self.assertRaises(ValueError):
            buscar_sumandos([1,2,3], 8)

# Si usas Jupyter descomenta la última línea
# Si usas IDLE, Python o PyCharm descomenta la penultima
main()
# main(argv=['first-arg-is-ignored'], exit=False)
