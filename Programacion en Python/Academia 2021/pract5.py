def multiplica_lista(x, y):
    lista = []
    for i in range(len(x)):
        lista.append(x[i] * y[i])
    return lista

def ajuste_lineal(y):
    # x=[i for i in range(len(y))]
    # Definimos la lista vacia inicialmente
    lista_x = list(range(len(y)))
    # Definimos la lista x
    suma_x = sum(lista_x)
    suma_y = sum(y)
    suma_xy = sum(multiplica_lista(lista_x, y))
    suma_x2 = sum(multiplica_lista(lista_x, lista_x))
    n = len(y)
    # Calculamos a
    a = (suma_xy - ((suma_x * suma_y) / n)) / ((suma_x2) - ((suma_x ** 2) / n))
    b = (suma_y - a * (suma_x)) / n
    return a, b
# Llamada a la funcion
print(ajuste_lineal([1, 1.1, .9, 1, 1.1, .9, 1.1]))

def movmean(x, n):
    s=[x[0]/n]
    for i in range(len(x)+1-n):
        suma=0
        for j in range(i,i+n):
            suma += x[j]
        s.append(suma/n)
    return s
print(movmean([1, 4, 0, 2, 0, 0, 6, 0, 0, 0], 2), (0, 2, 2, 1, 1, 0, 3, 3, 0, 0))


def detrend(y):
    y_nueva = []
    y_recta = []
    y_final = []

    a, b = ajuste_lineal(y)

    lista_x = list(range(len(y)))

    for i in lista_x:
        y_recta.append((a * i) + b)

    # y=a*x+b
    # Restamos señales
    for posicion in range(len(y)):
        y_final.append(y[posicion] - y_recta[posicion])

    return y_final


# Llamada a la función
print(detrend([1, 1.1, .9, 1, 1.1, .9, 1.1]))