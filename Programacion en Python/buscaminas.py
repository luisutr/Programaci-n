def rectangulo_max(matriz):
    origen= (0,0)
    final=(1,1)
    coordcuad = (origen, final)
    elem=[]
    for fila in matriz:
        for i in fila:
           elem.append(i)
    if len(elem)==1:
        return coordcuad
    else:
        coordcuads =[]
        coordcuads.append(cuadradosdeceros(matriz))
    return coordcuad

def todoceros(m):
    suma=0
    for fila in m:
        for i in fila:
            suma+=i
    if suma == 0:
        return True
    return False

def cuadradosdeceros(matriz):
    if len(matriz[0])<=2:
        if len(matriz[0])==1:
            return ((0,0),(1,1))
        return ((1,0),(2,2))
    origen=()
    for x in range(len(matriz)):
        fila = matriz[x]
        for y in range(len(fila)):
            elem = fila[y]
            if (y+1 <= len(fila))  and (x+1 <= len(matriz)):
                if (elem == 0 and fila[y+1] == 0) and (matriz[x+1][y]==0 and matriz[x+1][y+1]==0):
                    if origen == ():
                        origen = (y,x)
                if matriz[x][y-1]==0 and matriz[x-1][y]==0 and elem == 0:
                    fin = (y+1,x+1)
    return origen,fin




print(cuadradosdeceros(((1,0,0,1),(1,0,0,1),(0,0,0,1),(1,1,1,1)))) #((1,0),(3,3))-->1,0 - 2,2 (le sumaremos uno al final)
print(cuadradosdeceros(((1,0,),(1,0)))) #((1,0),(3,3))-->1,0 - 2,2 (le sumaremos uno al final)
print(cuadradosdeceros(((0,),(1,0))))
'''
1 0 0 1
1 0 0 1
0 0 0 1
1 1 1 1
'''
