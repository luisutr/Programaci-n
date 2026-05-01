__author__ = 'propietario'
def pivotar(lista):
    linea1=lista[0]
    if linea1[0]==1 and linea1[0]!=0:
        linea1=linea1
    else:
        linea1 = dividirfila(linea1,linea1[0]) #tendras que tener luego un for que vaya cambiando los valores
    return linea1

def dividirfila(fila, elemento):
    aux=[]
    for i in range(0,len(fila)):
            aux.append(fila[i]/elemento)
    return aux


print(pivotar([ [8.00,2.00,3.00], [0.00,1.00,0.00], [0.00,0.00,1.00] ]))