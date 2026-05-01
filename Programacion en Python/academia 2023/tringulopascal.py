
def trianguloPascal(n):
    # creamos una lista que contendra los dos primeras lineas
    triangulo = [[1],[1,1]]
    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,n):
        # inicializamos la linea
        linea = [1]
        # bucle por cada uno de los valores de la anterior linea
        for j in range(0,len(triangulo[i])-1):
            # añadimos a la lista los nuevos valores
            # sumamos el valor de la lista anterior con el siguinte
            #linea.extend([ lista[i][j] + lista[i][j+1] ])
            linea.append(triangulo[i][j] + triangulo[i][j+1])
        # añadimos el ultimo valor a la nueva linea
        # siempre es un 1 igual que el primero
        #linea += [1]
        linea.append(1)
        # añadimos la linea a la lista
        triangulo.append(linea)
    #devolvemos la lista ya creada
    return triangulo

print(trianguloPascal(10))


def factotial(n):
    fact=n
    for i in range(n-1,0,-1):
        fact*=i
    return fact
print(factotial(4))

def factotial2(n):
    fact=n
    for i in range(1,n):
        fact*=i
    return fact
print(factotial2(4))