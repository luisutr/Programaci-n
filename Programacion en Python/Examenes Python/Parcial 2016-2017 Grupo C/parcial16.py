# -*- coding: utf-8 -*-

import random

def comprobarcubo(cubo):
    h1= sum(cubo[0])
    h2=sum(cubo[1])
    h3=sum(cubo[2])
    v1=cubo[0][0]+cubo[1][0]+cubo[2][0]
    v2=cubo[0][1]+cubo[1][1]+cubo[2][1]
    v3=cubo[0][2]+cubo[1][2]+cubo[2][2]
    d1=cubo[0][0]+cubo[1][1]+cubo[2][2]
    d2=cubo[0][2]+cubo[1][1]+cubo[2][0]
    if h1 == h2 and h2 == h3 and h3 == v1 and v1 == v2 and v2 == v3 and v3 == d1 and d1 == d2:
        return True,h1,h2,h3,v1,v2,v3,d1,d2
    else:
        return False,h1,h2,h3,v1,v2,v3,d1,d2




def iniciocubo():
    cubo=[]
    subcobo1=[]
    subcobo2=[]
    subcobo3=[]
    for i in range(4):
        for j in range(3):
            if i == 0:
                subcobo1.append(0)
            if i == 1:
                subcobo2.append(0)
            if i == 2:
                subcobo3.append(0)
        if i == 0:
            cubo.append(subcobo1)
        if i == 1:
            cubo.append(subcobo2)
        if i == 2:
            cubo.append(subcobo3)
    return cubo

def exitste(cubo,valor):
    for i in range(len(cubo)):
        subcubo=cubo[i]
        for j in range(len(subcubo)):
            if subcubo[j] == valor:
                return True
    return False

def darsolucion(cubo):
    return "YES"

def cuadro_magico():
    cubo = iniciocubo()
    for i in range(len(cubo)):
        subcubo=cubo[i]
        for j in range(len(subcubo)):
            valor = random.randint(0,9)
            var=exitste(cubo,valor)
            while var==True:
                valor = random.randint(0,9)
                var=exitste(cubo,valor)
            subcubo[j]=valor
    result=[]
    while True:
        es,h1,h2,h3,v1,v2,v3,d1,d2=comprobarcubo(cubo)
        if es == True:
            return cubo, h1,h2,h3,v1,v2,v3,d1,d2
        else:
            print cubo,h1,h2,h3,v1,v2,v3,d1,d2
            if "si" == raw_input("Qieres seguir:"):
                cuadro_magico()
            else:
                return "Ha salido"



#print cuadro_magico()


'''El assert es una instruccion de python que te permite definir
condiciones que deban cumplirse siempre.  En caso que la expresion
booleana sea True assert no hace nada y en caso de False dispara
una excepcion.
zip (seq1, ...)
Esta función devuelve una lista de tuplas, donde cada tupla contiene
 el i-ésimo elemento de cada una de las secuencias de argumento.
 Se requiere al menos una secuencia, o se lanzará TypeError.
 La lista devuelta se trunca a la longitud de la secuencia de argumento más corta.
 Cuando hay múltiples secuencias de argumento de la misma longitud,
 zip() es similar a map() con un argumento inicial de None.
 Con una sola secuencia como argumento, devuelve una lista de tuplas de un solo elemento.
>>> nombres = "Jorge", "Ricardo", "Carlos"
>>> apellidos = "Gonzalez", "Medina", "Pedro"
>>> edades = 30, 25, 41
>>>
>>> for nombre, apellido, edad in zip(nombres, apellidos, edades):
...     print("%s %s: %d." % (nombre, apellido, edad))
...
Jorge Gonzalez: 30.
Ricardo Medina: 25.
Carlos Pedro: 41.
'''
from math import log10

def ecm_benford(medida):
    ideal=[]
    for n in range(1,10):
        ideal.append(log10(n+1) - log10(n))
    return ecm(medida, ideal)

def ecm(x,y):
    sum=0
    if (len(x) == len(y)):
        for xi,yi in zip(x,y):
           sum += (xi - yi)**2
    return  sum/len(x)

print ecm_benford((1,0,0,0,0,0,0,0,0))

def buridan(a,n):
    if n == 1:
        return a
    if n%2 == 0:
        return buridan(a,n-1)/2
    return (1+buridan(a,n-1))/2

print [buridan(0.1, n) for n in range(1,20)]

'''
permutations()	p[, r]	r-length tuples, all possible orderings, no repeated elements
permutations('ABCD', 2)	 	AB AC AD BA BC BD CA CB CD DA DB DC
'''

from itertools import permutations

def es_solucion(p):
    l = p + (p[0],)
    sum = 0
    sol=[]
    for i in (0,3,6):
        for j in l[i:i + 4]:
            sum += j
        sol.append(sum)
    for k in sol:
        if k != 20:
            return False
    return True

def es_solucion(p):
    l = p + (p[0],)
    return all(20 == sum(l[i:i+4]) for i in (0,3,6))

def triangulo_numerico():
    for p in permutations(range(1,10)):
        if es_solucion(p):
            return p
    raise ValueError('No hay solución')


print triangulo_numerico()