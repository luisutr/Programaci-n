def nudos_relacionados(G, origen, final):
    salida = []
    adyacentes= nodosadyacentes(G,origen)
    for i in adyacentes:
        for j in i:
            G.remove(j)
    salida = recorrercamino(adyacentes,salida, final, G)
    return salida

def recorrercamino(adyacentes,salida, final, copia):
    if adyacentes:
        camino = adyacentes.pop()
        nodo = camino[len(camino) - 1]
        caminos = caminosposibles(copia,nodo)
        for i in caminos:
            if final not in i:
                camino_nuevo = camino + [i]
                adyacentes.append(camino_nuevo)
                copia.remove(i)
            else:
                camino_nuevo = camino + [i]
                salida.append(camino_nuevo)
        return recorrercamino(adyacentes, salida, final, copia)
    return salida


def nodosadyacentes(G,origen):
    adynts = []
    for i in G:
        if origen in i:
            adynts.append([i])
    return adynts

def caminosposibles(G,nodo):
    v=[]
    for i in G:
        for elemento in nodo:
            if elemento in i:
                v.append(i)
    return v

def pasaatupla(sol):
    soltup = []
    if sol != []:
        for tupla in sol:
            soltup.append(tuple(tupla))
        return tuple(soltup)

def copiaG(G):
    lista=[]
    for i in G:
        lista.append((i[1], i[2]))
    return lista

def maze_solver(G, origen, final):
    if len(G) == 1 and  final in G[0]:
        return G
    salida = nudos_relacionados(G, origen, final)
    salida = pasaatupla(salida)
    return salida

def calculapeso(camino, pesos, G):
    suma=0
    for i in camino:
        pos = G.index(i)
        suma += pesos[pos]
    return suma


def distancia(origen,final,G):
    pesos=[]
    copia = copiaG(G)
    copia = sorted(copia)
    for i in G:
        pesos.append(i[0])
    caminos = maze_solver(copia, origen, final)
    minimo=999
    posmin=0
    copia = copiaG(G)
    if caminos:
        for camino in range(len(caminos)):
            pesocamino = calculapeso(caminos[camino], pesos, copia)
            if minimo>pesocamino:
                minimo=pesocamino
                posmin = camino
        if (origen, final) in copia and minimo>pesos[copia.index((origen, final))]:
            return pesos[copia.index((origen, final))]
        return minimo
    if (origen, final) in copia:
        return pesos[copia.index((origen, final))]

#(coste,a,b)
G = ((3, 0, 1), (5, 0, 2), (1, 0, 3), (7, 2, 3), (7, 2, 4), (1, 2, 5), (4, 3, 5),
     (3, 1, 0), (5, 2, 0), (1, 3, 0), (7, 3, 2), (7, 4, 2), (1, 5, 2), (4, 5, 3))

print(distancia(3,4,G))
print(distancia(2,4,G))
print(distancia(2,3,G))
print(distancia(0,2,G))

from unittest import TestCase, main

class Test(TestCase):

    def test_distancia(self):
        G = ((3, 0, 1), (5, 0, 2), (1, 0, 3), (7, 2, 3), (7, 2, 4), (1, 2, 5), (4, 3, 5),
             (3, 1, 0), (5, 2, 0), (1, 3, 0), (7, 3, 2), (7, 4, 2), (1, 5, 2), (4, 5, 3))
        casos = [(G, 3, 4, 12), (G, 2, 4, 7), (G, 2, 3, 5), (G, 0, 2, 5)]
        for G, i, j, d in casos:
            self.assertEqual(distancia(i, j, G), d)

# Si usas Jupyter o VSCode descomenta la ultima línea
# Si usas IDLE, Python o PyCharm descomenta la penultima
main()