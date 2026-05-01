#calculas las filas del triangulo y las guarda como listas
def triangulopascal(h):
    trinangulo = []
    lista = [1,1]
    for n in range(h):
        #nueva linea del triangulo, tendra tantas lineas como indique h
        nueva = []
        #hago un bucle de tantas posiciones como necesite en la linea, eso me lo indica n (la linea en la que estoy)
        # como el primer valor es 0 --> no hace bucle concatena 1 ()linea 13 e imprime
        # en la siguiente como tiene 1, solo posicion 0 -> bucle de i = 0 y concatena 1 sale del bucle y concatena el otro 1 e imprime
        # ahora ya tiene 2 [0,1] --> 12  y luego sale y concatena el 1 del final e imprime
        #...
        for i in range(n):
            if i == 0:
                nueva.append(lista[i])
            else:
                nueva.append(int(lista[i-1])+int(lista[i]))
        # el uno del final de la linea
        nueva.append(1)
        trinangulo.append(nueva)
        lista = nueva
    return trinangulo

# funcion que recoge las filas del tringulo como listas y las imprime según la imgen del triangulo
def imprimetringulo(h):
    triangulo = triangulopascal(h)
    #recorro por posiciones para saber en que lienea estoy, porque así puedo calcular cuantos espacios tengo que meter
    for i in range(len(triangulo)):
        fila=""
        linea = triangulo[i]
        for elemento in linea:
            fila+=str(elemento)+" "
        # se que tengo que meter h espacios, menos el numero de fila, menos 1 porque esa posicion la ocupa el primer numero de la fila
        print(" "*(h-1-i)+fila)

##imprimetringulo(5)


def arbol (altura_copa,ancho_tronco):
    if altura_copa%2 != 0:
        altura_copa+=1
    for i in range(1, altura_copa + 1):
        print (" " * (altura_copa - i) + "*" * (2 * i - 1))
    for x in range(3):
        print(' '*((altura_copa)-(ancho_tronco//2))   + '*'* ancho_tronco )

arbol (15,4)
