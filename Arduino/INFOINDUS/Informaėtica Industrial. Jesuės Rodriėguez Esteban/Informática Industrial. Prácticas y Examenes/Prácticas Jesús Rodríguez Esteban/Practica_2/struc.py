############################################## Funciones ################################################################
def setA(struct, a): #Fija el valor de a
    struct[0] = a

def setResult(struct, r):  #Almacena el resultado en r
    struct[1] = r

# -*- coding: utf-8; mode: python -*-

def analizar_numeros(k): #Funcion que se encarga de asegurar que el type de lo introducido es int
    for i in k:
        if i in '0123456789':
            return True

############################################## OPCION 1 ################################################################
def sumatorio(struct):
    lista = struct[0].split(",")
    a = lista[0]
    b = lista[1]
    if analizar_numeros(a)==True and analizar_numeros(b)==True: #Solo admite enteros
        a=int(lista[0])
        b=int(lista[1])
        if a<b:
            struct[1] = "Total:"+str(sumador(a, b)) + "  " + "Rango:"+ str(sumario(a, b))
        else:
            struct[1]= "Error: Has introducido mal los datos. El primer valor debe de ser menor que el segundo valor"
    else:
        struct[1] = "Error: Solo se admiten números enteros"



def sumador(a,b):
    suma=0
    for i in range (a,b+1):
        suma+=i
    return suma

def sumario(a,b):
    cadena=''
    for i in range(a,b):
        cadena+=str(i)
        cadena+='-'
    cadena+=str(b)
    return cadena


############################################## OPCION 2 ################################################################
def cuadrados(struct):
    cadena_numeros=struct[0]
    lista_numeros=cadena_numeros.split(',')
    elementos=lista_numeros[0]
    lista_numeros_a_elevar=lista_numeros[1].split('-')
    elevados=""
    if analizar_numeros(lista_numeros_a_elevar) == True and analizar_numeros(elementos) == True:  # Solo admite enteros
        if len(lista_numeros_a_elevar) == int(elementos):
            for i in range(int(elementos)):
                elevados += str(int(lista_numeros_a_elevar[i])**2) + ","
            struct[1] = elevados[:-1]
        else:
            struct[1]="Has introducido mal los datos"
    else:
        struct[1] = "Error: Solo se admiten números enteros"

############################################## OPCION 3 ################################################################
def contar_n(struct):
    cadena_introducida=struct[0]
    lista_split=struct[0].split(',')
    texto = lista_split[0]
    n = lista_split[1]
    lista=[]
    cadena=''
    for j in n:
        contador = 0
        for i in texto:
            if i == j:
                contador +=1
        lista.append(j + " " + str(contador) +  "veces" + " ")
    for i in lista:
        cadena+=i
        cadena+=(' ')
    struct[1] = cadena

############################################## OPCION 4 ################################################################
def palindromo(struct):
    texto = struct[0]
    cadena=''
    if texto == texto[::-1]:
        cadena+='Es palindromo'
    else:
        cadena+='No es palindromo'
    struct[1] = cadena

############################################## GetResult ################################################################
def getResult(struct):
    return struct[1]
