def subset_sum(numbers, target, partial=[], sumas=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target:
        sumas.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n], sumas)
    return sumas
print(subset_sum(range(1,6),6))

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
print(cart_product_1([],[10,15,20,8]))


def producto_cart():
    i = [10,15,20,8]
    j = [10,15,20,8]
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

print(combo2([10,15,20,8],2))


def combinations(N, lista):
    if not N:
        return [[]]
    if not lista:
        return []

    elegido = [lista[0]]
    resto = lista[1:]
    combi = [ elegido + list_ for list_ in combinations(N - 1, resto) ]

    return combi + combinations(N, resto)

print(combinations(3,[10,15,20,8]))

#print(tarros(([10,15,20,8],25)))#3

def comb2(s):
    lista=[]
    for i, v1 in enumerate(s):
        for j in range(i+1, len(s)):
            lista.append([v1, s[j]])
    return lista
print(comb2([10, 20, 15, 8 ]))


def permutaciones(ar_list):
    if not ar_list:
        yield []
    else:
        for a in ar_list[0]:
            for prod in permutaciones(ar_list[1:]):
                yield [a,]+prod


def todas(canciones):
    posibles=[]
    for i in range(len(canciones)):
        posibles+=combinations(i,canciones)
    return posibles

def combinations(N, lista):
    if N==0:
        return [[]]
    if len(lista)==0:
        return []
    elegido = [lista[0]]
    resto = lista[1:]
    combi = []
    for i in combinations(N - 1, resto):
        combi.append(elegido+i)
    return combi + combinations(N, resto)

print(todas([10,15,8,20]))

def potencia(c):
    """Calcula y devuelve el conjunto potencia del
       conjunto c.
    """
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def combinaciones(c, n):
    """Calcula y devuelve una lista con todas las
       combinaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return [s for s in potencia(c) if len(s) == n]

def imprime_ordenado(c):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)

#imprime_ordenado(potencia(range(1,7)))
#imprime_ordenado(combinaciones(range(1,7),4))

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]
def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]
def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s) for s in permuta(c[1:])],[])


imprime_ordenado(permuta(range(1,3)))

def permutaciones(c, n):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c tomando n
       elementos a la vez.
    """
    return sum([permuta(s)
                for s in combinaciones(c, n)],
               [])

imprime_ordenado(permutaciones([1, 2, 3, 4], 2))

def combinations_by_subset(seq, r):
    if r:
        for i in range(r - 1, len(seq)):
            for cl in (list(c) for c in combinations_by_subset(seq[:i], r - 1)):
                cl.append(seq[i])
                yield tuple(cl)
    else:
        yield tuple()


print(list(combinations_by_subset([1, 2, 3, 4], 2)))


def permutations(seq):
    if len(seq) <= 1:
        yield seq
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + seq[0:1] + perm[i:]
print(list(permutations([1, 2, 3])))


list1 = [1,2,3,1,2,3]
list2 = [1,2,3]
combined = []
def combinados(list1,list2):
    for a in list1:
        new_list = []
        for b in list2:
            new_list.append([a, b])
        combined.append(new_list)
    return combined

print(combina_a_dos(list1,list2))

