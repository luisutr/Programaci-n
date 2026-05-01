def restar(fila1, fila2):
    resta=[]
    for i in range(len(fila1)):
        resta.append(fila1[i]-fila2[i])
    return resta
def dividir(fila,posicion):
    division=[]
    for i in range(len(fila)):
        if fila[posicion] != 0:
            division.append(float(fila[i]/float(fila[posicion])))
        if fila[posicion] == 0:
            division.append(fila[i])
    return division
def fila_pivote(m, posicion):
    for i in range(len(m)):
        if m[0][posicion] == 0:
            aux=m.pop(posicion)
            m.append(aux)
    pivote0 = m[0]
    return pivote0
def matriz_pivote(m, posicion):
    for i in range(len(m)):
        if m[0][posicion] == 0:
            aux=m.pop(posicion)
            m.append(aux)
    return m
def multiplicar(fila1,fila2):
    multiplicacion=[]
    for i in range(len(fila1)):
        multiplicacion.append(fila1[i]*fila2[i])
    return multiplicacion

def triangular(m):
    for i in range(len(m)-1):
        fila=m[i+1]
        posiciones=i+1
        for j in range(posiciones):
            pivote=fila_pivote(m,j)
            m[j]=pivote
            fila=restar(pivote,multiplicar(pivote,fila))
            m[i+1]=fila
    print m
    return m

triangular([[1,0,0], [0,1,0], [0,0,1]])
#3
triangular([[1,1,1], [1,1,1], [1,0,2]])
#2
triangular([[1,1], [1,1]])