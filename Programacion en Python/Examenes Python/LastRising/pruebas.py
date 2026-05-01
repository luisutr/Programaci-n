"""Suma de fecha y días
El cálculo de la nueva fecha es relativamente complicado. Nuestra estrategia es empezar en el día uno del mes
sumando el número del día menos uno a los días que hay que sumar. Una vez en este punto vamos sumando los días
de cada mes hasta que ya no nos queden suficientes días que sumar y ese resto se suma al número de día inicial.
De esta forma nos evitamos el problema de tener que corregir una fecha a posteriori."""

def sumar_dias(fecha, dias):
    dias += fecha[0] - 1
    fecha = (1, fecha[1], fecha[2])
    while dias > 0:
        fecha, dias = sumar_mes(fecha, dias)
    return fecha

def sumar_mes(fecha, dias):
    dm = dias_mes(fecha)
    if dm > dias:
        return (1+dias,fecha[1],fecha[2]), 0
    return siguiente_mes(fecha), dias - dm

def dias_mes(fecha):
    ndias = [[0,31,28,31,30,31,30,31,31,30,31,30,31],
             [0,31,29,31,30,31,30,31,31,30,31,30,31]]
    return ndias[es_bisiesto(fecha[2])][fecha[1]]

def siguiente_mes(fecha):
    if fecha[1] == 12:
        return (fecha[0], 1, fecha[2]+1)
    return (fecha[0], fecha[1]+1, fecha[2])

