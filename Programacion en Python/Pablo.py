def subintervalo_mayor(sec):
    sec1, sec2 = compara(sorted(quita_rep(tupla_conjunto(sec))))
    if len(sec1) > len(sec2):
        return((int(sec1[0]), int(sec1[-1])))
    return((int(sec2[0]), int(sec2[-1])))

def quita_rep(sec):
    sec2 = []
    for i in sec:
        if i not in sec2:
            sec2.append(i)
    return sec2

def compara(s):
    tupla1 = []
    tupla2 = []
    s_llena = list(range(s[0],s[-1]+1))
    for a,b in zip(s, s_llena):
        if a == b:
            tupla1.append(a)
        else:
            if a not in tupla1:
                tupla2.append(a)
    return tupla1, tupla2

def tupla_conjunto(sec):
    intervalo_menor = []
    intervalos = []
    conjunto = []
    for intervalo in sec:
        intervalo_menor = list(range(intervalo[0],intervalo[1]+1))
        intervalos.append(intervalo_menor)
    for i in intervalos:
        for j in i:
            conjunto.append(j)
    return(conjunto)


#print(subintervalo_mayor(((5,7),(9,11),(2,5),(1,4),(4,6))))


import random
def buscar_sumandos2(V,x):
    i = random.choice(V)
    j = random.choice(V)
    if V.count(V[0])!=len(V):
        while i == j:
            j = random.choice(V)
    print(i, j)
    if i + j == x:
        return i, j
    return 0,0
def buscar_sumandos(V,x):
    for w in range(11):
        i,j= buscar_sumandos2(V,x)
    if i !=0 and j!=0:
        return i,j
    else:
        raise ValueError('')


#print(buscar_sumandos([12, 4, 14, 17, 9], 13))
#print(buscar_sumandos([1, 1], 2))
print(buscar_sumandos([1, 2, 1], 2))
#print(buscar_sumandos([1,2,3], 8))