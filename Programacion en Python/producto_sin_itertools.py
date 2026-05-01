
def combina_a_dos():
    a = {1, 2}
    b = {3, 4}
    return (sum(list(map(lambda i: list(map(lambda j: (i, j), b)), a)), []))
print(combina_a_dos())

def cart_product_1(result,*seqs):
    if not seqs:
        return [[]]
    else:
        for x in seqs[0]:
            for p in cart_product_1(result, *seqs[1:]):
                result.append([x]+p)
        return result
print(cart_product_1([],[1,2,3,4]))


def producto_cart():
    i = [1,2,3,4,5]
    j = [1,2,3,4,5]
    return [(x, y) for x in i for y in j]

print(producto_cart())

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

print(combo2([10,15,3,9],2))


def combinations(N, iterable):
    if not N:
        return [[]]
    if not iterable:
        return []

    head = [iterable[0]]
    tail = iterable[1:]
    new_comb = [ head + list_ for list_ in combinations(N - 1, tail) ]

    return new_comb + combinations(N, tail)

print(combinations(2,[10,15,3,4]))
