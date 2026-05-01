def splitN(L,n):
    r=[]
    rdiv=[]
    for i in L:
        r.append(i)
    for j in range(0, len(r), n):
        rdiv.append(tuple(r[j:j+n]))
    return tuple(rdiv)

def listanumeros(L):
    lista=[]
    for i in L:
        for j in i:
            if j not in lista:
                lista.append(j)
    return set(sorted(lista))

def matriz_adj(L):
    nodos = (listanumeros(L))
    matriz=[]
    for y in nodos:
        fila=[1 if (x,y) in L else 0 for x in nodos]
        matriz.append(tuple(fila))
    return tuple(matriz)

print(matriz_adj([(2,3), (2,4), (4,5), (5,2)]))

def arbol_binario(L):
    arbol=None
    for i in L:
        arbol = construye(arbol, i)
    return arbol
#si el padre es mayor del elemento que quiero meter, devuelvo la estructura con recuersividad,
# por si el elemento que meto a su vez es un arbol
def insertohijo(padre, hijoizq,hijoder,i):
    if padre > i:
        return padre, construye(hijoizq, i), hijoder
    #si el madre es menor que el elemento a meter
    else:
        return padre, hijoizq, construye(hijoder, i)
def construye(arbol, i):
    #caso base, si el arbol esta vacio
    if arbol == None:
        return i, None, None
    else:
        #si el arbol no esta vacio
        #fragmento el arbol en raiz padre, hijo izquierdo hijo derecho
        padre, hijoizq, hijoder = arbol
        return insertohijo(padre, hijoizq,hijoder,i)

print(arbol_binario([3, 8, 1, 13, 5, 9]))

def buscar(arbol, valor):
    if arbol == None and valor != None:
        return False
    padre, hijoizq, hijoder = arbol
    if padre == valor:
        return True
    elif padre < valor:
        if hijoder:
            return buscar(hijoder, valor)
        return False
    if hijoizq:
        return buscar(hijoizq, valor)
    return False

def arbol_a_conjunto(A):
    if A == None:
        return set()
    padre, hijoizq, hijoder = A
    return {padre}.union(arbol_a_conjunto(hijoizq)).union(arbol_a_conjunto(hijoder))

def mezcla(A, B):
    D = {}
    for ka, a in A.items():
        D[ka] = a
        for kb, b in B.items():
            if ka == kb in D:
                D[ka] = a,b
            elif kb not in D:
                D[kb] = b
    return D

def hay_ciclo(G):
    l=[]
    for fila in G:
        for i in fila:
            l.append(i)
    if l[0] == l[-1]:
        return True
    return False

def presente_indicativo(verbo):
    terminacion = verbo[-2:]
    raiz = verbo[:-2]
    conjugaciones = {
        'ar': ('o','as','a','amos','áis','an'),
        'er': ('o', 'es', 'e', 'emos', 'éis', 'en'),
        'ir': ('o', 'es', 'e', 'imos', 'ís', 'en')
        }
    l=[]
    for clave,valor in conjugaciones.items():
        if clave == terminacion:
            for i in valor:
                l.append(raiz+i)
    return l

def cuartiles(L):
    values=sorted(L)
    if len(L) < 4:
        efin = values[-1]
        return(q1(values), q2(values), efin, efin)
    return(q1(values), q2(values), q3(values), values.pop())

def q1(values):
    d = abs((len(values)+1)/4)-int((len(values)+1)/4)
    if d != 0:
        return values[int((len(values)+1)/4)-1]+d*(values[int((len(values)+1)/4)]-values[int((len(values)+1)/4)-1])
    return values[int((len(values)/4)-1)]

