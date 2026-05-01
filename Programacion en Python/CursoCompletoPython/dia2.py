
#bucle determinista determinado Inicio y Fin - Tipo de incremento
# range(10)
# range(2,10)
# range (2,10,2)
for i in range(10):
    print(i, end=" ")
print()

for i in range(2,10):
    print(i, end=" ")
print()
for i in range (2,10,2):
    print(i, end=" ")
print()

cadena = "Hola Mundo!"

for i in range(len(cadena)):
    #print(i, end=" ") posiciones
    print(cadena[i], end="")# valores

print(cadena[0])
print(cadena[1])
print(cadena[-1])
print(cadena[-2])
print(cadena[-3])

