def colocar_sistema(A,B):
    for i in range(len(A)):
        ecuacion=A[i]
        aux=B.pop(0)
        ecuacion.append(aux)
        A[i]=ecuacion
    return A

def lin_solve(A,B):
    A=colocar_sistema(A,B)
    A=escalonar(A)
    A=list(reversed(A))
    aux=[]
    for i in range(len(A)):
        aux.append(list(reversed(A[i])))
    C=escalonar(aux)
    return C

def trasponer(A):
    traspuesta=[]
    for i in reversed(A):
        fila = i
        aux=[]
        for j in reversed(fila):
            aux.append(j)
        traspuesta.append(aux)
    return traspuesta

def escalonar(A):
   # A = deepcopy(A)
    for j in range(len(A)):
        if j< len(A[j]):
            fila_pivote(A,j)
            #elegir_fila(A, j)
            normalizar_fila(A[j], j)
            combinacion_lineal(A[j],j)
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
            pass
def combinacion_lineal(fila ,j):
    for i in range(j, len(fila)):

            pass

def reducir_desde_fila(A, j):
    for i in range(j + 1, len(A)):
        reducir_fila(A[i], A[j], j)


def reducir_fila(fila, pivote, j):
    for i in range(j, len(fila)):
        fila[i] -= pivote[i] * fila[j]

def fila_pivote(m, posicion):
    for i in range(len(m)):
        if m[0][posicion] == 0:
            aux=m.pop(posicion)
            m.insert(0,aux)
    return m


print escalonar([[1,0,0], [0,1,0], [0,0,1]])
#3
print escalonar([[1,1,1], [1,1,1], [1,0,2]])
#2
print escalonar([[1,1], [1,1]])


print trasponer([[1,2,3],[0,2,4],[0,0,5]])
