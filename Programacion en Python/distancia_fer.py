
def degrafoadicc(G):
    dicc={}
    for i in G:
        p,o,d=i
        if o in dicc.keys():
            dicc[o].append((d,p))
        else:
            dicc[o]=[(d,p)]
    return dicc


def dijkstra(i,j,G):
    #G=degrafoadicc(G)
    """
    Determina el camino mas corto entre los vertices 'a' y 'z' de un
    grafo ponderado y conexo 'G'.
    """
    assert i in G
    assert j in G

    # Definicion de infinito como un valor mayor
    # al doble de suma de todos los pesos
    Inf = 0
    for u in G:
        for v, w in G[u]:
            Inf += w

    # Inicializacion de estructuras auxiliares:
    #  L: diccionario vertice -> etiqueta
    #  S: conjunto de vertices con etiquetas temporales
    #  A: vertice -> vertice previo (en camino longitud minima)
    L = dict([(u, Inf) for u in G]) #py3: L = {u:Inf for u in G}
    L[i] = 0
    S = set([u for u in G]) #py3: S = {u for u in G}
    A = { }

    # Funcion auxiliar, dado un vertice retorna su etiqueta
    # se utiliza para encontrar el vertice the etiqueta minima
    def W(v):
        print("v=",v)
        return L[v]
    def quitaelmenor(S,L):
        menor=99
        choice=-1
        for ele in S:
            if L[ele]<menor:
                menor=L[ele]
                choice=ele
        return choice
    # Iteracion principal del algoritmo de Dijkstra
    while j in S:
        #print("L=",L)
        #print("S=", S)
        u = quitaelmenor(S,L)
        #print("u=",u)
        S.discard(u)
        for v, w in G[u]:
            if v in S:
                if L[u] + w < L[v]:
                    L[v] = L[u] + w
                    A[v] = u

    # Reconstruccion del camino de longitud minima
    P = []
    u = j
    while u != i and u in A.keys():
        P.append(u)
        u = A[u]
    P.append(i)
    P.reverse()

    # retorna longitud minima y camino de longitud minima
    return L[j], P




G = ((3, 0, 1), (5, 0, 2), (1, 0, 3), (7, 2, 3), (7, 2, 4), (1, 2, 5), (4, 3, 5),
     (3, 1, 0), (5, 2, 0), (1, 3, 0), (7, 3, 2), (7, 4, 2), (1, 5, 2), (4, 5, 3))

def distancia(i,j,G):
    dG=degrafoadicc(G)
    w, p =  dijkstra(i,j,dG)
    #print (p)
    #print (w)
    return w


print(distancia(3,4,G))
print(distancia(2,4,G))
print(distancia(2,3,G))
print(distancia(0,2,G))