def q2(values):
    if len(values) % 2 == 0:
        return (values[int((len(values)/2)-1)]+values[int(len(values)/2)])/2
    return values[int(len(values)//2)]

def q3(values):
    d = abs(3*(len(values)+1)/4)-int(3*(len(values)+1)/4)
    if d != 0:
        return values[int(3*(len(values)+1)/4)-1]+d*(values[int(3*(len(values)+1)/4)]-values[int(3*(len(values)+1)/4)-1])
    return values[int(3*(len(values)/4)-1)]


def rpn_to_algebraic(s):
    op = ['+','-','*','/']
    rpn=[]
    for i in s.split():
        if i in op:
            a = str(rpn.pop())
            b = str(rpn.pop())
            rpn.append(str('(' + str(b) + ' ' + i + ' ' + str(a) + ')'))
        else:
            rpn.append(str(int(i)))
    return rpn.pop()


from unittest import TestCase, main
class Test(TestCase):
    def test_splitN(self):
        self.assertEqual(list(splitN(range(6),3)), [(0,1,2),(3,4,5)])
        self.assertEqual(list(splitN(range(6),2)), [(0,1),(2,3),(4,5)])
        self.assertEqual(list(splitN(range(3),3)), [(0,1,2)])
        self.assertEqual(list(splitN([],3)), [])

    def test_matriz_adj(self):
        self.assertEqual(matriz_adj([(2,3), (2,4), (4,5), (5,2)]),
                         ((0,0,0,1), (1,0,0,0), (1,0,0,0), (0,0,1,0)))
        self.assertEqual(matriz_adj([(5,3), (4,4)]),
                         ((0,0,1), (0,1,0), (0,0,0)))
        self.assertEqual(matriz_adj([(5,5), (4,4)]),
                         ((1,0), (0,1)))
        self.assertEqual(matriz_adj([(5,1), (4,2)]),
                         ((0,0,0,1), (0,0,1,0), (0,0,0,0), (0,0,0,0)))

    def test_arbol_binario(self):
        self.assertEqual(arbol_binario([3, 8, 1, 13, 5, 9]),
                         (3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))))
        self.assertEqual(arbol_binario(range(5)),
                         (0, None, (1, None, (2, None, (3, None, (4, None, None))))))
        self.assertEqual(arbol_binario(list(reversed(range(5)))),
                         (4, (3, (2, (1, (0, None, None), None), None), None), None))
        self.assertEqual(arbol_binario([]), None)

    def test_buscar(self):
        self.assertTrue(buscar((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))),
                               13))
        self.assertFalse(buscar((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))),
                                12))
        self.assertTrue(buscar((4, (3, (2, (1, (0, None, None), None), None), None), None),
                               0))
        self.assertFalse(buscar(None, 0))

    def test_arbol_a_conjunto(self):
        self.assertEqual(arbol_a_conjunto(None), set())
        self.assertEqual(arbol_a_conjunto((5,None,None)), {5})
        self.assertEqual(arbol_a_conjunto((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None)))),
                         {3,8,1,13,5,9})
        self.assertEqual(arbol_a_conjunto((4, (3, (2, (1, (0, None, None), None), None), None), None)),
                         {0,1,2,3,4})

    def test_mezcla(self):
        self.assertEqual(mezcla({'a':1}, {'b':2}), {'a':1,'b':2})
        self.assertEqual(mezcla({'a':1,'e':2}, {'a':1,'b':2}), {'a':(1,1),'b':2,'e':2})
        self.assertEqual(mezcla({}, {}), {})
        self.assertEqual(mezcla({1:2,2:3,3:4}, {1:1,2:2,3:3}), {1:(2,1),2:(3,2),3:(4,3)})

    def test_hay_ciclo(self):
        self.assertTrue(hay_ciclo([(1,1)]))
        self.assertTrue(hay_ciclo([(1,2),(3,4),(2,3),(4,1)]))
        self.assertFalse(hay_ciclo([(1,2),(3,4),(2,3),(4,11)]))
        self.assertFalse(hay_ciclo([(1,2),(3,4),(2,3),(3,4)]))

    def test_conjugacion(self):
        self.assertEqual(presente_indicativo('amar'),
                         ['amo', 'amas', 'ama', 'amamos', 'amáis', 'aman'])
        self.assertEqual(presente_indicativo('leer'),
                         ['leo', 'lees', 'lee', 'leemos', 'leéis', 'leen'])
        self.assertEqual(presente_indicativo('batir'),
                         ['bato', 'bates', 'bate', 'batimos', 'batís', 'baten'])
        self.assertEqual(presente_indicativo('ir'),
                         ['o', 'es', 'e', 'imos', 'ís', 'en'])

    def test_cuartiles(self):
        self.assertEqual(cuartiles((63,34,60,30,45,32,56,40,21,37,54,33,28,53,19,45,28,52,24,29)),
                         (28.25, 35.5, 52.75, 63))
        self.assertEqual(cuartiles(range(10)), (1.75, 4.5, 7.25, 9))
        self.assertEqual(cuartiles((1,2,3)), (1,2,3,3))
        self.assertEqual(cuartiles((1,1,1)), (1,1,1,1))

    def test_rpn_to_algebraic(self):
        self.assertEqual(rpn_to_algebraic('12 3 - 2 5 * +'), '((12 - 3) + (2 * 5))')
        self.assertEqual(rpn_to_algebraic('1 2 3 4 - - -'), '(1 - (2 - (3 - 4)))')
        self.assertEqual(rpn_to_algebraic('1 2 - 3 - 4 -'), '(((1 - 2) - 3) - 4)')
        self.assertEqual(rpn_to_algebraic('1'), '1')

# Si usas Jupyter descomenta la última línea
# Si usas IDLE, Python o PyCharm descomenta la penultima
main()
