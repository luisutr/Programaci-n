def vocales_a_numeros(s):
    return ''.join([letra_transformada(c) for c in s])

def letra_transformada(c):
    vocales = 'aeioAEIO'
    numeros = '43104310'
    if c in vocales:
        return numeros[vocales.index(c)]
    return c