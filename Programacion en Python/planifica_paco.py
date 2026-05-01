def planifica(L, m, R):
    if len(L) == 0:
        return
    ListaA = sorted(enumerate(list(L)), key=lambda e: e[0])
    pila = []
    for i in ListaA:
        pila.append([i])

    lista_discos = []
    disco_definitivo = []
    disco_pesos = []
    while pila:

        disco = []
        disco = pila.pop()
        lista_discos.append(disco)
        for i in ListaA:
            suma = 0
            for j in disco:
                suma += j[1]
            if suma + i[1] <= R and i not in disco:
                disco_nuevo = disco + [i]
                pila.append(disco_nuevo)

    resultado = []
    while (len(resultado) <= m) and len(lista_discos) > 0:
        disco_definitivo = [lista_discos[0]]
        peso = 0
        for i in lista_discos:

            if (len(i) >= len(disco_definitivo[0])):
                disco_definitivo.append(i)
                disco_definitivo.pop(0)
        for k in disco_definitivo[0]:
            for l in lista_discos:
                if k in l:
                    lista_discos.remove(l)

        if len(resultado) == 0:
            resultado.append(disco_definitivo[0])
        else:
            for j in resultado:
                flag = False
                if set(j).intersection(disco_definitivo[0]) != set():
                    flag = True
                    break
            if flag == False:
                resultado.append(disco_definitivo[0])
                break

    indices_resultados = []
    tupla_indices = []
    for i in resultado:
        for j in i:
            tupla_indices.append(j[0])
        indices_resultados.append(tuple(tupla_indices))
        tupla_indices = []

    return tuple(indices_resultados)

print(planifica([10, 15, 20, 8],2,25))
print(planifica([10, 15],2,25))
print(planifica([10, 25, 15],2,25))
print(planifica([10, 1, 2, 3, 15, 4, 25, 15, 1],2,25))