__author__ = 'luis'


# Haz un programa que reciba una cadena de texto
# y devuelva las posiciones de la vocal a si existe
def prueba(cadena):
    aux=[]
    for i in range(len(cadena)):
        print i, cadena[i]
        if cadena[i] == "a":
            aux.append(i)

    return aux


print prueba("Cadena")
