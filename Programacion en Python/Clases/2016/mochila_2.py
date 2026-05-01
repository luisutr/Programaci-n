#!/usr/bin/env python
# -*-coding:utf-8-*-

def combinacion(combinar, lista):
    """
    Esta funcion combina los elementos de la lista "combinar" con los elementos de la lista
    "Lista"; toma cada elemento de combinar y le adjunta un elemento respectivo de "lista" a menos
    de que el elemento de "Lista" este repetido en el elemento de "combinar" o este en posicion detras del
    ultimo caracter del elemento "combinar"

    PARAMETROS:
        Dos listas
    RETORNO:
        Una lista con la combinacion unica de "combinar" y "lista" sin repetir elementos.
    """
    new_comb = []
    for x in combinar:
        pto = lista.index(x[len(
            x) - 1])  # Hace que el nuevo elemento agregado de "Lista", sea el siguiente en posicion del ultimo caracter del elemento "combinar"
        for j in range(pto, len(
                lista)):  # para cada elemento de 'lista' desde el elemento "lista" que hace parte del ultimo caracter del elemento de "combinar" hasta el ultimo elemento de'lista'
            if lista[j] not in x and lista[len(
                    lista) - 1] not in x:  # Si el elemento de "lista" no esta en el elemento "combinar" y ademas el elemento "lista" no es el ultimo caracter del elemento "combinar"
                new_comb.append(x + lista[j])  # Agrega a una nueva lista la combinacion
    print new_comb
    print "+++++++++++++++++++++++++++++++++++++++++++++++++"

    return new_comb  # Esta nueva lista se utilizara como parametro al llamar de nuevo la funcion...


lista = ["a", "b", "c", "d", "e"]
print "COMBINACIONES"
print "++++++++++++++"
combinacion(combinacion(combinacion(combinacion(lista, lista), lista), lista),
            lista)  # Llamo la funcion asi misma y me permite organizar una nueva lista cada vez y usarla como parametro (este es el truco!)
