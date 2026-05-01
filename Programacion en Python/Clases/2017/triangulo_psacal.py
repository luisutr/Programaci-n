# -*- coding: utf-8; mode: python -*-

def triangulo_pascal(n):
    #casos base especiales para el 0 y el 1
    if n == 0:
        return []

    if n == 1:
        return [[1]]
    #para cualquier otro valor
    #hace una recursividad del valor menos 1
    #y otro con la unidad
    triangulo1 = triangulo_pascal(n-1)
    triangulo2 = [1]
    #recorre al valor menos uno
    #anadiendo a t2 la formula que da el siguiente elemento de haber hecho la recursividad

    for i in range(1, n-1):
        triangulo2.append(triangulo1[n-2][i-1] + triangulo1[n-2][i])
    #finalmente mete los valores 1 de las sublistas como se ve en el ejemplo
    triangulo2.append(1)
    #guarada cada recursividad en la lista general y lo devuelve
    triangulo1.append(triangulo2)
    return triangulo1

# mostramos el resultado
resultado = triangulo_pascal(5)
for i in resultado:
    print (i)


# función para el calculo de pascal
# tiene que recibir el numero de lineas que tendra
def triangulo(n):

    # creamos una lista que contendra los dos primeras lineas
    lista = [[1],[1,1]]

    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,n):

        # inicializamos la linea
        linea = [1]

        # bucle por cada uno de los valores de la anterior linea
        for j in range(0,len(lista[i])-1):

            # añadimos a la lista los nuevos valores
            # sumamos el valor de la lista anterior con el siguinte
            #linea.extend([ lista[i][j] + lista[i][j+1] ])
            linea.append(lista[i][j] + lista[i][j+1])

        # añadimos el ultimo valor a la nueva linea
        # siempre es un 1 igual que el primero
        #linea += [1]
        linea.append(1)

        # añadimos la linea a la lista
        lista.append(linea)

    #devolvemos la lista ya creada
    return lista


def triangulo_pascal2():
    try:
        n = int(input("Numero de lineas para triangulo de Pascal: "))
        resultado = triangulo(n)
        L = [' '.join([str(i) for i in x]) for x in resultado]
        for s in L:
            espacios = (len(L[-1])-len(s))//2
            print(' '*espacios + s)
    except:
        print ("\nTiene que ser un valor numerico")

#triangulo_pascal2()
