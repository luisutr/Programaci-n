'''1. Máximos de una señal
Una señal puede representarse por una secuencia (o cualquier objeto iterable) de valores reales que corresponden a los valores de la señal en instantes periódicos de tiempo. Los instantes de tiempo suelen identificarse por números enteros positivos consecutivos (0,1,2,3,...).

Implementa una función maximos(v) que admite un único argumento v que codifica la función como se describe arriba. Debe devolver las posiciones (instantes de tiempo) en las que la función tiene un máximo local.

     maximos([0,1,2,3,2,3,0])
    (3, 5)
Nota: El tipo de contenedor devuelto puede ser cualquier iterable, incluso un generador'''

def maximos(v):
    maximo = 0
    posicion = []
    for numero in v:
        if maximo < numero:
           maximo = numero
    for i in range(len(v)):
        if v[i] == maximo:
            posicion.append(i)
    return tuple(posicion)
#print(maximos([0, 1, 2, 3, 2, 3, 0]))

def maximos2(v):
    posiciones = []
    maximo = max(v)
    for i in range(len(v)):
        if v[i] == maximo:
            posiciones.append(i)
    return posiciones


def maximos3(v):
    pos = []
    maximo = max(v)
    pos.append(encuentramax(v,maximo,0,[]))
    return pos

def encuentramax(v,m,i,p):
    if v.index(m):
        pos = v.index(m)
        p.append(pos)
        v.pop(pos)
        v.insert(pos, "X")
    else:
        return p
    encuentramax(v,m,i,p)

def movmean(x, n):
    s=[int(x[0]/n)]
    print(s)
    for i in range(len(x)+1-n):
        suma=0
        for j in range(i,i+n):
            suma += x[j]
        s.append(int(suma/n))
    return tuple(s)


print(movmean([0, 4, 0, 2, 0, 0, 6, 0, 0, 0], 2), (0, 2, 2, 1, 1, 0, 3, 3, 0, 0))

def calculamedia(x):
    suma = 0
    for i in x:
        suma += i
    return suma/len(x)

def std(x):
    n = len(x)
    sumatorio = 0
    a = 0
    import math
    for i in range (n):
        sumatorio = sumatorio + x[i]
    media = sumatorio/n
    for j in range (n):
        a = a + (x[j] - media)**2
    return math.sqrt(a/(n-1)), media
# Ejercicio 6
def normalize (x):
    z = []
    b,media = std(x)
    for k in range(len(x)):
        z.append((x[k] - media)/b)
    return z
'''x
print(normalize([1,2,3]),[-1,0,1])
print(normalize([1.1,.9,1.1,.9]),
                             [0.8660254037844392,
                              -0.8660254037844382,
                              0.8660254037844392,
                              -0.8660254037844382])
print(normalize(range(5)),
                             [-1.2649110640673518,
                              -0.6324555320336759,
                              0,
                              0.6324555320336759,
                              1.2649110640673518])
print(normalize([0,2,4]),[-1,0,1])
'''
def calculam(n,s):
    if n == 1:
        return s
    if n%2==0:
        n = n/2
        s.append(int(n))
    else:
        n = (n*3)+1
        s.append(int(n))
    return calculam(n,s)

def ulam(n):
    solucion = []
    solucion.append(n)
    return calculam(n,solucion)

def ulam2(n):
    s=[]
    s.append(n)
    while (n != 1):
        if n%2==0:
            n = n/2
            s.append(int(n))
        else:
            n = (n*3)+1
            s.append(int(n))
    return s

'''
def chk(n,i): L=tuple(i); return n,sum(L),len(L)
for n,s,l in ((1,1,1),(157,3170,37),(37,535,22),(222,86371,71)):
    print(chk(n,ulam2(n)), (n,s,l))
'''
from math import sqrt
def std2(x):
    suma = []
    N = len(x)
    media = calculamedia(x)
    for i in range(N):
        suma.append((x[i]-media)**2)
    return sqrt((1/(N-1))*sum(suma))

def std(x):
    suma = 0
    N = len(x)
    media = calculamedia(x)
    for i in range(N):
        suma+=((x[i]-media)**2)
    return sqrt((1/(N-1))*suma)
