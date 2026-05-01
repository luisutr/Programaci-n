def test2():
    for i in range(10):
        i = 3
        if i == 3:
            break
        print(i)

#test2()


def PruebaA():
    def pruebaB(x):
        print(x,v,end=" ")
        x+=2
    v=2
    x=3
    pruebaB(v)
    print(x)

#PruebaA()

a=[[0,0,0],[1,1,1],[2,2,2]]

for i in zip(*a):
    print((i), end="")


print("*****************")
f = lambda n,m: n%m != 0

def f(n,m):
    if n%m != 0:
        return True
    return False

print(f(5,15))


print("*****************")

a=[2,4,6]
b=[1,3,5]
c=[i*j for i in b for j in a]

pares=[i*j for i in b for j in a if (i*j)/2 == 2]
result=[]
for i in b:
    for j in a:
        if (i * j) / 2:
            result.append(i*j)

print(c)

print(pares)

print("*****************")