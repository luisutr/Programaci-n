def cuenta_espacios(texto):
    contador = 0
    for caracter in texto:
        if caracter == " ":
            contador += 1
    return contador

#print(cuenta_espacios(["a","B"," ", " "]))

def buscapares(lista):
    contador = 0
    for numero in lista:
        # un numero par
        if numero%2 == 0:
            contador += 1
    return contador

#print(buscapares([2,3,4,5,6,7,8,9]))

def calculamedia(lista):
    media=0
    suma = 0
    for numero in lista:
        suma += numero
    media = suma/len(lista)
    return media

#print(calculamedia([2,3,4,5,6,7,8,9]))

#Un chico a quedado en un sitio y le sobran 10 minutos
#no quiere esperar y se da una vuelta PERO tiene que regresar a su punto
#JUSTO a los 10 minutos.
#
# movimientos = ["S","N","E","O","S","N","E","O"] ---> "no llega a la cita" len(lista) != 10 --> no se cumple la premisa del tiempo

def cuentaenlista(lista,busco):
    contador = 0
    for caracter in lista:
        if caracter == busco:
            contador += 1
    return contador

def aseguracita(movimientos):
    m = len(movimientos)
    if len(movimientos)!=10:
        return "No llega a la cita"
    else:
        if (cuentaenlista(movimientos,"S") == cuentaenlista(movimientos,"N")) and (cuentaenlista(movimientos,"O")==cuentaenlista(movimientos,"E")):
            return "llega a la cita"
        else:
            return "No llega a la cita"

#print(aseguracita(["S","S","E","E","O","O","N","N", "E", "O"]))


#posiciones donde estan los espacios

def localiza_espacios(texto):
    espacios = []
    for posicion,valor in enumerate(texto):
        if valor == " ":
            espacios.append(posicion)
    return espacios
#print(localiza_espacios("Hola hola hola"))

'''
lista = ["S","S","E","E","O","O","N","N", "E", "O"]
lista.pop(8)
print(lista)
'''


#dada una lista cualquiera de elemntos quiero eliminar lo que se encentre en las posiciones pares

def eliminapospares(lista):
    posimapres = []
    for posicion,valor in enumerate(lista):
        if posicion%2 != 0:
            posimapres.append(valor)
    return posimapres

print(eliminapospares(["S","S","E","E","O","O","N","N", "E", "O"]))




nombre = "petra"

def dalavueltanombvre(nombre):
    # creacion de variables
    # codigo que resulelve
    return 0


"artep"




















