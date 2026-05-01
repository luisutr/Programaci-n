variablecadena = "abc"
for posicion, valor in enumerate(variablecadena):
    if valor != "a":
        print(str(posicion) + ":" + valor)

#valores
#-------
variablecadena = ["a", "b", "c"]
for mivariable in variablecadena:
    if mivariable != "a":
        print(mivariable)

#posiciones
#----------
variablecadena = ["a", "b", "c"]
for posicion, valor in enumerate(variablecadena):
    if valor != "a":
        print(str(posicion) + ":" + valor)


tupla =(1,2)

lista=[1,2]
lista.append(3)
lista.insert(0,0)
lista.pop(0)
print(lista)
