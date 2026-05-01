def muevo(origen, arco):
    for x in arco:
        if x != origen:
            return x

def siguiente(G,nodo):
    v=[]
    if G !=[]:
        for i in range(len(G)):
            if nodo in G[i]:
                v = G[i]
                G.pop(i)
                return G,v
    return G, v

def recorregrafo( G,origen,sol):
    G, sig = siguiente(G,origen)
    if sig != []:
        sol.append(sig)
    if 0 in sig:
        return sol
    origen = muevo(origen,sig)
    if sig != []:
        recorregrafo(G,origen,sol)
    return sol

def hay_ciclo(G):
    if len(G) == 1:
        if G[0][0] == G[0][1]:
            return True
    for nodo in G:
        camino = recorregrafo(G,nodo[0],[])
        if camino != None and camino!=[]:
            if camino[0][0] == camino[-1][1]:
                return True
        camino = recorregrafo(G, nodo[1], [])
        if camino != None and camino != []:
            if camino[0][0] == camino[-1][1]:
                return True
    return False
'''
print(hay_ciclo([(1,1)]))
print(hay_ciclo([(1,2),(3,4),(2,3),(4,1)]))
print(hay_ciclo([(1,2),(3,4),(2,3),(4,11)]))
print(hay_ciclo([(1,2),(3,4),(2,3),(3,4)]))
print(hay_ciclo([(1,2),(3,1)]))
'''

# Descomenta la siguiente línea y la última para ejecutar las pruebas
from unittest import TestCase, main

class Test(TestCase):
    def test_hay_ciclo(self):
        self.assertTrue(hay_ciclo([(1, 1)]))
        self.assertTrue(hay_ciclo([(1, 2), (3, 4), (2, 3), (4, 1)]))
        self.assertFalse(hay_ciclo([(1, 2), (3, 4), (2, 3), (4, 11)]))
        self.assertFalse(hay_ciclo([(1, 2), (3, 4), (2, 3), (3, 4)]))
        self.assertFalse(hay_ciclo([(1, 2), (3, 1)]))

# Si usas Jupyter descomenta la última línea
# Si usas IDLE, Python o PyCharm descomenta la penultima
main()
# main(argv=['first-arg-is-ignored'], exit=False)
