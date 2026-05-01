def recorrer(G,origen,camino):
    G, signodo = verticeadj(G,origen)
    if signodo != []:
        camino.append(signodo)
        sig = sum(signodo)-origen
        recorrer(G,sig,camino)
    return camino
def verticeadj(G,elemento):
    v=[]
    if G !=[]:
        for i in range(len(G)):
            if elemento in G[i]:
                v = G[i]
                G.pop(i)
                return G,v
    return G, v
def hay_ciclo(G):
    for i in G:
        for j in i:
            camino = recorrer(G,j,[])
            if camino != None and camino!=[]:
                print(camino)
                if camino[0][0] == camino[-1][1]:
                    return True
    return False




print(hay_ciclo([(1,1)]))
print(hay_ciclo([(1,2),(3,4),(2,3),(4,1)]))
print(hay_ciclo([(1,2),(3,4),(2,3),(4,11)]))
print(hay_ciclo([(1,2),(3,4),(2,3),(3,4)]))
print(hay_ciclo([(1,2),(3,1)]))