def es_bisiesto(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

print sumar_dias((21,1,2016), 15)
print sumar_dias((21,1,2016), 1)
print sumar_dias((31,1,2016), 1)
print sumar_dias((31,1,2016), 0)
print sumar_dias((21,1,2016), 366)


"""Regresión lineal
Este ejercicio es aplicación directa de la fórmula, no tiene nada especial.
"""
def regresion_lineal(puntos):
    xm = media([p[0] for p in puntos])
    ym = media([p[1] for p in puntos])
    xy = 0.
    xx = 0.
    for p in puntos:
        xy += (p[0]-xm)*(p[1]-ym)
        xx += (p[0]-xm)**2
    a = xy/xx
    b = ym - a*xm
    return a,b

def media(l):
    return sum(l)/len(l)

print regresion_lineal([(0.,1.),
                        (1.,4.),
                        (-1.,-2.)])
print regresion_lineal([(1.,1.),
                        (2.,2.),
                        (8.,8.)])
print regresion_lineal([(1.,1.),
                        (2.,2.),
                        (8.,8.1)])

"""Bloque 2. Ley D'Hont
El algoritmo que se propone en el bloque 2 es muy simple. Basta calcular la tabla de votos divididos por el número de escaños para cada partido. Las celdas de esa tabla se ordenan de manera que el que pueda pagar más por cada escaño vaya primero. Por último basta coger solo tantas celdas como escaños haya disponibles y contar a quién corresponde cada escaño.
"""
def reparto_d_hont(n, votos):
    precios_ordenados = sorted(precios_por_escanno_partido(votos, n),
                               key = celda_precio,
                               reverse=True)
    return cuenta_escannos(precios_ordenados[:n])

"""En esta implementación hemos usado algunas características avanzadas de la función sorted pero es simplemente por brevedad. Lo mismo puede conseguirse con una simple función auxiliar y escribiendo las tuplas en el orden adecuado para que las comparaciones se produzcan como queremos.
La tabla de precios por escaño y partido, es decir, los votos divididos por número de escaños, la implementamos como una simple lista de tuplas con el nombre del partido y el coste del escaño. Esto facilita enormemente la ordenación."""

def precios_por_escanno_partido(votos, n):
    precios = []
    for partido in votos:
        precios += precios_por_escanno(partido, n)
    return precios
"""Donde el precio por escaño que podría pagar cada partido, siguiendo la ley de oferta y demanda es simplemente el número de votos dividido por el número de escaños disponibles (que pueden ser entre 1 y n). Es decir:"""

def precios_por_escanno(partido, n):
    return [ (partido[0], partido[1]/i) for i in range(1,n+1) ]
"""Contar los escaños es simplemente contar cuántas celdas de cada partido han quedado. Por comodidad lo hacemos con un diccionario y lo ordenamos por número decreciente de escaños, como en los resultados electorales oficiales."""

def cuenta_escannos(precios):
    escannos = {}
    for p in precios:
        incrementa_cuenta_escannos(escannos, celda_partido(p))
    return sorted([(k, escannos[k]) for k in escannos ],
                  key = celda_precio,
                  reverse = True)
"""Al utilizar un diccionario inicialmente vacío tenemos que tratar de forma especial el caso del escaño inicial. También podríamos haber inicializado el diccionario con todos los partidos y una cuenta inicial a cero."""

def incrementa_cuenta_escannos(escannos, partido):
    if partido in escannos:
        escannos[partido] += 1
    else:
        escannos[partido] = 1
"""Cada celda contiene el nombre del partido y el precio que puede pagar. Para no llenar el código con índices que son muy propensos a error utilizamos funciones auxiliares que dada una celda devuelve cada uno de sus elementos."""
def celda_precio(celda):
    return celda[1]

def celda_partido(celda):
    return celda[0]
"""Solo falta probar. Haremos dos casos de prueba, el del enunciado y los resultados de Madrid de las últimas elecciones generales.
"""
print reparto_d_hont(12,
                     [('A', 4000000),
                      ('B', 3500000),
                      ('C', 2000000),
                      ('D', 1500000)])

print reparto_d_hont(36,
                     [('PP', 1203837),
                      ('Podemos', 750477),
                      ('Cs', 676389),
                      ('PSOE', 643158),
                      ('Unidad Popular en Comun', 189237),
                      ('UPyD', 43103),
                      ('PACMA', 28302),
                      ('VOX', 22441),
                      ('X La Izquierda-Los Verdes', 5007),
                      ('FE de las JONS', 4688),
                      ('Recortes Cero-Grupo Verde', 4009),
                      ('PUM+J', 2832),
                      ('PH', 1848),
                      ('PCPE', 1730),
                      ('SAIn', 1229),
                      ('P-LIB', 1053)])



"""Vocales anumeros """

def vocales_a_numeros(s):
    return ''.join([letra_transformada(c) for c in s])

def letra_transformada(c):
    vocales = 'aeioAEIO'
    numeros = '43104310'
    if c in vocales:
        return numeros[vocales.index(c)]
    return c

"""Iniciales
Simple manipulación de cadenas. Eliminamos todo lo que no sean letras porque no serían iniciales. Eso no se indica en el enunciado, por lo que se consideraría válido aunque no se haga.
"""
def iniciales(s):
    palabras = normalizar_cadena(s).split(' ')
    return ''.join([p[0] for p in palabras if len(p) > 0])

def normalizar_cadena(s):
    return ''.join([noletra_a_espacio(c) for c in s])

import string

def noletra_a_espacio(c):
    transtab = dict(zip(u'ÁÉÍÓÚÜáéíóúü','AEIOUUaeiouu'))
    if c in transtab:
        return transtab[c]
    validas=string.letters + u'Ññ'
    if c in validas:
        return c
    return ' '

print iniciales('No por mucho madrugar,amanece mas temprano')

"""Traza de una matriz cuadrada
Es trivial con una list comprehension.
"""

def traza(m):
    return sum([m[i][i] for i in range(len(m))])

print traza([[1,2,3],[4,5,6],[7,8,9]])
print traza([[1,0,0],[0,1,0],[0,0,1]])

"""Producto escalar y producto vectorial
Define una función escalar y otra función vectorial que implementan el producto escalar y vectorial de dos vectores respectivamente.

Cada vector se representa como una tupla de tres coordenadas cartesianas.
"""
def escalar(a,b):
    return sum(ai*bi for ai,bi in zip(a,b))

def vectorial(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])

