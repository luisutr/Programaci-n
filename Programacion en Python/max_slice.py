def max_slice(L):
    maximo = 0
    elmejor = 0
    dicc = {}
    for i in range(len(L)):
        dicc[(i, i)] = L[i]
        if maximo < L[i]:
            maximo = L[i]
        for j in range(i + 1, len(L)):
            dicc[(i, j)] = sum(L[i:j])
            if maximo < sum(L[i:j]):
                maximo = sum(L[i:j])
    print(dicc)
    print(maximo)
    for intervalo, valor in dicc.items():
        if valor == maximo:
            return intervalo
    return (0, 0)


print(max_slice([-2, 1, -3, 4, -1, 2, 1, -5, 4]), (3, 7))
print(max_slice([3, 2, 6, -1, 4, 5, -1, 2]), (0, 8))
print(max_slice([2, -3, 6]), (2, 3))
print(max_slice([2]), (0, 1))