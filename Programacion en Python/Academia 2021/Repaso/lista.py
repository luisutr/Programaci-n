numero = 2021

cadena = str(numero)

[2,0,2,1]

resultado = [1,2,0,2]


def dalavuelta(numero):
    # declaracion de variable
    lista = []
    #dar la vuelta al numero
    cadena = str(numero) #cadena = "2021"
    #print("Solucion 1: list(reversed(cadena))")
    #print(list(reversed(cadena)))
    for i in cadena:
        lista.append(i)
    # lista = [2,0,2,1]
    #devuelvo la solucion
    #print("Solucion 2: lista[::-1]")
    #print(lista[::-1])
    print("Solucion 3: list(reversed(lista))")
    return list(reversed(lista))

print(dalavuelta(2021))

print(list(range(9,-1,-1)))

#Dar la vuelta a una lista
resultado = [2, 0, 2, 1]
#            0,1,2,3
print(len(resultado))
print(resultado[3])
lista = []
for i in range(len(resultado)-1,-1,-1): #3,2,1,0
    lista.append(resultado[i])
print(lista)