"""
Triángulo de Pascal¶
El triángulo de Pascal es un triángulo de números que se construye de la siguiente manera. Empieza con un 1 en la fila superior. Cada fila posterior se construye a partir de la inmediata superior, donde el primer y el último número de cada fila son iguales que el primer y último número de la anterior, y cada número entre ellos es la suma de los dos a la izquierda y a la derecha en la fila inmediatamente superior. La fila enésima tiene n números. Tiene la siguiente pinta:

      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1
Define la función triangulo_pascal que imprime por salida estándar un triángulo de Pascal con el número de líneas que se indica en su único argumento.

Nota: El triángulo debe imprimirse siguiendo escrupulosamente la salida del ejemplo. Los espacios son parte esencial del problema. Nota que los números están separados por un espacio y las líneas están centradas respecto a la de mayor tamaño.
"""

def trianguloPascal(n):

    # creamos una lista que contendra los dos primeras lineas
    lista = [[1],[1,1]]

    # bucle que se generara tantas veces como lineas vayamos a tener
    for i in range(1,n):

        # inicializamos la linea
        linea = [1]

        # bucle por cada uno de los valores de la anterior linea
        for j in range(0,len(lista[i])-1):

            # añadimos a la lista los nuevos valores
            # sumamos el valor de la lista anterior con el siguinte
            #linea.extend([ lista[i][j] + lista[i][j+1] ])
            linea.append(lista[i][j] + lista[i][j+1])

        # añadimos el ultimo valor a la nueva linea
        # siempre es un 1 igual que el primero
        #linea += [1]
        linea.append(1)

        # añadimos la linea a la lista
        lista.append(linea)

    #devolvemos la lista ya creada
    return lista

def triangulo_pascal():
    try:
        n = int(raw_input("Numero de lineas para triangulo de Pascal: "))
        resultado = trianguloPascal(n)
        L = [' '.join([str(i) for i in x]) for x in resultado]
        for s in L:
            espacios = (len(L[-1])-len(s))//2
            print(' '*espacios + s)
    except:
        print "\nTiene que ser un valor numerico"

triangulo_pascal()



"""Date un paseo de 10 minutos"""


"""Fórmula de Ramanujan para π
Una de las fórmulas más utilizadas para aproximar el valor de pi se la debemos al genial matemático indio Srinivasa Ramanujan.
Define una función sr_pi(n) que calcula la aproximación de pi utilizando solo los n primeros términos del sumatorio en la fórmula de Ramanujan.
Ignoraremos los efectos de la imprecisión de los números reales."""

from math import factorial as fact
from math import sqrt

def inv_pi(n):
    return (2*sqrt(2)/9801)*sum(fact(4*k)*(1103+26390*k)/(fact(k)**4*396**(4*k)) for k in range(n))

def sr_pi(n):
    return 1/inv_pi(n)

sr_pi(10)

"""
Números crecientes y decrecientes
Se define un número creciente como aquél en el que sus dígitos, leídos de izquierda a derecha, nunca son menores que los anteriores. 234559 es un ejemplo de número creciente. De forma complementaria, número decreciente es aquel cuyos dígitos leídos de izquierda a derecha nunca son mayores que los anteriores. 97732 es un ejemplo de número decreciente.

Elabora la función creciente_decreciente que admite un único argumento numérico y devuelve 1 si es creciente, -1 si es decreciente y 0 si no es ni creciente ni decreciente.

Nota: Si el número es tanto creciente como decreciente (números con una cifra o con varias cifras iguales) debe devover 1 (primero creciente).
"""

def creciente_decreciente(n):
    cifras = [ int(x) for x in str(n) ]
    diferencias = [ b-a for a,b in zip(cifras,cifras[1:]) ] + [0]
    if min(diferencias) >= 0:
        return 1
    if max(diferencias) <= 0:
        return -1
    return 0

