__author__ = 'Ruben'


def fact(n):
    valor=1
    if n==1 or n==0:
        valor=1
    else:
        for i in range(1,n+1):
            valor=valor*i
    return valor

def coeficientes(filas):
    coeficientes=[]
    a=0
    j=0
    if filas==1:
        coeficientes.append(1)
    else:
        for a in range(filas):
            elemetos=a+1
            for j in range(elemetos):
                resultado=fact(a)/(fact(j)*fact(a-j))
                coeficientes.append(resultado)
    return coeficientes

def escalonar(filas):
    lista = coeficientes(filas)
    lista.reverse()
    i = 2
    print ((len(lista)/2)-1)*" ",
    print lista.pop()
    while i <= len(lista):
        print ((len(lista)/2)-1)*" ",
        for j in range(i):
            print(lista.pop()),
        print
        i+=1

escalonar(4)

