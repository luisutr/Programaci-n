def rectangulo_maximo(m):
    dicc={}
    max = 0
    for ix in range(len(m)):
        for iy in range(len(m)):
            for fx in range(len(m)):
                for fy in range(len(m)):
                    if ix <= fx and iy <= fy:
                        ceros = mira_si_es_ceros((ix,iy),(fx,fy),m)
                        if ceros == True:
                            dicc[(ix,iy),(fx,fy)]=(fx+1)*(fy+1)
                            if max < (fx+1)*(fy+1):
                                max = (fx+1)*(fy+1)
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
