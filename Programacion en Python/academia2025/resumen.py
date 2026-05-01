
lista = ["a", 1,2, 0.6, (1,4,5), "Hola"]

lista.in


#cuando vale la suma de valores numericos de la cadena

cadena = "Esto es una cadena que tiene numeros com 2, el 4, 0 y el 9 "

# este suma cifra a cifra
def sumanumeros(cadena):
    suma = 0
    c= ""
    for c in cadena:
        if c.isdigit():
            suma += int(c)
    return suma

print(sumanumeros(cadena))


cadena = "Esto es una cadena que tiene numeros com 1, el 10, 20 y el 930 "
#SUMAR CIFRAS de un digito o más
def sumaTodosNumeros(cadena):
    suma = 0
    numero="0"
    for c in cadena:
        if c.isdigit():
            numero += c
        else:
            suma += int(numero)
            numero = "0"
    return suma

print(sumaTodosNumeros(cadena))