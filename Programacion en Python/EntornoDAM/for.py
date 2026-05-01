cadena = "Hola Hola"
for i in cadena:
    print(i)

print("Posicion|Valor")
print("--------------")
for i in range(len(cadena)):
    print((i,cadena[i]))

lista = ["shooter","rpg","mundo abierto","tercera persona", "terror"]
for i in lista:
    op = "no"
    print("¿Te gustan los juegos "+i+"?")
    op = input("si o no: ")
    if op == "si":
        print("Bien, los "+i+" te gustan.")

