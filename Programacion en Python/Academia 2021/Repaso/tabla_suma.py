def tablasuma(n,m):
    for i in range(1,10):
        rango=""
        for j in range(n,m+1):
            rango+=str(j+i)+" "
        print(str(i)+" :"+rango)

tablasuma(3,5)

#compresion de listas

lista=[]
for i in range(10):
    lista.append(i*5)
print(lista)

print([i*5 for i in range(10)])

lista=[]
for i in range(10):
    x=str(i*5)
    if(x[-1]=="0" and x!="0"):
        lista.append(x)
print(lista)

print([i*5 for i in range(10) if str(i*5)[-1]=="0" and str(i*5)!="0"])





# -> [1,3,3,1]  4 posciones --> range(4)

def triangulopascal():
    lista = [1, 2, 1]
    for n in range(10):
        nueva = []
        for i in range(n-1):
            if i == 0:
                nueva.append(lista[i])
            else:
                nueva.append(lista[i-1]+lista[i])
        nueva.append(1)
        print(nueva)
        lista = nueva
print(triangulopascal())