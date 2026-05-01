def recorrervalores(cadena):
    for i in cadena:
        print(i)


recorrervalores("Luis")

def recorrerentero(num):
    cadena = str(num)
    for i in num:
        print(i)


mensaje = "1:2:4:2,4,5,6:2,5,3,6"


def dalavuelta(num):
    cadena = str(num)
    cadena = cadena[::-1]
    return int(cadena)

print(dalavuelta(1998))


lista = ["a","b","c","d"]

print(lista[0])
print(lista[1])
print(lista[3])
print(lista[-1])
print(lista[-2])

for i in [0,1,2,3]:
    print(lista[i])

for i in range(len(lista)-1):
    print(lista[i],lista[i+1])

print(list(range(3)))
print(list(range(3,9)))
print(list(range(3,12,2)))
print(list(range(len(lista)-1,-1,-1)))

def dalavueltados(num):
    cadena=str(num)
    inverso=""
    for i in (range(len(cadena) - 1, -1, -1)):
        inverso+=cadena[i]
    return int(inverso)

print(dalavueltados(1999))


# es oscilante si es tal como: 231427
# va un numero menor lueggo mayor...
#va un numero mayor, luego menor, luego mayor...