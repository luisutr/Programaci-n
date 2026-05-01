def creasublistas(L,n):
    lista=[]
    for i in range(0,len(L)-n,n):
        lista.append(L[i:i+n])
    if len(L)%2!=0 and n%2==0:
        lista.append([L[-1]])
    return lista

def sublistas(L):
    lista=[]
    for i in range(1,len(L)):
        lista.append(creasublistas(L,i))
    lista.append(L)
    return lista

print(sublistas([1,2,3,4,5,6,7]))
