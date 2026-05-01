


cadena = "Hola mundo"
print("COSAS DE CADENAS")
print("#######################################")
print(cadena[0:5])
print(cadena[8:10])
print(cadena[-1])
print(cadena[-2])
print(cadena[::-1])
print(cadena[2::-1])

print("\nCOSAS DE RANGE")
print("#######################################")
print(list(range(len(cadena))))
print(list(range(1,len(cadena))))
print(list(range(1,len(cadena),2)))
print(list(range(len(cadena)-1,-1,-1)))

print(cadena)
for posicion in range(len(cadena)-1,-1,-1):
    print("posicion: "+str(posicion)+", "+"valor: "+cadena[posicion])


cadena = [1,2,3,4,5,99,-1,"Hola",2.7]
print("\nCOSAS DE LISTAS")
print("#######################################")
print(cadena[0:5])
print(cadena[8:10])
print(cadena[-1])
print(cadena[-2])
print(cadena[::-1])
print(cadena[2::-1])