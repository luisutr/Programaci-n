# Definir una función iniciales con un único argumento cadena de texto. La función debe devolver una cadena que contiene
# todas las letras iniciales de cada palabra del texto.
# Por ejemplo, el resultado de iniciales('No por mucho madrugar, amanece más temprano.') debe devolver 'Npmmamt'.
#



def iniciales(s):
    palabras = normalizar_cadena(s).split(' ')
    return ''.join([p[0] for p in palabras if len(p) > 0])

import string

def normalizar_cadena(s):
    return ''.join([signo_a_espacio(c) for c in s])

def signo_a_espacio(c):
    if c in '!?,.-':
        return ' '
    return c