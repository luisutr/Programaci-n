cadena = "pepitogrillo, otro, otra"
print(cadena.split(","))
cadena = cadena.replace(", ", ',')
print(cadena)
print(cadena.split(","))

lista = []
nombres = "Luis, Elena, Lucia, Juan, Pedro, Antonio"
nombres = nombres.replace(", ", ",")
#convierte a lista un string pegando cortes en el caracter delimitador dado
lista = nombres.split(",")
for i in range(len(lista)):
    if lista[i] == "Elena":
        print("Encontrada")
        lista[i] = "Helena"
lista.append("Jose")
lista.insert(0,"Juanma")
print(lista)
lista.pop()
print(lista)
lista.pop(0)
print(lista)
#index nos da la primera posicion de donde esta un elemento
print(lista.index("Helena"))
numeros = [1,5,8,9,0,3,2,6,5,27,22]
print(max(numeros))
print(min(numeros))
print(sum(numeros)/len(numeros))