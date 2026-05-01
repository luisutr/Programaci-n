def iter_enlazadas(n):
    for j in range(1,n+1):
        lista = ""
        for i in range(j):
            lista+=str(i)+','
        print (str(j)+": "+lista)

iter_enlazadas(5)

def tabla_suma(n,m):
    for i in range(1,10):
        lista=''
        for k in range(n,m+1):
            k+=i
            lista+=str(k)+" "
        print(str(i)+" :"+lista)
tabla_suma(3,5)

def  recorridos_de_una_lista(L):
    print(sumados(L))
    print(posicionespares(L))
    print(valorespares(L))
    print(posicionesvalorespares(L))

def sumados(L):
    L2=[]
    for i in L:
        L2.append(i+2)
    return L2
def posicionespares(L):
    pospares = []
    for i in range(len(L)):
        if i % 2 == 0:
            pospares.append(L[i])
    return pospares

def valorespares(L):
    valorespares = []
    for i in L:
        if i % 2 == 0:
            valorespares.append(i)
    return valorespares

def posicionesvalorespares(L):
    pares = []
    for i in range(len(L)):
        if L[i] % 2 == 0:
            pares.append(i)
    return pares

recorridos_de_una_lista([2,7,4,5,9,1,21,22,68])

def norma(L):
    suma=0
    for i in L:
        suma+=(i**2)
    return suma
print(norma([1,2,3,4,5]))

def incluye_lista(L,x,y):
    hay_x = False
    hay_y= False
    for i in L:
        if i==x:
            hay_x = True
        if i==y:
            hay_y = True
    if hay_x==True and hay_y==True:
        return True
    return False

print(incluye_lista([0,4,6,7],4,6))

def incluye_lista_2(L,x,y):
    for i in L:
        if i == x:
            for j in L:
                if j == y:
                    return True
    return False

print(incluye_lista_2([0,4,6,7],5,4))


def factoriales(L):
    lista = []
    for i in L:
        factorial=1
        for j in range(1,i+1):
            factorial*=j
        lista.append(factorial)
    return lista

print(factoriales([5,2,6,12,4]))


def cuenta_vocales(cadena):
    lista=[0,0,0,0,0]
    for i in cadena:
        if i=='a':
            lista[0]+=1
        if i=='e':
            lista[1] += 1
        if i=='i':
            lista[2] += 1
        if i=='o':
            lista[3] += 1
        if i=='u':
            lista[4] += 1
    return lista
print(cuenta_vocales('esta cadena'))
#[3,2,0,0,0]
##a e i u o


cadena="23**45**80**90"
print(cadena.split("**"))

def deletrea(palabra):
    cadena = ""
    for i in palabra:
        cadena+=i+" "
    return cadena

def separa(frase):
    frase=frase[0:-1]
    lista = frase.split(" ")
    for palabra in lista:
        print(palabra+"\t- Palabra de "+str(len(palabra))+" caracteres: "+deletrea(palabra))
separa("Esta frase es un prueba.")