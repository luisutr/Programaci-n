cadena = "   esto es cadena    "

lista = [1,2,3,4]


print(cadena[1:])

# METOS CADENAS

print(cadena.split(" "))
print(cadena.count("a"))
print(cadena.index("e"))
print(cadena.upper())
print(cadena.strip(" "))
print(cadena)
print(cadena.find("e"))

print(cadena.find("xxxxx"))
print("".join(list(reversed(cadena))))

#METODOS DE LISTAS
lista.append(5)
lista.pop(0)
print(lista)
lista = list(reversed(lista))
lista.insert(0,0)
print(lista)
print(sorted(lista))