'''
print(std([1,1,1,1,2,1,1,1,1]),0.3333333333)
print(std([1,2,3]),1)
print(std([2,2,1,2,3,2,1,2,2]),0.6009252125773316)
print(std([3,3,5,7,7]),2)
'''

def normalize(x):
    z=[]
    media = calculamedia(x)
    desvia = std(x)
    for i in range(len(x)):
        z.append((x[i]-media)/desvia)
    return z

def extiendelista(x,y):
    if len(x) > len (y):
        aux=[]
        for i in range(len(x)- len(y)):
            aux.append(0)
        y = y + aux
    else:
        aux = []
        for i in range(len(y) - len(x)):
            aux.append(0)
        x = x + aux
    return x,y

def xcorr(x, y):
    correla = []
    ## calcula N y m segun longitudes
    if len(x) > len (y):
        N = len(x)
    else:
        N = len (y)
    m = range(-1*(N-1),N)
    ## Extiende para que las dos listas tengan la misma longitud
    x, y = extiendelista(x, y)
    #print(x)
    #print(y)
    #print(N)
    #print(m)
    for im in m:
        suma = 0
        if im < 0:
            ##N-im-1 de estos bucles quito el -1 porque por definicion el for llega uno menos
            for n in range(N+im):
                suma += y[n-im]*x[n]
            correla.append(suma)
        if im>=0:
            for n in range(N-im):
                suma += x[n+im]*y[n]
            correla.append(suma)
    return tuple(correla), m

'''
print(xcorr([1,2,1], [0,1,0]),
                             ((0,1,2,1,0),range(-2,3)))
print(xcorr([1,2,3,2,1], [0,1,1]),
                             ((0,0,1,3,5,5,3,1,0),range(-4,5)))
print(xcorr([1,2,3,2,1], [1,1,1]),
                             ((0,0,1,3,6,7,6,3,1),range(-4,5)))
print(xcorr([1,1,1], [1,2,3,2,1]),
                             ((1,3,6,7,6,3,1,0,0),range(-4,5)))
print(xcorr([1,2,3,4,5], [3,1,0]),
                             ((0,0,0,1,5,9,13,17,15),range(-4,5)))
print(xcorr([1,2,0,4,5], [3,4]),
                             ((0,0,0,4,11,6,16,32,15),range(-4,5)))

'''

def ondulante(num):
  x = [int(a) for a in str(num)]
  es_ondulante=0
  for i in range(1,len(x)-1):
    if (x[i-1] < x[i] and x[i] > x[i+1]) or (x[i-1] > x[i] and x[i] < x[i+1]):
      pass
    else:
      es_ondulante+=1
  if es_ondulante == 0:
    return True
  return False

print(ondulante(1212121))

def palindromas(cadena):
  #Metemos la palabra en una lista
  cadena=list(cadena.lower())
  cadena_revertida=cadena[::-1]
  es_palindromo=0
  for x,y in zip(cadena,cadena_revertida):
    if x != y:
      es_palindromo+=1
  if es_palindromo == 0:
    return True
  return False


palindromas('Sometemos')




#[(1,2),(2,3),(3,1),(4,5),(5,6),(4,6)]
#(5,6) --> punto
# 0 1  --> punto[0] --> 5. punto[1] --> 6
def alcanzable(L,n):
  sol=[n]
  for punto in L:
    if n in punto:
      if punto[0]!=n:
        sol.append(punto[0])
      else:
        sol.append(punto[1])
  return sorted(sol)

print(alcanzable([(1,2),(2,3),(3,1),(4,5),(5,6),(4,6)],6))

def imprimir_diagonal(M,x,y):
    diagonal=[]
    long = len(M)-max(x,y)
    for i in range(len(M)):
        if long!=0:
            diagonal.append(M[x+i][y+i])
            long-=1
    return diagonal

print(imprimir_diagonal([[1,2,3,9],[4,5,6,4],[7,8,9,5],[2,3,4,5]],0,2))
'''
  0 1 2 3
0[1,2,3,9],
1[4,5,6,4],
2[7,8,9,5],
3[2,3,4,5]
'''