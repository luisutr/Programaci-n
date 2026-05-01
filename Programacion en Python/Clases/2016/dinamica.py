__author__ = 'luisutrilla'

import random

def prueba0():
    nombres = ['a', 'b', 'c', 'd']
    valores = [6, 7, 8, 9]
    pesos = [3, 3, 2, 5]
    elems = zip(nombres, valores, pesos)
    val, saco = mochila01(elems, 5)
    for e in saco:
        print e
    print 'Valor total =', val

def constr_elems(n, valMax, pesoMax):
    return [ (str(i),
              random.randint(1, valMax),
              random.randint(1, pesoMax)) \
             for i in range(n) ]

def prueba1(n):
    elems = constr_elems(n, 10, 10)
    val, saco = mochila01(elems, 40)
    print 'Contenido del saco'
    for e in saco:
        print e
    print 'Valor total =', val

def valor(e): return e[1]
def peso(e): return e[2]

def mochila01(disponibles, pesoMax = 20):
    pset = genPowerset(disponibles)
    return elegir(pset, pesoMax)

def elegir(pset, pesoMax):
    mejorVal, mejorSaco = 0.0, None
    for saco in pset:
        valor, peso = valorPesoSaco(saco)
        if peso <= pesoMax and valor > mejorVal:
            mejorVal, mejorSaco = valor, saco
    return (mejorVal, mejorSaco)

def valorPesoSaco(saco):
    v, p = 0.0, 0.0
    for elem in saco:
        v += valor(elem)
        p += peso(elem)
    return (v, p)

def genPowerset(L):
    powerset = []
    for i in range(2**len(L)):
        powerset.append(genSubset(L,i))
    return powerset
def genSubset(L, i):
    subset = []
    for j in range(len(L)):
        if isBitSet(i, j):
            subset.append(L[j])
def isBitSet(n, bit):
    return n & (1 << bit) != 0

prueba1(20)
