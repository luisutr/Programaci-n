import random

def seleccionar_rapido(L,k):
    listaordenada=quicksort(L)
    return listaordenada[k]

def quicksort(cadena):
    menor = []
    igual = []
    mayor = []
    if len(cadena) > 1:
        pivot = random.choice(cadena)
        for x in cadena:
            if x < pivot:
                menor.append(x)
            if x == pivot:
                igual.append(x)
            if x > pivot:
                mayor.append(x)
        return quicksort(menor)+quicksort(igual)+quicksort(mayor)  # se realiza la suma para juntar las cadenas(listas)
    else:  # cuando queda un solo elemento en la  cadena(lista) entonces hay que regresarlo
        return cadena


#Pruebas de ordenamiento
'''    
cadena = list(range(3,18))
random.shuffle(cadena)
print(cadena)
cadena = quicksort(cadena)
print ("SU LISTA ORDENADA CON EL METODO QUICKSORT ES:",  cadena)
'''
print(seleccionar_rapido([5],0))
print(seleccionar_rapido(list(range(8)),3))
L = list(range(3,18))
random.shuffle(L)
print(seleccionar_rapido(L,3))
L = list(range(4,100,2))
random.shuffle(L)
print(seleccionar_rapido(L,5))
