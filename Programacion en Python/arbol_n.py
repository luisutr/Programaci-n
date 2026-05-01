def arbolNavidad(n):
    for i in range(1, n + 1):
        print (" " * (n - i) + "*" * (2 * i - 1))

arbolNavidad(16)

#arbolNavidad(6)


def arbolpatron (patron, n):
    letra = 0
    arbol=[]
    for i in range(n):
        lista = []
        print(" " * (n - i)),
        for j in range(i):
            if letra < len(patron)-1:
                print(patron[letra]),
                lista.append(patron[letra])
                letra+=1
            else:
                print(patron[letra]),
                lista.append(patron[letra])
                letra = 0
        arbol.append(lista)
        print
    return arbol

def centroarbol():
    lista = arbolpatron("abc",10)
    print(lista)
    centro=[]
    for fila in lista:
        if len(fila)%2!=0:
            centro.append(fila[int(len(fila)/2)])
    return centro

print(centroarbol())

