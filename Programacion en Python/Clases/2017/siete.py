__author__ = 'luisutrilla'

def juego (lista):
    suma = 0
    for i in lista:
        if i >= 1 and i <= 7:
            suma = suma + i
        elif i >= 10 and i <= 12:
            suma = suma + 0.5
    return suma


def compara_mano(lista1, lista2):
    resultado1 = juego(lista1)
    resultado2 = juego(lista2)
    if resultado1 <= 7.5 and resultado2 <= 7.5:
        if resultado1 == resultado2:
            return 0
        elif resultado1 > resultado2:
            return 1
        else:
            return 2
    elif resultado1 > 7.5 and resultado2 <= 7.5:
        return 2
    elif resultado2 > 7.5 and resultado1 <= 7.5:
        return 1
    else:
        return 0

print compara_mano([2,5,12], [7,10])
print compara_mano([1,5,12], [7,10])
print compara_mano([2,5,12], [7,10])
print compara_mano([5,12], [3,10])
print compara_mano([5,12,3], [5,10])
print compara_mano([5,12,3], [5,10,4])
print compara_mano([5,2,12], [5,4,7])