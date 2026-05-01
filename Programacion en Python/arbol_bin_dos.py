def insertarDerecho(arbol,nodo):
    arbol[2]=[nodo, None, None]
    return arbol
def insertarIzquierdo(arbol,nodo):
    arbol[1]=[nodo, None, None]
    return arbol

def inserta_en_arbol_binario(arbol,elem):
    if arbol[0]<elem:
        if arbol[2] == None:
            insertarDerecho(arbol,elem)
            #si no quiero tener tantas funciones
            #arbol[2]= [elem, None, None]
        else:
            inserta_en_arbol_binario(arbol[2],elem)
    else:
        if arbol[1] == None:
            insertarIzquierdo(arbol,elem)
            #arbol[1]=[elem, None, None]
        else:
            inserta_en_arbol_binario(arbol[1], elem)
    return arbol


def convierte_arbol_a_tuplas(arbol):
    if arbol[0]!=None:
        if type(arbol[2]) == list:
            arbol[2]=convierte_arbol_a_tuplas(arbol[2])
        if type(arbol[1]) == list:
            arbol[1]=convierte_arbol_a_tuplas(arbol[1])
    arbol = tuple(arbol)
    return arbol

def delistasatuplas(arbol):
    for i in range(len(arbol)):
        if type(arbol[i]) == list:
            arbol[i] = tuple(arbol[i])
             #delistasatuplas(arbol[i])
    return tuple(arbol)


def arbol_binario(lista):
    if lista != []:
        lista = list(lista)
        arbol = [lista[0], None, None]
        for i in range(1,len(lista)):
            arbol = inserta_en_arbol_binario(arbol,lista[i])
        #print(arbol)
        #arbol = convierte_arbol_a_tuplas(arbol)
        arbol = delistasatuplas(arbol)
        return arbol
    return None



print(arbol_binario([3, 8, 1, 13, 5, 9]))
#(3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None)))
#print(arbol_binario(range(5)))
# (0, None, (1, None, (2, None, (3, None, (4, None, None))))))
#print(arbol_binario(list(reversed(range(5)))))
#(4, (3, (2, (1, (0, None, None), None), None), None), None))
#print(arbol_binario([]), None)

