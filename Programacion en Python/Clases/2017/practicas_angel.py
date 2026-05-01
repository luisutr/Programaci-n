# PRACTICA 11
def suma_rango(n,m):
    suma=0
    for i in range (n,m):
        suma += i
    return suma

# PRACTICA 12
def contar_negativos(lista):
    contar=0
    for i in lista:
        if i < 0:
            contar += 1
    return contar

#PRACTICA 13
def es_primo(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
# PRACTICA 14
def buscar_vocal(texto):
    posicion=0
    for i in texto:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            return posicion
        posicion+=1
    return -1
#PRACTICA 15
def multiplos_7_en_rango(a,b):
    lista=[]
    for i in range(a,b):
        if i %7==0:
            lista.append(i)
    return lista

#PRACTICA 16
def pintar_cuadrado(x):
    superior(x)
    inferior(x)
def superior(x):
    print("+"+"-"*(x-3)+"+")
def inferior(x):
    for i in range (int(x//2)-2):
        print("|"+" "*(x-3)+"|")
    return superior(x)

#PRACTICA 17
import string
def codigo_cesar(texto):
    abecedario=[string.ascii_letters]
    codificacion=""
    for letra in texto:
        for a in range (len(abecedario)):
            if letra == abecedario[a]:
                if (a+3)<len(abecedario):
                    codificacion+=abecedario[a+3]
            else:
                    if a == (len(abecedario)-3):
                        codificacion+="a"
                    elif a == (len(abecedario)-2):
                        codificacion+="b"
                    else:
                        codificacion+="c"

        if letra == ' ':
            codificacion += ' '
    return codificacion

#PRACTICA 18
def es_perfecto(n):
    sumar=0
    for i in range (1,n):
        if n%i==0:
            sumar += i
    if sumar == n:
        return True
    return False

#PRACTICA 19
def cifras(n):
    result=0
    #para convertir a string: str
    for i in str(n):
        numero=int(i)
        result.append(numero)
    return result

#PRACTICA 20
def compara_mano(mano1,mano2):
    sumaA=0
    sumaB=0
    for i in mano1:
        if i > 7:
            sumaA += 0.5
        else:
            sumaA+=i
    for i in  mano2:
        if i >7:
            sumaB += 0.5
        else:
            sumaB+=i
    if (sumaA >7.5 and sumaB >7.5) or (sumaA == sumaB):
        return 0
    elif (sumaB > 7.5 and sumaA <= 7.5)or(sumaA>sumaB and sumaA <= 7.5):
        return 1
    else:
        return 2



