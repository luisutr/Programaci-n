__author__ = 'luisutrilla'

def matriz():
    matriz = []
    filas = int(raw_input("Cantidad de Filas: "))
    columnas = int(raw_input("Cantidad de Columnas: "))
 
    for i in range(filas):
        tmp = []
        for j in range(columnas):
            elemento = raw_input("Elemento %d,%d : " % (i,j) )
            tmp.append(elemento)
        matriz.append(tmp)

    print matriz
    return matriz    #retornamos

matriz()


palabas=["ingeniero", "industrial"]