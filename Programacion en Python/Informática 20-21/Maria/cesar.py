from math import *

def rng(minimo, maximo):
    from random import random
    return minimo + random() * (maximo - minimo)

def root_bolzano(pol):
    error = 1e-8

    error_cometido = inf

    xn = rng(-10000, 10000)
    xp = rng(-10000, 10000)

    fn = polyval(pol, xn)  # imagen negativo
    fp = polyval(pol, xp)  # imagen positivo

    if fp > 0:
        while fb * fn > 0:
            xn = rng(-10000, 10000)
            fn = polyval(pol, xp)
    if fp < 0:
        xn = xp
        fn = fp
        while fb * fn < 0 or fb=fn:
            xp = rng(-10000, 10000)
            fp = polyval(pol, xp)

    while abs(error_cometido) > error:
        xs = (xp + xn) / 2
        fs = polyval(pol, xs)
        if fs > 0:
            xp = xs
        else:
            xn = xs
        error_cometido = abs(xn - xp)
    return xs

def polyval(p,x):
    lista = []
    a = 0
    for pos, i in enumerate(p):
         a = a+(i*(x**pos))
    return a

def polyder(P):
    deri = []
    for i in range(1,len(P)):
        deri.append((i)*(P[i]))
    return deri

def primer_persistente(n):
    for i in range(10 ,1000000):
        grado = n_persistente(i)
        if grado == n:
            return i


def n_persistente(nu):
    iteracione s =1
    p = 1
    if nu > 9:
        while nu != 0:
            u = n u %10
            p *= u
            nu =(nu - u) / 10
            iteraciones += 1
            persistencia = iteraciones
    return persistencia

def primer_cuadron_fuerte():
    for i in range(1, 500):
        if cuadrado_perfecto(i) == int:
            i[0] = 2
            if cuadrado_perfecto(i) == int:
                return i


def cuadrado_perfecto(n):
    if sqrt(n) == int:
        return n