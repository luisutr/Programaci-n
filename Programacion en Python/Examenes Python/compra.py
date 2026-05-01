
def opciones_de_compra(precios, n, total):
    return [ c for c in combinaciones_n(precios, n) if sum(c) <= total ]

def combinaciones_n(precios, n):
    if len(precios) == n:
        return [ precios ]
    if n == 1:
        return [ [x] for x in precios ]
    return [ [precios[0]] + i for i in combinaciones_n(precios[1:], n-1)] \
        + combinaciones_n(precios[1:], n)





print opciones_de_compra([2,5,1,3],2,6)
print opciones_de_compra([3,5,2],2,4)