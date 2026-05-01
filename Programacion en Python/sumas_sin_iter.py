def producto_0(args, kwds):
    if type(args)==list:
        args=(args),
    pools=args*kwds
    def cycle(sequence, uplevel):
        while True:
            vals = next(uplevel)   # advance upper level, raises if done
            it = iter(sequence)    # (re-)start iteration of current level
            try:
                while True: yield vals + (next(it),)
            except StopIteration:
                pass
    def cycle(values, uplevel):
        for prefix in uplevel:  # cycle through all upper levels
            for current in values:  # restart iteration of current level
                yield prefix + (current,)

    step = iter(((),))
    for pool in pools:
        step = cycle(pool, step)   # build stack of iterators
    return step

# USADA POR FERNANDO
def producto_5(args, kwds):
    if type(args)==list:
        args=(args),
    pools=args*kwds
    def cycle(values, uplevel):
        for prefix in uplevel:  # cycle through all upper levels
            for current in values:  # restart iteration of current level
                yield prefix + (current,)
    step = iter(((),))
    for pool in pools:
        step = cycle(pool, step)   # build stack of iterators
    return step

#USADA POR MARTA
def producto_1(args, rep):
    if type(args)==list:
        args=(args),
    if type(args)!=int:
        pools = [tuple(pool) for pool in args] * rep
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)

#USADA POR ANDRES
def producto_3(args, kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    if type(args)==list:
        args=(args),
    pools = args*kwds
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
'''
#solo para 2.7
def producto_2(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
'''

def combinartodas(n):
    permutaciones=[]
    x = list(range(1,n))
    for i in range(1, n + 1):
        replist=[]
        for j in range(n):
            replist.append(i)
        productos= producto_5(x, i)
        permutaciones += ([list(p) for p in productos])
    return permutaciones

def sumas(n):
    soluciones=[]
    permutaciones=combinartodas(n)
    for lista in permutaciones:
        if sum(lista)==n and tuple(sorted(lista)) not in soluciones:
            soluciones.append(tuple(sorted(lista)))
    soluciones.append((n,))
    return (soluciones)



#print(sumas(7))#11
print("producto_0")
print(list(producto_0([1,2,3,4,5], 3)))
print("producto_1")
print(list(producto_1([1,2,3,4,5], 3)))
#print("producto_2")
#print(list(producto_2([1,2,3,4,5])))
print("producto_3")
print(list(producto_3([1,2,3,4,5], 3)))
print("producto_5")
print(list(producto_5([1,2,3,4,5], 3)))