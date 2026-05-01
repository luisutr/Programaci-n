__author__ = 'luisutrilla'
import string

alfabeto = string.ascii_letters

def codigo_cesar(m, n):
    clave = ''
    l = len(alfabeto)
    Posicion = 0
    for letra in m:
        for i in range(l):
            if (i + n < l):
                Posicion = i + n
            else:
                Posicion = abs((l - i) - n)
            if letra == alfabeto[i]:
                clave = clave + alfabeto[Posicion]
        if letra == ' ':
            clave = clave + ' '
    return clave

clave = codigo_cesar("Hola xyz XYZ", 3)

print(clave)


def codigo_cesar(m):
    clave = ''
    l = len(alfabeto)
    Posicion = 0
    for letra in m:
        for i in range(l):
            if (i + 3 < l):
                Posicion = i + 3
            else:
                if i == (l-3): #letra a
                    Posicion = 0
                elif i == (l-2):
                    Posicion = 1
                else:
                    Posicion = 3
            if letra == alfabeto[i]:
                clave = clave + alfabeto[Posicion]
        if letra == ' ':
            clave = clave + ' '
    return clave



print codigo_cesar("Hola xyz XYZ")


import string
def codigo_cesar_angel(texto):
    abecedario= string.ascii_letters
    codificacion=""
    for letra in texto:
        for a in range(len(abecedario)):
            if letra == alfabeto[a]:
                if (a+3)<len(abecedario):
                    codificacion+=abecedario[a+3]
                else:
                    if a == (len(abecedario)-3): #letra a
                        codificacion+="a"
                    elif a == (len(abecedario)-2):
                        codificacion+="b"
                    else:
                        codificacion+="c"

        if letra == ' ':
            codificacion += ' '
    return codificacion

print codigo_cesar_angel("Hola xyz XYZ")


import string
def codigo_cesar_alvaro(texto):
    alfab = alfabeto_lista()
    numero = len(alfab)
    codigo = ""
    posicion = 0
    for letra in (texto):
        for i in range(numero):
            if i+3 < numero :
                posicion = i + 3
            elif i == numero-3:
                posicion = 0
            elif i == numero-2:
                posicion = 1
            elif i==numero-1:
                posicion = 3
            if letra == alfab[i]:
                codigo += alfab[posicion]
        if letra == " ":
            codigo += " "
    return codigo


def alfabeto_lista():
    abc=[]
    for i in (string.ascii_letters):
        abc.append(i)
    return abc

print codigo_cesar_alvaro("Hola xyz XYZ")


def codigo_cesar_javier(cadena):
    codigo = []
    dario= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"]
    for i in cadena:
        n = dario.index(i)
        codigo.append(dario[n+3])
    return codigo

print (codigo_cesar("Hola xyz XYZ"))


def codigo_cesar_israel(texto):
    abcd='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc'
    codigo=""
    for j in texto:
        for i in range(len(abcd)):
             if j == abcd[i] and i+3 < len(abcd):
                codigo += abcd[i+3]
        if j == " ":
            codigo += " "
    return codigo

print codigo_cesar_israel("Hola xyz XYZ")


#### No esta ni medio empezada, pero es que no tengo ni idea de como seguir