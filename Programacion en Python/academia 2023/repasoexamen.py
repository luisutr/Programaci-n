'''
Termina la solución para que devuelva la suma de todos los múltiplos de 3 o 5
por debajo del número pasado. Además, si el número es negativo, devuelve 0
(para los idiomas que los tienen).
'''

def multiplos35(n):
    suma = 0
    for i in range(3,n):
        if (i%3 == 0) or (i%5==0):
            suma+=i
    return suma
print(multiplos35(10))

'''
Su tarea es escribir una función que tome una cadena y devuelva una nueva cadena con
 todas las vocales eliminadas.

Por ejemplo, la cadena "This website is for losers LOL!" se convertiría en 
"Ths wbst s fr lsrs LL!".
'''

def eliminavocales(cadena):
    sol=""
    vocales = ["a","e","i","o","u"]
    for i in cadena:
        if i.lower() not in vocales:
            sol+=i
    return sol
print(eliminavocales("This website is for losers LOL!"))

'''
Implemente la función que toma una matriz que contiene los nombres de las personas a las que les gusta un artículo. Debe devolver el texto de la pantalla como se muestra en los ejemplos:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
'''
def megusta(lista):
    sol=" like this"
    longitud=len(lista)
    if longitud==0:
        return "no one likes this"
    elif longitud==1:
        return lista[0]+sol
    elif longitud==2:
        return lista[0]+" and "+lista[1]+sol
    elif longitud==3:
        return lista[0]+", "+lista[1]+" and "+lista[2]+sol
    else:
        return lista[0]+", "+lista[1]+" and "+str(longitud-2)+" others"+sol

print(megusta(["Alex", "Jacob", "Mark", "Max"]))

'''
numero de telefono 
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
'''
def createPhoneNumber(l):
    lista=[]
    for i in l:
        lista.append(str(i))
    uno="("+"".join(lista[0:3])+")"
    dos=" "+"".join(lista[3:6])+"-"
    tres="".join(lista[7:])
    return uno+dos+tres
print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

'''
se le pide que eleve al cuadrado cada dígito de un número y los concatene.
Por ejemplo, si ejecutamos 9119 a través de la función, saldrá 811181, porque 9 2 es 81 y 1 2 es 1.
Nota: La función acepta un número entero y devuelve un número entero
'''
def cuadrados(n):
    N=str(n)
    sol=""
    for i in N:
        elem = int(i)
        sol+=str(elem**2)
    return sol
print(cuadrados(9119))

'''
Algoritmo, mira si es un cuadrado
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
'''
from math import sqrt
def escuadrado(n):
    raiz = sqrt(n)
    if raiz-int(raiz)==0:
        return True
    return False
print(escuadrado(26))

'''
getMiddle("test") should return "es"
getMiddle("testing") should return "t"
getMiddle("middle") should return "dd"
getMiddle("A") should return "A"
'''

def getMiddle(cadena):
    sol=""
    tipo=""
    if len(cadena)==1:
        return cadena
    elif len(cadena)%2==0:
        tipo="par"
    else:
        tipo="impar"
    if tipo=="par":
        sol = cadena[int(len(cadena) / 2)-1] + cadena[int(len(cadena) / 2)]
    else:
        sol = cadena[int(len(cadena) / 2)]
    return sol

print(getMiddle("test")) # should return "es"
print(getMiddle("testing")) #should return "t"
print(getMiddle("middle")) #should return "dd"
print(getMiddle("A"))

'''
Un isograma es una palabra que no tiene letras repetidas, consecutivas o no consecutivas.
 Implemente una función que determine si una cadena que contiene solo letras es un isograma. 
Suponga que la cadena vacía es un isograma. Ignorar mayúsculas y minúsculas.
Ejemplo: (Entrada --> Salida)
isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
'''
def isIsogram(palabra):
    listaletras=[]
    for letra in palabra:
        if letra not in listaletras:
            listaletras.append(letra)
    if len(listaletras)==len(palabra):
        return True
    return False
print(isIsogram("moose"))

'''
Escriba una función que tome un número entero como entrada y devuelva el número de bits 
que son iguales a uno en la representación binaria de ese número. Puede garantizar que 
la entrada no sea negativa.
Ejemplo : la representación binaria de 1234 es 10011010010, por lo que la función debería 
regresar 5 en este caso
'''
def conviertedecbin(decimal):
    if decimal <= 0:
        return "0"
        # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

    return numero_binario
def bitcounter(decimal):
    sumbit=0
    binario = conviertedecbin(decimal)
    sbin=str(binario)
    for i in sbin:
        if i == "1":
            sumbit+=1
    return sumbit

print(bitcounter(1234))

'''
Compruebe si una cadena tiene la misma cantidad de 'x' y 'o'. 
El método debe devolver un valor booleano y no distinguir 
entre mayúsculas y minúsculas. La cadena puede contener cualquier carácter.
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''
def XO(cadena):
    cadena=cadena.lower()
    xs=cadena.count("x")
    os=cadena.count("o")
    if xs==os:
        return True
    return False
print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))

'''
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''
def jadencased(cadena):
    mayus=""
    lista = cadena.split(" ")
    for palabra in lista:
        palabra=palabra[0].upper()+palabra[1:]
        mayus+=palabra+" "
    return mayus[:-1]
print(jadencased("How can mirrors be real if our eyes aren't real"))

'''
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''
def accum(cadena):
    sol=""
    for i in range(len(cadena)):
        letra=cadena[i]*(i+1)
        if len(letra)>0:
            letra = letra[0].upper() + letra[1:]
        else:
            letra = letra[0].upper()
        sol+=letra+"-"
    return sol[:-1]
print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))

'''
Se le proporciona una matriz (que tendrá una longitud de al menos 3, pero podría ser muy grande) 
que contiene números enteros. La matriz está completamente compuesta por enteros impares o 
completamente compuesta por enteros pares excepto por un solo entero N. 
Escriba un método que tome la matriz como argumento y devuelva este "valor atípico" N.
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''
def elemnoparidad(lista):
    contp=0
    conti=0
    for i in range(3):
        if lista[i]%2 == 0:
            contp+=1
        else:
            conti+=1
    #lista de pares
    if contp>conti:
        for num in lista:
            #busco el impar
            if num%2 != 0:
                return num
    #la lista es de impares
    else:
        for num in lista:
            #busco el par
            if num % 2 == 0:
                return num
print(elemnoparidad([2, 4, 0, 100, 4, 11, 2602, 36]))

'''
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
'''

#listas comprimidas
numeros = [1, 2, 34, 86, 4, 5, 99, 890, 45]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
print(pares)

#lista resultado = variable append for num in numeros Condicion o condiciones
pares = [num for num in numeros if num % 2 == 0]

cadena = "variable append for num in numeros Condicion o condiciones"
cont=0
palabras = [i for i in cadena if i==" "]
print(len(palabras))

#sets compreshion
frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r"}
print(mi_set)
#{'r'}
#Dictionary comprehension
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']
mi_dict = {i:j for i,j in zip(lista1, lista2)}
print(mi_dict)
#{'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}

#Años bisiestos
#not a % 4 and (a % 100 or not a % 400)
anos=[1982,1992,1994,1998,2000,2001,2003,2002,2010,2022,2024]
bisiesto = [a for a in anos if a%4==0 and (a%400==0 or a % 100!=0)]
print(bisiesto)

