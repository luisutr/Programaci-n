def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma / len(lista)
    return promedio
lista_numeros = [10, 20, 30, 40, 50]
promedio = calcular_promedio(lista_numeros)
print("El promedio es:", promedio)

import pytest
    assert calcular_promedio([]) == 0
    assert calcular_promedio([5]) == 5
    assert calcular_promedio([10, 20, 30, 40, 50]) == 30
    assert calcular_promedio([2.5, 3.7, 5.8]) == pytest.approx(4.0)
    assert calcular_promedio([-10, -5, 0, 5, 10]) == 0
