'''
La Criba de Eratóstenes es un algoritmo capaz de identificar los números primos en un conjunto. Para ello:
Se inicia el proceso con un conjunto de números, desde 2 hasta "n" (por ejemplo del 2 al 10).
Iniciando desde n = 2: Se tachan (eliminan) todos sus múltiplos en el conjunto original.
Se repite el proceso con n = 3, tachando sus múltiplos, y así sucesivamente hasta que n alcance al número superior del rango original, deteniendo el algoritm
'''


def criba_eratostenes(n):
    primos = []
    no_primos = []

    for i in range(2, n + 1):
        if i not in no_primos:
            primos.append(i)

            for j in range(i * i, n + 1, i):
                no_primos.append(j)

    return primos   


print(criba_eratostenes(120))