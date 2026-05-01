# -*- coding: utf-8; mode: python -*-


"""
Una operación de filtrado básica es la reducción del número de muestras, que equivale a reducir la frecuencia de muestreo.
Esta operación se puede describir matemáticamente así:

Es decir, la señal de salida conserva los valores de la de entrada, pero solo se preservan una de cada M muestras.
Nota: El diezmado habituamente requiere un paso previo de filtrado que vamos a ignorar en esta prueba
La operación complementaria del diezmado es la interpolación. Generar nuevas muestras como resultado de un promediado de
las muestras de alrededor. En nuestro caso usaremos el método más simple (interpolación lineal) que consiste en generar
muestras como la media aritmética de la muestra que la precede y la que sigue. Es decir:

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