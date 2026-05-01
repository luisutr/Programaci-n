
def matriz_adj(L):
    s, minimo, lista_coef = n_tuplas(L)
    W = []
    for i in range(s):
        W.append([0] * s)
    nodos = sorted(set(sum(L, tuple())))
    if max(lista_coef)-min(lista_coef)!=s:
        for k in L:
            x = k[0] - minimo
            y = k[1] - minimo
            W[y][x] = 1
    else:
        for k in L:
            x = k[0] - (minimo+1)
            y = k[1] - minimo
            W[y][x] = 1
    return tuple(W)


def n_tuplas(L):
    K=[]
    B=[]
    for i in range(len(L)):
        for a in L[i]:
            K.append(a)
    A=sorted(K)
    for p in A:
        if p not in B:
            B.append(p)
    return len(B), min(B),B


#print(matriz_adj([(2,3), (2,4), (4,5), (5,2)])) #, ((0,0,0,1), (1,0,0,0), (1,0,0,0), (0,0,1,0)))
#print(matriz_adj([(5,1), (4,2)]))
                         #((0,0,0,1), (0,0,1,0), (0,0,0,0), (0,0,0,0)))


def otra_matriz_ad(G):
    maximo = saca_maximo(G)
    M = matrizdeceros(maximo)
    M = pone_puntos(G,M)
    M = elimina(G,M)
    return M

def saca_maximo(G):
    mx=0
    for i in G:
        if mx<max(i):
            mx=max(i)
    return mx

def matrizdeceros(mx):
    M=[]
    for i in range(mx+1):
        fila=[]
        for j in range(mx+1):
            fila.append(0)
        M.append(fila)
    return M

def pone_puntos(G,M):
    for i in G:
        M[i[0]][i[1]]=1
    return M

def listadenum(G):
    lista=[]
    for i in G:
        lista+=i
    return lista

def elimina(G,M):
    listan = listadenum(G)
    aeliminar=[]
    mx = saca_maximo(G)
    for i in range(len(M)):
        if i not in listan:
            aeliminar.append(i)
    M = eliminaf(M,aeliminar)
    return M

def eliminaf(M,aeliminar):
    X=[]
    for j in range(len(M)):
        if j not in aeliminar:
            fila = M[j]
            fila = eliminaelem(fila,aeliminar)
            X.append(fila)
    return X

def eliminaelem(fila,aeliminar):
    f=[]
    for i in range(len(fila)):
        if i not in aeliminar:
            f.append(fila[i])
    return f

'''
import numpy as np
import pandas as pd
def elimina_filas(G,M):
    listan = listadenum(G)
    aeliminar=[]
    mx = saca_maximo(G)
    for i in range(len(M)):
        if i not in listan:
            aeliminar.append(i)
    df = pd.DataFrame(M, index=range(mx+1))
    df = (df.drop(aeliminar))
    df = df.drop(aeliminar, axis=1)
    print(df)
'''

print(otra_matriz_ad([(2,3), (2,4), (4,5), (5,2)]))


Matrizcon=[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0]]

