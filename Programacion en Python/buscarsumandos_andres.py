# 10 buscar sumandos
def buscar_sumandos(V,x):
    for i in range(len(V)):
        r=x-V[i]
        V[i]=0
        if r in V:
            return (i,V.index(r))
    raise ValueError('')

print(buscar_sumandos([12, 4, 14, 17, 9], 13))
print(buscar_sumandos([1, 1], 2))
print(buscar_sumandos([1, 2, 1], 2))
#print(buscar_sumandos([1,2,3], 8))
