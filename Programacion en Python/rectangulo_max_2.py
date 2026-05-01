def potencia(c):
    """Calcula y devuelve el conjunto potencia del
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    potencialista=[]
    for s in r:
        potencialista.append(s + [c[-1]])
    return r + potencialista

def combinaciones(M, n):
    com=[]
    c = len(M)
    for i in range(c):
        com.append([i,i])
    for s in potencia(range(c)):
        if len(s)==n:
            com.append(s)
            com.append(list(reversed(s)))
    #return [s for s in potencia(c) if len(s) == n]
    return sorted(com)
def combina_a_dos(a):
    return (sum(list(map(lambda i: list(map(lambda j: (i, j), a)), a)), []))

def rectangulo_maximo(m):
    dicc={}
    max = 0
    x=combinaciones(m,2)
    #print(x)
    comb = combina_a_dos(x)
    #print(comb)
    for cordenadas in comb:
        ix,iy=cordenadas[0]
        fx,fy=cordenadas[1]
        if ix <= fx and iy <= fy:
            ceros = mira_si_es_ceros((ix, iy), (fx, fy), m)
            if ceros == True:
                dicc[(iy, ix), (fy+1, fx+1)] = (fx + 1) * (fy + 1)
                if max < (fx + 1) * (fy + 1):
                    max = (fx + 1) * (fy + 1)
    #print(dicc)
    for key, value in dicc.items():
        if value == max:
            return (key,value)


def mira_si_es_ceros(coordi,coordf, m):
    ix, iy = coordi
    fx, fy = coordf
    suma=0
    for x in range(ix,fx+1):
        for y in range(iy,fy+1):
            valor = m[x][y]
            suma += valor
    if suma == 0:
        return True
    return False

#print(mira_si_es_ceros((0,1),(3,3), ((1,0,0,1),(1,0,0,1),(0,0,0,1),(1,1,1,1))))


print(rectangulo_maximo(((1,0,0,1),(1,0,0,1),(0,0,0,1),(1,1,1,1))),
                         ((1,0),(3,3)))
print((rectangulo_maximo(((1,0),(1,0))), ((1,0),(2,2))))
'''
1001
1001
0001
1111
'''

def recorresubmatriz(cori, corf, m):
    ix, iy = cori
    fx, fy = corf
    suma=0
    for x in range(ix,fx+1):
        for y in range(iy,fy+1):
            if m[x][y] != 0:
                return False
            suma += 1
    return True, suma

