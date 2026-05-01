def cuartiles(L):
    L=sorted(L)
    if len(L) < 4:
        return(q1(L), q2(L), L[-1], L[-1])
    return(q1(L), q2(L), q3(L), q4(L))

def q1(L):
    q=0.00
    x= (len(L)+1)/4
    if (x != int(x)):
        inicio=int(x)-1
        fin=inicio+1
        decimal = abs(x) - int(x)
        q = float(L[inicio])+decimal*(L[fin]-L[inicio])
        return q
    return L[x]

def q2(L):
    q=0.00
    x=(len(L))/2
    if len(L) % 2 == 0:
        inicio=int(x)-1
        fin= int(x)
        q=(L[inicio]+L[fin])/2
        return q
    return L[int(x)]

def q3(L):
    x = 3*(len(L)+1)/4
    decimal = abs(x)-int(x)
    if decimal != 0:
        return L[int(x)-1]+decimal*(L[int(x)]-L[int(x)-1])
    return L[int(3*(len(L)/4)-1)]

def q4(L):
    return L.pop()

print((63,34,60,30,45,32,56,40,21,37,54,33,28,53,19,45,28,52,24,29), (28.25, 35.5, 52.75, 63))
print(cuartiles(range(10)), (1.75, 4.5, 7.25, 9))
print(cuartiles((1,2,3)), (1,2,3,3))
print(cuartiles((1,1,1)), (1,1,1,1))
