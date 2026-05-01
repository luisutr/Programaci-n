# -*- coding: utf-8; mode: python -*-


# Diagonal principal (2 puntos)
# Definir una función traza(m) que devuelve la suma de los elementos de la diagonal principal de la matriz m. La matriz
# m es cuadrada y se representa como una lista de listas. Cada elemento de m es una fila de la matriz.
# Por ejemplo, el resultado de traza([[1,2,3],[4,5,6],[7,8,9]]) debe devolver 15, y el resultado de traza([[1,0,0],[0,1,0],[0,0,1]]) debe devolver 3.



def traza(m):
    subm=[]
    result=0
    for i in range(len(m)):#este bucle for nos recorre nuestra "lista grande" y sus posiciones guardandola en
        #nuestra variable subm
        subm=m[i]
        result+=subm[i]
    return result
