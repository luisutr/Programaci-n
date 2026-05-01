import itertools
def sumas(n):
    soluciones=[]
    x = list(range(1,n))
    permutaciones=[]
    for i in range(1,n+1):
        permutaciones+=([list(p) for p in itertools.product(x, repeat=i)])
    print(permutaciones)
    for lista in permutaciones:
        if sum(lista)==n and tuple(sorted(lista)) not in soluciones:
            soluciones.append(tuple(sorted(lista)))
    soluciones.append((n,))
    return (soluciones)


#print(sumas(4))
#[(1,1,1,1),(1,1,2),(1,3),(2,2),(4,)]

from itertools import permutations
def ts(V,x):
    lista=[]
    permutaciones=list(permutations(V,2))
    for i in permutaciones:
        if i[0]+i[1]==x:
            lista.append(i)
    return lista

#print(ts(list(range(8)),4))
#[(0, 4), (1, 3), (3, 1), (4, 0)]

def sumasM(n):
    lista=[]
    soluciones=[]
    permutaciones=[]
    for i in range(1,n):
        permutaciones += list(permutations(list(range(1,n)), i))
    for lista in permutaciones:
        if sum(lista)==n and tuple(sorted(lista)) not in soluciones:
            soluciones.append(tuple(sorted(lista)))
    soluciones.append((n,))
    return soluciones

#print(sumas(4))#5
#print(sumas(5))#7
print(sumas(6))#11
#print(sumas(7))#15


'''
import itertools 
x = [1, 2, 3, 4, 5, 6] 
print([p for p in itertools.product(x, repeat=2)]) 
'''

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
