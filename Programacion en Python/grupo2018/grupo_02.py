import math

def lista_a_tupla(slgen1):
    nlineas = math.sqrt(len(slgen1[0]))
    aux=0
    matrizresul=[]
    for sublista in slgen1:
        subresul=[]
        tupla=[]
        for elemento in sublista:
            if aux < 3:
                tupla.append(elemento)
                aux += 1
            else:
                subresul.append(tuple(tupla))
                aux = 0
                tupla = []
                tupla.append(elemento)
                aux = 1
        subresul.append(tuple(tupla))
        matrizresul.append(tuple(subresul))
    return matrizresul

print(lista_a_tupla([[1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,1]]))

