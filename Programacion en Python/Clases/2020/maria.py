def polyval(p,x):
  result = 0
  for posi,valor in enumerate(p):
    result = result + valor*(x**posi)
  return result

#print(polyval([1,0,0,0,2,3],5))

## EJERCICIO 13

def rng(minimo, maximo):
    from random import random
    return minimo + random()*(maximo - minimo)

def root_bolzano(polinomio):
    tol = 1e-07
    minimo=1
    maximo=-1
    error=9999
    while minimo > 0:
        aleatorio = rng(-200, 200)
        print(aleatorio)
        minimo = polyval(polinomio,aleatorio)
    while maximo < 0:
        aleatorio = rng(-200, 200)
        maximo = polyval(polinomio,aleatorio)
    while abs(error)>tol:
        medio = (maximo+minimo)/2
        funcion = polyval(polinomio,medio)
        if funcion>0:
            maximo = funcion
        else:
            minimo = funcion
        error = abs(funcion-medio)
    return funcion

#print(root_bolzano([1,0,2,2,4,1]))

## EJERCICIO 9

from math import sqrt


def primer_cuadron_fuerte():
    for i in range(1000000):
        if cuadron(i) == True:
            c1 = str(i)
            if c1[0] == "1":
                c2 = c1.replace("1", "2", 1)
                if cuadron(int(c2)) == True:
                    return i

def cuadron(n):
    raiz = sqrt(n)
    entera = int(raiz)
    decimales = raiz - entera
    if decimales == 0.0:
        return True
    else:
        return False

print(primer_cuadron_fuerte())