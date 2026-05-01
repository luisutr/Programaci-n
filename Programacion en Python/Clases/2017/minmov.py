# -*- coding: utf-8; mode: python -*-
"""Empiezas con 1€ y, con cada movimiento, puedes o bien doblar tu dinero o sumar otro euro.
¿Cuál es el mínimo número de movimientos para obtener exactamente 200€?
Escribe una función minmov que acepta como único argumento la cantidad objetivo (en nuestro ejemplo 200)
y devuelve el mínimo número de movimientos necesarios para obtener exactamente esa cantidad."""



def minmov(dinero):
    contador = 0
    resto = 0
    if dinero>1:
        dinero, resto, contador = movimientos_dobles(dinero,resto, contador)
    dinero = dinero + resto
    while dinero>0:
        dinero -= 1
        contador += 1
    return contador

def movimientos_dobles(dinero,resto, contador):
    resto += dinero%2
    dinero = dinero/2
    dinero = int(dinero)
    contador += 1
    if dinero>1:
        return movimientos_dobles(dinero,resto, contador)
    else:
        return dinero, resto, contador


print minmov(200)  #si metes 200 en minimo es 10
print minmov(300) #si metes 300 en minimo es 12
print minmov(3000) #si metes 3000 en minimo es 18
