def splitN(L,n):
    cont=0
    nueva=[]
    sub=[]
    for i in L:
        if cont==n:
            nueva.append(tuple(sub))
            cont=0
            sub=[]
            sub.append(i)
            cont+=1
        else:
            sub.append(i)
            cont+=1
    nueva.append(tuple(sub))
    return tuple(nueva)



#print(splitN(range(6), 4))

from matrices import *


def matriz_adj(L):
    maximo=sacamaxdegrafo(L)
    matriz=creamatrizcuadrada(maximo)
    #ubico los puntos con un 1 en la matriz
    for punto in L:
        x = punto[0]
        y = punto[1]
        matriz[y][x]=1
    print(matriz)
    matriz = eliminafilasceros(matriz)
    return matriz

#print(matriz_adj([(2,3), (2,4), (4,5), (5,2)]))


def presente_indicativo(verbo):
    conjugacion=[]
    raiz = verbo[0:-2]
    ar = ["o","as","a","amos","áis","an"]
    terminacion = verbo[-2::]
    if terminacion=="ar":
        for i in ar:
            conjugacion.append(raiz+i)
    return conjugacion
print(presente_indicativo('cantar')) #['canto', 'cantas', 'canta', 'cantamos', 'cantáis', 'cantan']


##### sin Recursividad

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f *=i
    return f
print(factorial(5))


##### con Recursividad

def recufactorial(n):
    if n>1:
        resultado = n*recufactorial(n-1)
    else:
        resultado = 1
    return resultado

print(recufactorial(5))

'''
https://www.universoformulas.com/estadistica/descriptiva/cuartiles/
'''
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
    c = L.pop()
    return c
'''
print((63,34,60,30,45,32,56,40,21,37,54,33,28,53,19,45,28,52,24,29), (28.25, 35.5, 52.75, 63))
print(cuartiles(range(10)), (1.75, 4.5, 7.25, 9))
print(cuartiles((1,2,3)), (1,2,3,3))
print(cuartiles((1,1,1)), (1,1,1,1))

'''

'''
Mezcla de diccionarios
Implementar una función mezcla(A,B) que devuelve un diccionario que mezcla los
elementos de A y B. La función no debe alterar los diccionarios que se pasan como
argumento. En caso de que una clave exista en los dos diccionarios, la clave del
diccionario devuelto deberá estar asociada a una tupla con los dos valores.
'''
def mezcla(A,B):
    D={}
    for claveA, valorA in A.items():
        D[claveA]=valorA
        for claveB, valorB in B.items():
            if claveB == claveA in D:
                D[claveA] = valorA,valorB
            elif claveB not in D:
                D[claveB] = valorB
    return D

A = {"coche" : "coupe", "moto" : "scooter", "barco" : "yate"}
B = {"barco" : "velero", "coche" : "suv", "camion" : "trailer"}
print(mezcla(A, B))

'''
Árboles binarios
Un árbol binario es una tupla de tres elementos o bien None si el árbol está vacío. El
primer elemento es un valor numérico n. El segundo elemento es un árbol binario
con todos los números inferiores a n. El tercer elemento es un árbol con todos los
números superiores a n.
Implementar una función arbol_binario(L) que devuelve el árbol
binario correspondiente a la lista de números que se indica en el argumento L.
Ejemplo:
>>> arbol_binario([3, 8, 1, 13, 5, 9])
(3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))) 
'''

def arbol_binario(L):
    tree = None
    for i in L:
        tree = (node(tree, i))
    return tree

#esta función de devuelve la estructura nodo
def node(tree, i):
    if tree == None:
        return (i, None, None)
    padre, hijoI, hijoD = tree
    if padre > i:
        return (padre, node(hijoI, i), hijoD)
    return (padre, hijoI, node(hijoD, i))


print(arbol_binario([3, 8, 1, 13, 5, 9]))