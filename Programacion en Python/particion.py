def particion(secc,k):
    pivote = secc[k]
    secc = sorted(secc)
    iz=[]
    dr=[]
    for i in secc:
        if i < pivote:
            iz.append(i)
        else:
            dr.append(i)
    return iz,pivote,dr

#print(particion([32,17,41,52,98,24,65],2))


def buscar_sumandos(V,x):
    for i in range(len(V)):
        for j in range(len(V)):
            if V[i]+V[j]==x:
                return True, i, j
    return False

print(buscar_sumandos([1,2,3,4,5,6],6))