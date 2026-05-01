def sacamaxdegrafo(L):
    maximo = 0
    for puntos in L:
        for i in puntos:
            if i > maximo:
                maximo = i
    return maximo

def creamatrizcuadrada(n):
    matriz = []
    for i in range(n+1):
        fila=[]
        for j in range(n+1):
            fila.append(0)
        matriz.append(fila)
    return matriz


def eliminafilasceros(m):
    matriznueva = []
    #me guardo las filas que no sean enteras de 0
    for fila in m:
        if sum(fila) != 0:
            matriznueva.append(fila)
    return matriznueva

def hacecopiamatriz(m):
    x = []
    for i in m:
        fila=[]
        for j in i:
            fila.append(j)
        x.append(fila)
    return x

def eliminacolumnasceros(matriz):
    m = hacecopiamatriz(matriz)
    # miro si la clumna esta llena de ceros
    for columna in range(len(matriz)):
        sum = 0
        for e in range(len(matriz)):
            sum += matriz[e][columna]
        # elimino elemenrtos de cada fila, osea!! columna
        if sum == 0:
            for i in range(len(matriz)):
                if len(matriz) == len(m):
                    m[i].pop(columna)
                else:
                    m[i].pop(columna-1)
    return  m


print(eliminacolumnasceros([[0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0]]))