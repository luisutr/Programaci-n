import itertools

lista=["it","wkppv","ixoyx","3452","zzzzzzzzz"]

def longest_conect(lista, n):
    """for i in itertools.permutations(lista):
        print i"""
    m=[]
    for i in range(len(lista)):
        aux = []
        for j in range(i,len(lista)):
            if len(aux) < n:
                aux.append(lista[j])
        m.append(aux)
    longest=0
    longest_con=[]
    for x in m:
        suma = 0
        for y in x:
            suma+=len(y)
        if longest<suma:
            longest=suma
            longest_con = x
    return longest_con



print longest_conect(lista,3)