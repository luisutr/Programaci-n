#!/usr/bin/env python
# -*-coding:utf-8-*-

#Archivo mochila.py
#Contiene la implementaci�n de la soluci�n por programaci�n din�mica
#Sea n objetos no fraccionables de pesos pi y beneficios bi.
# El peso máximo que puede llevar la mochila es capacidadW.
# Queremos llenar la mochila con objetos, tal que se maximice el beneficio.


def mochila(w,p,capacidadW):
    T = combinaciones(w,capacidadW)
    for c in range(capacidadW+1):
      T[0][c]=0
    for j in range(1,len(w)+1):
      for c in range(capacidadW+1):
        if c >= w[j-1]:
            T[j][c]=max(T[j-1][c],T[j-1][c-w[j-1]]+p[j-1])
        else:
            T[j][c]=T[j-1][c]
    for i in range(len(w)+1):
        print (T[i])



# w Elementos
# p Pesos de los elementos
# capacidadW Capacidad de elementos de la mochila
# T Un arreglo que considera todas las posibilidades de rellenar de elementos la mochila dispuestos a 0
# imagna filas y columnas

def combinaciones(w,capacidadW):
    T=[]
    for i in range(len(w)+1):
      ea_row = []
      for j in range(capacidadW+1):
        ea_row.append(0)
      T.append(ea_row)
    return T


mochila([5,7,4,3] ,[8,11,6,4],14)
