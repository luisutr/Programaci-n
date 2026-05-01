def todas(canciones):
    posibles=[]
    for i in range(len(canciones)):
        posibles+=combinations(i,canciones)
    return posibles

def combinations(N, lista):
    if N==0:
        return [[]]
    if len(lista)==0:
        return []
    elegido = [lista[0]]
    resto = lista[1:]
    combi = []
    for i in combinations(N - 1, resto):
        combi.append(elegido+i)
    return combi + combinations(N, resto)

print(todas(list(range(6))))
