# Ejercicio numero 1

def suma_rango(a, b):
    suma = 0
    if a > b:
        return 0
    else:
        for i in range(a, b):
            suma = i + suma
    return suma


# Ejercicio numero 2

def contar_negativos(lista):
    numeros = 0
    for i in lista:
        if i < 0:
            numeros = numeros + 1
    return numeros


# Ejercicio numero 3

def buscar_vocal(cadena):
    posicion = -1
    for i in (cadena):
        posicion = posicion + 1
        if i in ["a", "e", "i", "o", "u"]:
            return posicion
    return -1


# Ejercicio numero 4

def multiplos_7(primero, segundo):
    multiplos = []
    for i in range(primero, segundo):
        if i % 7 == 0:
            multiplos.append(i)
    return multiplos


# Ejercicio numero 5

def dibujar_cuadrado(l):
    dibujar_ancho(l)
    for i in range((l - 2) / 2):
        dibujar_largo(l)
    dibujar_ancho(l)


def dibujar_ancho(l):
    print '+' + '-' * (l - 2) + '+'


def dibujar_largo(l):
    print  '|' + ' ' * (l - 2) + '|'


# Ejercicio numero 6

def codigo_cesar(texto):
    alfabetoMinus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabetoMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    codificado = ''
    l = len(alfabetoMayus)
    for letra in texto:
        for i in range(l):
            if (i + 3 < l):
                Posicion = i + 3
            else:
                Posicion = abs((l - i) - 3)
            if letra == alfabetoMinus[i]:
                codificado = codificado + alfabetoMinus[Posicion]
            elif letra == alfabetoMayus[i]:
                codificado = codificado + alfabetoMayus[Posicion]
        if letra == ' ':
            codificado = codificado + ' '
    return codificado

# Ejercicio numero 7

def es_perfecto(x):
    suma = 0
    for i in range(1, x):
        if x % i == 0:
            suma = suma + i
    if suma == x:
        return True
    else:
        return False


# Ejercicio numero 8

def cifras(n):
    decimales = []
    cadena = str(n)
    for i in (cadena):
        i = int(i)
        decimales.append(i)
    return decimales


# Ejercicio numero 9

def sumapuntos(lista):
    suma = 0
    for i in lista:
        if i >= 1 and i <= 7:
            suma = suma + i

        elif i >= 10 and i <= 12:
            suma = suma + 0.5
    return suma


def compara_bazas(lista1, lista2):
    jugador1 = sumapuntos(lista1)
    jugador2 = sumapuntos(lista2)
    if jugador1 <= 7.5 and jugador2 <= 7.5:
        if jugador1 == jugador2:
            return 0
        elif jugador1 > jugador2:
            return 1
        else:
            return 2
    elif jugador1 > 7.5 and jugador2 <= 7.5:
        return 2
    elif jugador2 > 7.5 and jugador1 <= 7.5:
        return 1
    else:
        return 0


# Ejercicio numero 10

def buscar_texto(cadena, subcadena):
    veces = 0
    for i in range(len(cadena)):
        if i == cadena.lower().find(subcadena.lower(), i, len(cadena)):
            veces += 1

    return veces

print buscar_texto("repareparepare repare pare repare", "repare")