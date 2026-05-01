def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]

map(doblar, numeros)
#Facilmente podemos transformar este iterable en una lista:

print(list(map(doblar, numeros)))