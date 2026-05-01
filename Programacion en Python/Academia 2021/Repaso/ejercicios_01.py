def es_divisible_por2(n,lista):   #lista tiene los diferentes divisores
    divisible = []
    for d in lista:
        if n%d == 0:
            divisible.append(d)
    return divisible


# print(es_divisible_por2(100,[2,3,5,6,10]))


def paresoimpares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num%2==0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

numeros = [1,2,3,4,5,6,7,8,9]
#print(paresoimpares(numeros))


cadena = "hola mundo 2,45 1995 True Flase"
lista = ["a", 2, [1,2,3, [5,6]], 2.4, "mucho mas larga",["a","b"]]

contador = 0
for i in lista:
    if type(i) == list:
        contador +=1
        for j in i:
            if type(j)== list:
                print("Tengo una sublista")
#print("Tengo tantas listas: "+str(contador))


# repasa texto y mira si las posiciones anteriores a mayusculas tiene ". " si no tienen espacio y punto nos indica en
# una lista las posiciones de donde encontrar estos fallos.


texto = "Hola mundo Esto es una clase de programacion. Hoy es martes Estamos en octubre."

def buscaerrorestexto(texto):
    errores = []
    for i in range(1,len(texto)):
        if texto[i].isupper():
            if texto[i-1] != " " or texto[i-2] != ".":
                errores.append(i)
    return errores

#print(buscaerrorestexto("Hola mundo Esto es una clase de programacion. Hoy es martes Estamos en octubre."))


# Devuelve las vocales pero !! de solo las posiciones impares, devuelve una lista con las posiciones

def buscavalesimpares(texto):
    pos=[]
    vocales = ["a","e","i","o","u"]
    for i in range(len(texto)):
        if i%2 != 0:
            if texto[i] in vocales:
                pos.append((i,texto[i]))
    return pos

print(buscavalesimpares(texto))

#Calcula persistencia
# 256782  si el numero tiene mas de 1 digito --> sumamos sus digitos y dividimos el numero
# el resultado aplicamos lo mismo y si es mayor de 1 digito repetimos la operacion, hasta tener un numero de 1 dgitio
# devuelve un entero numero de itereaciones

def sumadigit(cadena):
    sum = 0
    for i in cadena:
        sum+=int(i)
    return str(sum)

def persistencia(numero):
    numcad = str(numero)
    contador = 0
    while len(numcad) > 1:
        numcad = sumadigit(numcad)
        contador +=1
    return contador, numcad

print(persistencia(256782))
