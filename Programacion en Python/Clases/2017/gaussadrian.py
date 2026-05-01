# -*- coding: utf-8; mode: python -*-

def rango_matriz(matriz):
    return len(filas_no_nulas(escalonar(matriz)))


def filas_no_nulas(m):
    return [f for f in m if f != [0] * len(f)]


from copy import deepcopy


def escalonar(A):
    A = proporcionales(A)
    A = deepcopy(A)
    print('original', A)
    for i in range(len(A)):
        elegir_fila(A, i)
        print ('escalonar',A)
        normalizar_fila(A[i], i)
        print ('normalizar',A)
        reducir_desde_fila(A, i)
        print('reducir', A)
    return A

def proporcionales(matriz):
    aux = []
    for i in range(len(matriz)):
        fila = matriz[i]
        for j in range(len(matriz)):
            flag = 0
            if i != j:
                filasig=matriz[j]
                for x in range(len(fila)):
                    try:
                        if filasig[x] % fila[x] == 0.0:
                            if x == 0:
                                dividendo = filasig[x] // fila[x]
                                flag += 1
                            elif dividendo == filasig[x] // fila[x]:
                               flag += 1
                    except ZeroDivisionError:
                        pass
                if flag == len(fila):
                    if j not in aux:
                        aux.append(j)
    aux.sort()
    aux.reverse()
    for z in aux:
        matriz.pop(z)
    return matriz

def elegir_fila(A, j): #ESTA FUNCIÓN FALLA EN MATRICES DE 2X3(MÁS COLUMNAS QUE FILAS)
    for i in range(j, len(A)):
        if A[i][j] != 0:
            A[i], A[j] = A[j], A[i]
            return
        if A[i][j] == 0:
            print('fila elegida', i, A)
            #return A[i][j]


def normalizar_fila(fila, j):
    aux = fila[j]
    for i in range(j, len(fila)):
        try:
            fila[i] /= aux
        except ZeroDivisionError:
            pass

#ELECCIÓN DESDE LA FILA QUE SE QUIERE REDUCIR
def reducir_desde_fila(A, j):
    for i in range(j + 1, len(A)):
        reducir_fila(A[i], A[j], j)
        print('fila', i, A)

#REDUCCIÓN DE LA FILA ELEGIDA
def reducir_fila(fila, pivote, j):
    primero = fila[j]
    for i in range(j, len(fila)):
        fila[i] -= (pivote[i] * primero)
        print('elem',i,fila, pivote[i] * fila[j])

print rango_matriz([[2,4,6],[4,5,6],[4,8,12]])
print rango_matriz([[1,0,0], [0,1,0], [0,0,1]])
#3
print rango_matriz([[1,1,1], [1,1,1], [1,0,2]])
#2