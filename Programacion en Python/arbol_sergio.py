
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


from unittest import TestCase, main
class Test(TestCase):
        def test_arbol_binario(self):
        self.assertEqual(arbol_binario([3, 8, 1, 13, 5, 9]),
                         (3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))))
        self.assertEqual(arbol_binario(range(5)),
                         (0, None, (1, None, (2, None, (3, None, (4, None, None))))))
        self.assertEqual(arbol_binario(list(reversed(range(5)))),
                         (4, (3, (2, (1, (0, None, None), None), None), None), None))
        self.assertEqual(arbol_binario([]), None)

# Si usas Jupyter descomenta la última línea
# Si usas IDLE, Python o PyCharm descomenta la penultima
main()