"""
Números en cualquier base
Como sabes el computador almacena los números internamente empleando una representación binaria (cada dígito solo puede tener dos valores, el 0 o el 1). En Python es sencillo obtener la representación binaria de un número usando '{:b}'.format(n). Este mecanismo permite obtener la representación en las bases más utilizadas (2, 8, 10 y 16) pero no es general.

En este ejercicio te proponemos definir la función to_base(n, b) que devuelve una lista con los dígitos de la representación de n en base b.

Ejemplo de funcionamiento
>>> to_base(978, 16)
[3, 13, 2]
>>> to_base(978, 10)
[9, 7, 8]
>>> to_base(978, 4)
[3, 3, 1, 0, 2]
Fíjate en que no utilizamos símbolos especiales para los dígitos de bases mayores que 10, sino que simplemente almacenamos en la lista el valor correspondiente de cada dígito.
"""

def to_base(n, b):
    if n == 0: return []
    return to_base(n//b, b) + [n%b]
"""
Números super pandigitales
Un entero positivo es pandigital en la base b (o b-pandigital) si contiene todos los dígitos de 0 a b-1 al menos una vez cuando se escriben en la base b. Un número n-super-pandigital es aquél que es pandigital en todas las bases desde 2 hasta n ambas incluidas.

Por ejemplo, 978=11110100102=11000203=331024=124035978=11110100102=11000203=331024=124035 es el número más pequeño 5-super-pandigital, y 10932657841093265784 es el número más pequeño 10-super-pandigital.

Escribe una funcion es_superpandigital(x, n) que devuelve True si el número x es n-super-pandigital y False en caso contrario.

Ejemplo de funcionamiento
>>> es_superpandigital(978, 5)
True
>>> es_superpandigital(978, 6)
False
"""

def es_superpandigital(x, n):
    return all(es_pandigital(x,b) for b in range(2,n+1))

def es_pandigital(x,b):
    digitos = set(to_base(x,b))
    return all(d in digitos for d in range(b))



""""Como realizar las pruebas
podeis llevaros una plantilla"""

import unittest
from unittest import TestCase
class Test(TestCase):
    def test_1_creciente_decreciente(self):
        self.assertEqual(1, creciente_decreciente(5))
        self.assertEqual(1, creciente_decreciente(25))
        self.assertEqual(-1, creciente_decreciente(52))
        self.assertEqual(0, creciente_decreciente(523))
        self.assertEqual(0, creciente_decreciente(542235))
        self.assertEqual(1, creciente_decreciente(5669))
        self.assertEqual(-1, creciente_decreciente(977622100))
    def test_2_to_base(self):
        self.assertEqual([3,13,2], to_base(978,16))
        self.assertEqual([9,7,8], to_base(978,10))
        self.assertEqual([3,3,1,0,2], to_base(978,4))
    def test_3_super_pandigital(self):
        self.assertTrue(es_superpandigital(978,4))
        self.assertTrue(es_superpandigital(978,5))
        self.assertFalse(es_superpandigital(978,6))
        self.assertTrue(es_superpandigital(1093265784,9))
        self.assertTrue(es_superpandigital(1093265784,10))
        self.assertFalse(es_superpandigital(1093265784,11))


"""
Convolución de señales
Dadas dos señales de tiempo discreto, definidas como secuencias de valores reales u(k)u(k) y v(k)v(k) se define la convolución de ambas señales como:

w[n]=∑ku[k]v[n−k]

Nota: Una señal u[k]u[k] se modela como una lista u con los números reales desde u[0]u[0] hasta u[m−1]u[m−1] siendo m = len(u). Todos los demás elementos se asume que valen 0. Es decir u[k]=0,∀k∉{0..m}u[k]=0,∀k∉{0..m}.

Definir una función elem con dos parámetros. El primer parámetro es una lista s conteniendo una señal discreta. El segundo parámetro es un entero k que indica un índice de elemento. La función debe devolver s[k] si k está en el rango de índices válidos para la lista s o 0.0 en caso contrario.

Definir una función conv_elem con tres parámetros. Los dos primeros parámetros corresponden a las señales u y v. El tercer parámetro es un entero n. La función debe devolver el resultado de la ecuación definida arriba. Es decir, debe devolver el elemento n-simo de la convolución de u y v. Se sugiere utilizar la función elem para evitar tener que considerar casos especiales.

Definir una función convolucion con dos parámetros que corresponden a las señales u y v y devuelve la lista de números reales resultado de la convolución de ambas señales. La longitud de la convolución de u y v es len(u) + len(v) - 1.

Ejemplo de funcionamiento
u = [ 1., 2., 1., 2., 1., 2., 1., 2. ]
v = [ 1., 2., 3., 2., 1. ]
print convolucion(u,v)

[1.0, 4.0, 8.0, 12.0, 13.0, 14.0, 13.0, 14.0, 12.0, 10.0, 5.0, 2.0]
"""

def elem(signal,k):
    if k >= len(signal) or k < 0:
        return 0.
    return signal[k]

def conv_elem(u, v, n):
    sum = 0.
    for k in range(len(u)):
        sum += elem(u,k)*elem(v,n-k)
    return sum

def convolucion(u,v):
    return [ conv_elem(u,v,i) for i in range(len(u)+len(v)-1) ]

#La función convolucion también se puede hacer sin list comprehensions.

def convolucion(u,v):
    c = []
    for i in range(len(u)+len(v)-1):
        c.append(conv_elem(u,v,i))
    return c


# -*- coding: utf-8; mode: python -*-


"""
Una operación de filtrado básica es la reducción del número de muestras, que equivale a reducir la frecuencia de muestreo.
Esta operación se puede describir matemáticamente así:
yn=xM⋅n
Es decir, la señal de salida conserva los valores de la de entrada, pero solo se preservan una de cada M muestras.
Nota: El diezmado habituamente requiere un paso previo de filtrado que vamos a ignorar en esta prueba
La operación complementaria del diezmado es la interpolación. Generar nuevas muestras como resultado de un promediado de
las muestras de alrededor. En nuestro caso usaremos el método más simple (interpolación lineal) que consiste en generar
muestras como la media aritmética de la muestra que la precede y la que sigue. Es decir:
y2n=xn

y2n+1=(x2n+x2n+2)/2

Es decir, las muestras pares corresponden a la señal original y las impares se toman como la media aritmética de la
anterior y la posterior.
1.	Definir una función diezmar que tenga dos parámetros. El primer parámetro es una lista x que representa la señal de
entrada. El segundo representa a M, la tasa de diezmado. La función debe devolver otra lista con solo uno de cada M elementos de x.
2.	Definir una función interpolar que tenga un parámetro, la lista x que representa la señal de entrada.
La función debe devolver una lista con el doble de elementos, donde los elementos impares se calculan interpolando como se explica arriba.

"""



def diezmar(x,M):
    y=[]
    for i in range(0,len(x),M):
        y.append(x[i])
    return y

def interpolar(x):
    y=[]
    for i in range(len(x)):
        y.append(x[i])
        y.append(.5*(x[i]+elem(x,i+1)))
    return y


"""
Nota numérica

Ejemplo de uso
expediente = ['Sobresaliente', 'Notable', 'Notable', 'Aprobado', 'Suspenso']
print nota_media(expediente)
6.5
"""


"""
Error cuadrático medio
Siguiendo con el ejemplo de la ley de Benford, en este ejercicio debes definir una función ecm_benford que admita un único argumento que es una tupla de nueve números correspondientes a las frecuencias de aparición de cada una de las cifras de 1 a 9 (ver ejercicio anterior para ver un ejemplo). La función debe calcular el error cuadrático medio respecto a la probabilidad ideal de cada cifra según la ley de Benford, que responde a la ecuación:

p(n)=log10(n+1)−log10(n)

Ejemplo de funcionamiento:
>>> ecm_benford((1,0,0,0,0,0,0,0,0))
0.06259926375341245
"""

from math import log10

def ecm_benford(medida):
   ideal=[]
   for n in range(1,10):
       ideal.append(log10(n+1) - log10(n))
   return ecm(medida, ideal)

def ecm(x,y):
   sum=0
   if (len(x) == len(y)):
       for xi,yi in zip(x,y):
          sum += (xi - yi)**2
   return  sum/len(x)

print ecm_benford((1,0,0,0,0,0,0,0,0))

"""
Triángulo numérico
Escribir una función triangulo_numerico sin argumentos que encuentre las cifras del 1 al 9 que deben escribirse en los círculos de la siguiente figura para que la suma de cualquiera de sus lados valga 20.

Cada círculo debe contener una cifra diferente. La función debe devolver una tupla o lista con la secuencia de las cifras que va en cada círculo empezando por el superior y en el sentido de las agujas del reloj.

 Nos piden encontrar una permutación de los números de 1 a 9 que cumpla una serie de restricciones.
"""

from itertools import permutations

def es_solucion(p):
   l = p + (p[0],)
   sum = 0
   sol=[]
   for i in (0,3,6):
       for j in l[i:i + 4]:
           sum += j
       sol.append(sum)
   for k in sol:
       if k != 20:
           return False
   return True

def es_solucion(p):
   l = p + (p[0],)
   return all(20 == sum(l[i:i+4]) for i in (0,3,6))

def triangulo_numerico():
   for p in permutations(range(1,10)):
       if es_solucion(p):
           return p
   raise ValueError('No hay solución')


print triangulo_numerico()


"""
Distancia Minkowski
La distancia Minkowski es una generalización de las distancias Manhatan y Euclídea, que viene dada por la siguiente fórmula.

(∑i=1n∣∣xi−yi∣∣p)1/p

En este ejercicio debes definir una función distancia_minkowski que admita tres argumentos. Los dos primeros argumentos son dos listas (o tuplas) de números de igual longitud. El último es el parámetro p que es un real comprendido entre 1 y 2 y debe tomar como valor por defecto 2. La función debe calcular la distancia Minkowski entre los dos primeros argumentos usando el parámetro p del tercer argumento.

Ejemplo de funcionamiento:
>>> distancia_minkowski([1,2,3], [0,2, 4], p=1.5)
1.5874010519681994
"""

def distancia_minkowski(x,y,p=2):
    return sum(abs(xi-yi)**p for xi,yi in zip(x,y))**(1/p)

distancia_minkowski([1,2,3], [0,2, 4], p=1.5)

"""
Distancia a una agrupación
Uno de los métodos computacionales más importantes en la actualidad es el clustering o agrupamiento de una colección de puntos de un espacio n-dimensional. El objetivo es clasificar los puntos en un conjunto de agrupamientos (o clusters) que contienen los puntos que más se parecen entre sí.

Los algoritmos de clustering deben comparar la distancia entre los puntos y los agrupamientos que se van generando. ¿Cómo podemos medir la distancia de un punto a un agrupamiento? No hay una respuesta universal, suele emplearse la distancia más pequeña entre el punto y cualquiera de los puntos del agrupamiento, o la mayor distancia, o la distancia media a todos los puntos del agrupamiento.

En este ejercicio debes definir una función distancia_cluster(punto, grupo) que tiene dos argumentos. El primero es un punto en un espacio n-dimensional (lista o tupla de valores numéricos), el segundo es un grupo de puntos (lista de puntos). La función debe devolver una tupla con tres valores: la distancia mínima del punto a todos los elementos del grupo, la distancia máxima, y la distancia media (en este orden).

Para medir la distancia entre dos puntos se usará la distancia euclídea (distancia Minkowski para p=2, es decir, la raiz cuadrada de la suma de las diferencias de las coordenadas al cuadrado).

>>> distancia_cluster((1,2,3), [(1,0,0), (1,1,0), (1,2,0), (2,1,0)])
(3.0, 3.605551275463989, 3.2711134314969423)
"""

def distancia_cluster(x, g):
    d = tuple(distancia_minkowski(x,y) for y in g)
    return min(d), max(d), sum(d)/len(d)

distancia_cluster((1,2,3), [(1,0,0), (1,1,0), (1,2,0), (2,1,0)])


"""Centroide de un agrupamiento"""

def centroide(g):
    N = len(g)
    return tuple(sum(x[i] for x in g)/N for i in range(len(g[0])))

centroide([(1,0,0), (1,1,0), (1,2,0), (2,1,0)])

