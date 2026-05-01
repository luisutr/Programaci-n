from libreria import *

def practica1(cadena):
    #cuuenta las vocales de la cadena
    listav = devuelve_vocales(cadena)
    return len(listav)
#print(practica1("Hola Mundo"))


#MANEJO DE LISTAS O CADENAS
cadena="Hola Mmundo cruel."
print(cadena[0:5])
print(cadena[5:-1])
print(cadena[5:len(cadena)])
print(cadena[0:-1])
print(cadena[-1])
print(cadena[-2])

#LISTCOMPRESSION********************************************

numeros = [1, 2, 34, 86, 4, 5, 99, 890, 45]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(pares)

pares = [num for num in numeros if num % 2 == 0]
print(pares)

saludos = ['hola', 'saludos', 'hi']
nombres = ['j2logo', 'antonio', 'vega']
frases = [saludo.title()+" "+nombre.title() for saludo in saludos for nombre in nombres]
print(frases)

##LABDA*******************************************

def cuadrado(x):
    return x ** 2
print(cuadrado(5))
cuad = lambda x: x ** 2
print(cuad(5))

def pares(numeros):
    pares=[]
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares
print(pares(numeros))


par = lambda numeros: [num for num in numeros if num % 2 == 0]
print(par(numeros))


#RECORRER MATRICES OJO!!!! que son listas !!!!!

m=[[0,0,8,8,0,0,0],[0,8,1,1,8,0,0],[0,8,1,1,8,0,0],[0,0,8,8,0,0,0]]

print(m[1][2:4])
print(m[2][2:4])

for fila in m:
    for elem in fila:
        print(elem)


lista = [1,2,3,4]

for i in lista:
    print(i)

#apilar los resultados
def gen_basico():
    yield "uno"
    yield "dos"
    yield "tres"

print(list(gen_basico()))

for valor in gen_basico():
    print(valor)  # uno, dos, tres

# devolver el valor de una variable
v = [1,2,3,4]
if type(v) == list:
    print([i for i in v if i%2==0])


# RECORRER DOS LISTAS AL MISMO TIEMPO
A = [2,6,8,3,4,5]
B = [2,6,8,3,4,5]
def gen():
  for i,d in zip(A,B):
    yield i*d

print(list(gen()))


