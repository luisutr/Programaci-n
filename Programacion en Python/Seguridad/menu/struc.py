__author__ = 'luis'
# -*- coding: utf-8; mode: python -*-

import os

def setA(struct, a):
    struct[0] = a
def getResult(struct):
    return struct[2]
def setB(struct, b):
    struct[1] = b
def getResult(struct):
    return struct[2]
def setResult(resultado):
    struct = [0,0,0]
    struct[2] = resultado
def suma(lista):
    op=lista.pop(0) # Quitamos la opcion
    N = lista.pop(0) #Guardamos el valor de N
    sumatorio = 0
    for i in range(int(N)):
        sumatorio += int(lista[i])
    return str(sumatorio)

def ejecutar(r):
    os.system("ls > listado.txt")


    #EJECUTAR UN COMANDO WINDOWS O MAC y como diferenciar en que sistema estoy