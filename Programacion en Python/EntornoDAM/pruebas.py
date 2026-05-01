from basicas.principales import conviertelistaacadena

cadena = conviertelistaacadena(["a","b"])

quote = "How can mirrors be real if our eyes aren't rea"

def mayus_ini(cadena):
    #split convierte a lista, trocea una cadena por el caracter delimitador
    lista = cadena.split(" ")
    mayus=""
    for palabra in lista:
        # upper convierte a mayus y + concatena en una cadena
        palabra = palabra[0].upper() + palabra[1:]
        mayus+=palabra+" "
    return mayus



