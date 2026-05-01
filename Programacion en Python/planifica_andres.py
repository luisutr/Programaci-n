def planifica(lst,m,k):
    solucion=[]
    sol_def=[]
    copia=copialista(lst)
    while m>0 and len(copia)>0:
        cd=selecciona_defin(copia,k)
        canciones=[]
        for c in cd:
            canciones.append(copia.index(c))
            copia[copia.index(c)] = 400
        solucion.append(canciones)
        m=m-1
    for s in solucion:
        sol_def.append(tuple(s))
    return sol_def
def copialista(lst):
    copi=[]
    for i in lst:
        copi.append(i)
    return copi

def selecciona_defin(lst,k):
    R=cabe_en_disco(lst,k)
    sol=[]
    for i in R:
        sol.append(len(i))
    return R[sol.index(max(sol))]

def cabe_en_disco(lst,k):
    R=hace_todas(lst)
    S=[]
    for i in R:
        if sum(i)<=k:
            S.append(i)
    return S
def hace_todas(lst):
    P=[]
    for n in range(len(lst)):
        P+=combo2(lst,n)
    if len(lst)==2:
        P.append(lst)
    return P
def combo2(lst,n):
    if n==0:
        return [[]]
    l=[]
    for i in range(0,len(lst)):
        m=lst[i]
        remLst=lst[i+1:]
        for p in combo2(remLst,n-1):
            l.append([m]+p)
    return l

print(planifica([10, 15, 20, 8],2,25))
print(planifica([10, 15],2,25))
print(planifica([10, 25, 15],2,25))
print(planifica([10, 1, 2, 3, 15, 4, 25, 15, 1],2,25))
