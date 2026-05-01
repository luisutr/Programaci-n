__author__ = 'luisutrilla'


def codigo_cesar2(m):
    alfabetoMinus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alfabetoMayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    clave = ''
    l=len(alfabetoMayus)
    Posicion = 0
    for letra in m:
        for i in range(l):
            if (i + 3 < l):
                Posicion = i + 3
            else:
                Posicion = abs((l - i) - 3)
            if letra == alfabetoMinus[i]:
                clave = clave + alfabetoMinus[Posicion]
            elif letra == alfabetoMayus[i]:
                clave = clave + alfabetoMayus[Posicion]
        if letra==' ':
            clave=clave+' '
    return clave

#print codigo_cesar("abcdef")


# Cifrado Cesar

TAM_MAX_CLAVE = 26

def obtenerModo():
    while True:
        modo = raw_input('Deseas encriptar o desencriptar un mensaje?').lower()
        if modo in ["encriptar", "e", "desencriptar", "d"]:
            return modo
        else:
            print('Ingrese "encriptar" o "e" o "desencriptar" o "d"')

def obtenerMensaje():
    return raw_input('Ingrese su mensaje:')

def obtenerClave():
    clave = 0
    while True:
        clave = int(input('Ingrese el numero de clave (1-%s)' % (TAM_MAX_CLAVE)))
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

from string import*

def codigo_cesar(mensaje):
    traduccion = ''

    ##Quitar esta parte
    dicc = {}
    cont = 0
    for  i in ascii_letters:
        dicc[i]=ord(i)
        cont +=1
    print dicc, cont
    ## Hasta aqui

    for letra in mensaje:
        if letra.isalpha():
            num = ord(letra)
            num += 3
            if letra.islower():
                if num > ord('z'):
                    num -= 58
            if letra.isupper():
                if num > ord('Z'):
                    num += 6

            traduccion += chr(num)
        else:
            traduccion += letra
    return traduccion

print(codigo_cesar("abdAXYZ"))