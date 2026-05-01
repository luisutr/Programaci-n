__author__ = 'Luis'

def eliminariguales(matriz):
    for i in range(len(matriz)):
        fila=matriz[i]

def proporcionales(matriz):
    aux=[]
    for i in range(len(matriz)):
        fila = matriz[i]
        for j in range(len(matriz)):
            flag=0
            if i != j:
                filasig=matriz[j]
                for x in range(len(fila)):
                    try:
                        #No es realmente lo que tiene que hacer
                        if filasig[x] % fila[x]==0:
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

def triangular(matriz):
    for nfila in range(len(matriz)):
        pivote = pivotar(matriz,nfila)
        for xfilas in range(len(matriz)):
            if xfilas>nfila:
                hacerceros(matriz,pivote,nfila,xfilas)

def hacerceros(matriz,pivote,nfila,xfilas):
    fila=matriz[xfilas]
    for k in range(len(fila)):
        fila[k] -= pivote[k]*fila[k]

def pivotar(matriz, nfila):
    pivote = matriz[nfila]
    for h in range(len(pivote)):
        pivote[h] = pivote[h]/pivote[nfila]
    return pivote


def rango(matriz):
    matriz = proporcionales(matriz)
    #....
    triangular(matriz)
    return matriz

