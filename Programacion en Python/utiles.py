a = 20.00

print a//3

print a/3


def tomarmejor(caben):
    maximo=0
    longitud=0
    posicion=0
    for i in range(len(caben)):
        if longitud<len(caben[i]):
                longitud=len(caben[i])
    for j in range(len(caben)):
        if longitud == len(caben[j]) and maximo<sum(caben[j]):
            posicion=j
    return posicion


def elementosrepe(L):
    for i in L:
        if L.count(i)>1:
            return -1
    return 0