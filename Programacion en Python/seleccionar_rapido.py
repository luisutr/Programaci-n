import random

def seleccionar_rapido(L,k):
    listaordenada=quicksort(L)
    return listaordenada[k]

def quicksort(arr):
    if not arr:
        return []
    pivote = random.choice(arr)
    pivots = [x for x in arr if x == pivote]
    lesser = quicksort([x for x in arr if x < pivote])
    greater = quicksort([x for x in arr if x > pivote])

    return lesser + pivots + greater




print(seleccionar_rapido([5],0))
print(seleccionar_rapido(list(range(8)),3))
L = list(range(3,18))
random.shuffle(L)
print(seleccionar_rapido(L,3))
L = list(range(4,100,2))
random.shuffle(L)
print(seleccionar_rapido(L,5))
