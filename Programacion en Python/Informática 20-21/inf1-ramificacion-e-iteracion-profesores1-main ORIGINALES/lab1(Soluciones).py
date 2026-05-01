# En este archivo deben estar definidas todas las funciones que se piden en el enunciado.

# Si trabajas con otros archivos (por ejemplo archivo1.py y archivo2.py) incluye las funciones de esos archivos en éste así:
# from archivo1 import *
# from archivo2 import *

def primer_multiplo(n, L):
    for i, x in enumerate(L):
        if x % n == 0:
            return i
    return -1

def concatena_lineas(L):
    cad = ''
    for linea in L:
        cad = cad + linea + '\n'
    return cad

def prob_mismo_cumple(n):
    P = 1.0
    for i in range(1,n+1):
        P = P * (366 - i) / 365
    return 1.0 - P

def suma_serie(n):
    suma = 0
    for i in range(1,n+1):
        suma = suma + 1/i**2
    return suma

def primer_feo(L):
    for i in L:
        if es_feo(i):
            return i

def es_feo(n):
    for d in [2,3,5]:
        n = quita_factor(n, d)
    return n == 1

def quita_factor(n, d):
    while n % d == 0:
        n = n / d
    return n

def suma_digitos(n):
    while n > 9:
        n = suma1(n)
    return n

def suma1(n):
    suma = 0
    for d in str(n):
        suma = suma + int(d)
    return suma

def en_mandelbrot(x,y):
    z, c = 0, complex(x,y)
    for i in range(80):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def primer_persistente(n):
    for i in range(1000000):
        if es_persistente(n,i):
            return i

def es_persistente(n, v):
    for i in range(n):
        if v < 10: 
            return False
        v = mult_cifras(v)
    return v < 10

def mult_cifras(n):
    p = 1
    for d in str(n):
        p = p * int(d)
    return p

def primer_cuadron_fuerte():
    for i in range(100000):
        n = i**2
        if es_cuadron_fuerte(n):
            return n

def es_cuadron_fuerte(n):
    from math import sqrt
    s = str(n)
    if s[0] != '1': 
        return False
    n2 = int('2' + s[1:])
    return sqrt(n2) % 1 == 0

def es_ondulante(n):
    L = list(cifras(n))
    prev = None
    for a,b in zip(L,L[1:]):
        if a == b:
            return False
        nuevo = a < b
        if nuevo == prev:
            return False
        prev = nuevo
    return True

def cifras(n):
    for i in str(n):
        yield int(i)

def polyder(p):
    return [i*c for i,c in cdr(enumerate(p))]

def cdr(L):
    it = iter(L)
    next(it)
    yield from it

def polyval(p,x):
    suma = 0
    for i,c in enumerate(p):
        suma = suma + c*x**i
    return suma

def root_bolzano(p, epsilon=1e-4):
    low, high = iniciales(p)
    x = (high + low)/2.0
    while abs(polyval(p,x)) >= epsilon:
        if (polyval(p,x)<0) == (polyval(p,low)<0): low = x
        else: high = x
        x = (high + low)/2.0
    return x


def iniciales(p, minimo=-1000., maximo=1000.):
    def rng():
        from random import random
        return minimo + random()*(maximo - minimo)

    def chk(a, b):
        return (polyval(p,a)<0) != (polyval(p,b)<0)
    
    for _ in range(1000000):
        a, b = sorted((rng(), rng()))
        if chk(a, b):
            return a, b

    raise Exception('No encuentro valores iniciales para', p)


def root_newton_raphson(p, epsilon=1e-4):
    pd, x = polyder(p), -p[0]
    while abs(polyval(p,x)) >= epsilon:
        print('err', polyval(p,x))
        x -= polyval(p,x)/polyval(pd,x)
    return x
