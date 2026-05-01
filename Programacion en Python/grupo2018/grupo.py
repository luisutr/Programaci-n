# -*- coding: utf-8; mode: python -*-

from gauss import *

gen1 = [ [[1,0,0], [0,0,0], [0,0,0]], [[0,0,0], [0,1,0], [0,0,0]], [[0,0,0], [0,0,0], [0,0,1]] ]
gen2 = [ [[0,0,0], [0,1,0], [0,0,0]], [[0,0,0], [0,1,0], [0,0,1]]]

"""Para que sea una base los vectores deben ser linealmente independientes, el número de vectores debe coincidir
con la dimensión del subespacio, y cualquiera de los vectores del sistema generador debe poderse expresar como
combinación lineal de los vectores de la base."""
def es_base(generador, base):
    # intenta rellenar esta función con ayuda de la solución del curso anterior
    return True

def implicitas(gen):
    # completa esta función aprovechando la solución del curso anterior
    return []


implicitas_interseccion = implicitas(gen1) + implicitas(gen2)

def parametricas(impl):
    # completa esta función aprovechando la solución del curso anterior
    return []

def union(gen1, gen2):
    un = gen1
    un+=gen2
    return un

"""[ ((1,0,0), (0,0,0), (0,0,0)), ((0,0,0), (0,1,0), (0,0,0)), ((0,0,0), (0,0,0), (0,0,1)) ]"""


def triangular (Matriz):
    a = Gauss(Matriz).diag()
    return a.A

def interseccion(gen1, gen2):
    return []

"""[ ((0,0,0), (0,1,0), (0,0,0)), ((0,0,0), (0,0,0), (0,0,1)) ]"""

def union(gen1,gen2):
    matriz=[]
    basegen1=[]
    basegen2=[]
    for i in gen1:
        elemento = i
        fila=[]
        for j in elemento:
            fila+=j
        matriz.append(fila)
        basegen1.append(fila)
    for i in gen2:
        elemento = i
        fila=[]
        for j in elemento:
            fila+=j
        matriz.append(fila)
        basegen2.append(fila)
    return matriz, basegen1, basegen2

matriz,basegen1, basegen2 = union(gen1,gen2)

print "UNION:"
print matriz
print "GEN1:"
print basegen1
print "GEN2:"
print basegen2
#gen1.extend(gen2)
#print gen1

#base de la una
print "BASE DE LA UNION:"
triangulada = triangular(matriz)
print triangulada
print rango_matriz(triangulada)

#implicitas: triangulos los dos sistemas gen
print "BASE DE LOS SG PARA CALCULAR IMPLICITAS: "
basegen1 = triangular(basegen1)
basegen2 = triangular(basegen2)

print basegen1
print basegen2

#luego para los generadores indepenpendiente ...
#antes de hacer la transpuesta debemos añadir la matriz de 0 con la diagonal de 1
def generarmatrizdiagonal(gen):
    dimension = len(gen[0])
    matrizdiagonal=[]
    for i in range(dimension):
        fila=[]
        for j in range(dimension):
            if i == j:
                fila.append(1)
            else:
                fila.append(0)
        matrizdiagonal.append(fila)
    return matrizdiagonal
print "MATRIZ DIAGONAL BG1"
matrizdiagonal = generarmatrizdiagonal(basegen1)
print matrizdiagonal

def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in xrange(rows)] for i in xrange(cols)]

trasgen1=transpuesta(basegen1)
trasgen2=transpuesta(basegen2)

print "TRANSPUEST BG1:"
print trasgen1


def unionx(trasgen1,matrizdiagonal):
    m=[]
    for i in range(len(trasgen1)):
        m.append(trasgen1[i]+matrizdiagonal[i])
    return m

print "SISTEMA IMP BG1"
sistemaparaimplicitas = unionx(trasgen1,matrizdiagonal)
print sistemaparaimplicitas

print "IMPLICITAS BG1"
print triangular(sistemaparaimplicitas)
print rango_matriz(sistemaparaimplicitas)

#Interseccion: los dos resultados de las implicitas de los sg los convierto en filas uno los dos sistemas y triangulo




#print lin_solve([1,0,3,-2],[2,2,1,-2])

