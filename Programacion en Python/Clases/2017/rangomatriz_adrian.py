def rango_matriz(matriz):
    return len(filas_no_nulas(escalonar(matriz)))


def filas_no_nulas(m):
    return [f for f in m if f != [0] * len(f)]


from copy import deepcopy


def escalonar(A):
    A = deepcopy(A)
    for j in range(len(A)):
        if j < len(A[j]):
            elegir_fila(A, j)
            normalizar_fila(A[j], j)
            reducir_desde_fila(A, j)
    return A


def elegir_fila(A, j):
    for i in range(j, len(A)):
        if A[i][j] != 0:
            A[i], A[j] = A[j], A[i]
    return A


def normalizar_fila(fila, j):
    for i in range(j, len(fila)):
        try:
            fila[i] /= fila[j]
        except ZeroDivisionError:
            return None



def reducir_desde_fila(A, j):
    for i in range(j + 1, len(A)):
        reducir_fila(A[i], A[j], j)


def reducir_fila(fila, pivote, j):
    for i in range(j, len(fila)):
        fila[i] -= pivote[i] * fila[j]


print(rango_matriz([[1, 2, 1], [1, 1, 1], [1, 2, 2], [1, 2, 0]]))