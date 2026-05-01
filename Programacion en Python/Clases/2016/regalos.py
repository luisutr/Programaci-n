__author__ = 'luisutrilla'

#!/usr/bin/env python
# -*-coding:utf-8-*-

lista_resultados = []

def combinacion(combinar, precios):
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
        pto = precios.index(x[len(x) - 1])
        # Hace que el nuevo elemento agregado de "Lista", sea el siguiente en posicion del ultimo caracter del elemento "combinar"
        for j in range(pto, len(precios)):
            # para cada elemento de 'lista' desde el elemento "lista" que hace parte del ultimo caracter del elemento de "combinar" hasta el ultimo elemento de'lista'
            if precios[j] not in x and precios[len(precios) - 1] not in x:
            # Si el elemento de "lista" no esta en el elemento "combinar" y ademas el elemento "lista" no es el ultimo caracter del elemento "combinar"
                new_comb.append(str(x) + "," + str(precios[j]))  # Agrega a una nueva lista la combinacion
        lista_resultados.append(new_comb)
    print new_comb
    print "+++++++++++++++++++++++++++++++++++++++++++++++++"
    return new_comb  # Esta nueva lista se utilizara como parametro al llamar de nuevo la funcion...

print "COMBINACIONES"
print "++++++++++++++"
#combinacion(combinacion(combinacion(combinacion(precios, precios), precios), precios),precios)
#  Llamo la funcion asi misma y me permite organizar una nueva lista cada vez y usarla como parametro (este es el truco!)


def regalos(precios, n, dinero):
    combinacion(combinacion(combinacion(combinacion(precios, precios), precios), precios), precios)
    lista_posibles = []
    for i in range(len(lista_resultados)):
        posibles = lista_resultados[i]
        for k in range(len(posibles)):
            posible = posibles[k]
            lista_posible = posible.split(",")
            if len(lista_posible) == n:
                suma = 0
                for j in lista_posible:
                    suma = int(j) + suma
                if suma <= dinero:
                    lista_posibles.append(lista_posible)
    return lista_posibles


print regalos(["2","5","1","3"],2,8)