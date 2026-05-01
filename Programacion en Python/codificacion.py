def print_r(matriz):
    for fila in matriz:
        print fila


def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in xrange(rows)] for i in xrange(cols)]

def codificar(cadena):
    lista=[]
    j=0
    for i in range(0,len(cadena),5):
        count = 5
        subcadena=[]
        while count > 0 and j < len(cadena):
                subcadena.append(cadena[j])
                j+=1
                count -= 1
        lista.append(subcadena)

    return transpuesta(lista)


print codificar("ARNRAN U RSTM5TW0B E EP B")

