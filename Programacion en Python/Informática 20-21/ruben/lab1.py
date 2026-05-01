# En este archivo deben estar definidas todas las funciones que se piden en el enunciado.

 

# Si trabajas con otros archivos (por ejemplo archivo1.py y archivo2.py) incluye las funciones de esos archivos en éste así:
# from archivo1 import *
# from archivo2 import *
#1:
##1.1.Primer múltiplo de un número: Implementa la función `primer_multiplo` que recibe como argumentos un número entero `n` y una lista `L`
# de números enteros y devuelve la posición del primer múltiplo de `n` que encuentre en la lista `L`. Si no hay ninguno debe devolver -1.
def primer_multiplo(n,L):
    for i in L:
        if i % n==0:
            return(L.index(i))
           
    return(-1)


##1.2. Función `concatena_lineas`:  La función devuelve el resultado de concatenar todas las cadenas insertando un carácter terminador de línea tras cada línea.
def concatena_lineas (c):
    r= ""
    for e in c:
        r= r + e + "\n"
    return r

##1.3. Probabilidad de coincidencia en la fecha de cumpleaños: Esta función debe devolver un número real que corresponde a la probabilidad de que
# al menos dos personas de un grupo de n personas cumplan años en el mismo día.
def prob_mismo_cumple (n):
    e= 0
    p= 1
    for e in range(1, n):
        p = p * (365  - e) / 365
    return (1-p)

##1.4.Suma de serie:
def suma_serie(n):
    if n >= 1:
        e = 1.0
        suma= 0.0
        while e<= n:
            suma +=(1/e**2)
            e += 1
        return suma
    else:
        return 0

##1.5. Números feos: Admite como argumento una secuencia de números enteros.  La función debe devolver el primer número feo de la secuencia o bien `None` si no contiene ninguno.
def primer_feo (L):
    for e in L:
        if feo(e):
            return e
def feo(n):
    if n == 1:
        return False
    for d in (2,3,5):
        n = divide (n,d)
    return n==1
    
def divide (n, d):
    while n%d==0:
        n = n//d
    return n

##1.6.Suma de dígitos: Devuelve un número entero de una sola cifra, resultante de sumar los dígitos del número mientras el resultado tenga más de un dígito.
import math
def suma_digitos (numero):
    c = 11; fin = 0
    while c >= 10:
        ncifras = 0; resto = 2
        while resto > 1:
            ncifras += 1
            resto = numero / (10**(ncifras))
        for e in range (ncifras):
            potencia = ncifras - 1 - e
            cifra = math.floor (numero/(10**(potencia)))
            numero-= cifra * (10**potencia)
            numeroSolo = cifra
            fin += numeroSolo
        c = fin; numero = fin; fin= 0
    return numero

##1.7.Números persistentes:
import math
def en_mandelbrot(x,y):
    z=0
    for e in range (80):
        z = z**2 + complex(x,y)
        if abs(z)>2:
            return False
    return True

##1.8.Números persistentes:
import math
def primer_persistente (p):
    num = 9 ; g = num ; n = 0
    while n != p:
        g += 1
        num = g
        n = 0
        fin = 1
        while num >=10:
            ncifras = 0; resto = 2
            while resto >= 1:
                ncifras += 1
                resto = num / (10**ncifras)
            for e in range (ncifras):
                potencia = ncifras -1 - e
                cifra = math.floor(num / (10**(potencia)))
                num = num - cifra * (10**potencia)
                solo = cifra
                fin *= solo
            num = fin ; fin = 1;n += 1
    return g


##1.9.Cuadrones fuertes:
from math import sqrt
def primer_cuadron_fuerte ():
    for e in range (100000):
        if cuadron_fuerte8 (e):
            return e
def cuadron_fuerte (e):
    s = str(e)
    if s[0] != "1":
        return False
    a = int ('2' + s[1:])
    return raiz(e) and raiz(a)
def raiz (x):
    e= sqrt (x)%1==0
    return e

##1.10.Números ondulantes:
def es_ondulante (n):
    z = str(n)
    e = [int(e)for e in z]
    resta = [a-b for a,b in zip(e,e[1:])]
    negativo = [a<0 for a in resta]
    if all(negativo[::2]) or all(negativo[1::2]):
        return True
    return False

##2.1.Derivación de polinomios: Esta funcion calcula la derivada del polinomio que se pasa como argumento.
pol1 = [2,5,2,1]

def polyder(pol):
    orden = len(pol)
    if orden == 1:
        return 0
    indices = range(orden)
    return [i*j for i,j in zip(pol,indices)][1:]


##2.2.Evaluación de polinomios: Esta funcion evalúa un polinomio `p` para un valor de `x` indicado como segundo argumento.
pol2 = [0,1,1]
var = 3

def polyval(pol, var):
    orden = len(pol)
    indices = range(orden)
    return sum([i*var**j for i,j in zip(pol,indices)])


##2.3.Teorema de Bolzano: (Es un teorema sobre funciones continuas reales definidas sobre un intervalo.
#Intuitivamente, el resultado afirma que, si una función es continua en un intervalo, entonces toma todos los valores intermedios comprendidos entre
#los extremos del intervalo) Utilizamos este teorema para aplicar el método de bisección para calcular una raiz mediante una función `root_bolzano`.
def rng(minimo, maximo):
    from random import random
    return minimo + random()*(maximo - minimo)

def root_bolzano(pol):
    x1 = -abs(max(pol))*2
    x2 = abs(max(pol))*2
    
    xa = rng(x1, x2)
    while abs(polyval(pol, xa)) > 1e-7:
        xa = rng(x1,x2)
        if polyval(pol, x1)*polyval(pol, xa) < 0:
            x2 = xa
        else:
            x1 = xa
    return xa


##2.4.Newton-Raphson general: Se usa la función para encontrar una raiz cualquiera de un polinomio que se indica como primer argumento con un margen de error que se indica como segundo argumento.
def root_newton_raphson(pol,epsilon):
    
    x1 = -abs(max(pol))*2
    x2 = abs(max(pol))*2
    
    xa = rng(x1, x2)
    for n in range(0,1000):
        if abs(polyval(pol, xa)) < epsilon:
            return xa
        if polyval(polyder(pol), xa) == 0:
            return None
        xa = xa - polyval(pol, xa)/polyval(polyder(pol), xa)
    return None





