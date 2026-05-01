def conviertedecimalabase(decimal,base):
    if decimal <= 0:
        return "Solo se admiten numero positivos"
        # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        resto = int(decimal % base)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(resto) + binario
        # E ir dividiendo el decimal
        decimal = int(decimal / base)
    return binario

def numbits(decimal):
    binario = conviertedecimalabase(decimal,2)
    conta=0
    for i in str(binario):
        if i == "1":
           conta+=1
    return conta

print(numbits(1234))

'''
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

def accum(cadena):
    sol = ""
    for i in range(len(cadena)):
        letra = cadena[i]*(i+1)
        if len(letra) > 0:
            letra = letra[0].upper() + letra[1:]
        else:
            letra = letra[0].upper()
        sol += letra + "-"
    return sol


deso=[8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3]
orde=sorted(deso)
print(orde)

cadena = "aaaaaaashhhhhskkkkkseeeeesiiiii"
listasplit=cadena.split("s")

unir = " ".join(listasplit)

print(unir)

vuelta = list(reversed(orde))
print(vuelta)
print(list(range(8)))

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