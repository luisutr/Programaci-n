__author__ = 'luisutrilla'
# -*- coding: utf-8 -*-

def elemcon(lista, entero):
    existe = ""
    for i in range(len(lista)):
        if lista[i] == entero:
            print i,
            existe = True

    if existe != True:
        print 0


def convolucion(listauno, listados, entero):
    existe = ""
    lista = []

    for i in range(len(listauno)):
        lista.append(listauno[i] * listados[i])

    for i in range(len(lista)):
        if lista[i] == entero:
            print i,
            existe = True

    if existe != True:
        print 0


# convolucion([2,1,4,5],[3,6,5,1],2)

def convo(listauno, listados):
    lista = []
    for i in range(len(listauno)):
        for j in range(len(listados)):
            lista.append((float(lista[i + j] + listauno[i] * listados[j])))

    return lista


# print convo([2,1,4,5],[3,6,5,1])

# primera duda
def cifras(n):
    lista = []
    for i in (n):
        lista.append(i)
    return lista


# print cifras([1,9,5,4])

# segunda duda
def entrar():
    usuario = raw_input("usuario: ")
    clave = int(input("clave: "))
    if usuario == 'jaime' and clave == 1501:
        return True
    else:
        return False


# print entrar()


def recorrer_cadena():
    lista = []
    for i in "programas ":
        lista.append(i)
    return lista


def codigo_cesar(cadena):
    lista = []
    for j in (cadena):
        lista.append(j)
    for i in range(3, len(cadena)):
        valor = cadena[i]
        """ insert añade donde le de la lista y desplaza"""
        lista.insert(0, cadena[i])
        """ append añade al final de la lista"""
        # lista.append(cadena[i])
        lista.pop()

    return lista


#print codigo_cesar('abcdef')

from math import sqrt
def es_perfecto(num):
    print "el",num,"?"
    suma = 0
    for i in range(1,num):
        if num % i == 0:
            suma += i
    if suma == num:
        return True
    else:
        return False

print "¿Es un umero perfecto",es_perfecto(28)