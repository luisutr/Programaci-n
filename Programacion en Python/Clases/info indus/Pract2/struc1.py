# -*- coding: utf-8; mode: python -*-

def set(struc1, a):
    struc1[0] = a
def setResult(struc1,r):
   struc1[1] = r

def sumatorio(struc1):
    sumario = 0
    valores = struc1[0].split(",")
    a = valores[0]
    b = valores[1]
    for i in range(a,b+1):
        sumario += i
    r = str(sumario)
    struc1[1] = r

def cuadrados(struc1):
    r=""
    lista_de_numeros = struc1[0].split(",")
    orden = int(lista_de_numeros[0])
    elementos = int(lista_de_numeros[1])
    lista = lista_de_numeros[2].split("-")
    for i in range (elementos):
        r+=str((int(lista[i])**orden))
        if i+1<elementos:
            r+=","
    struc1[1]= r

def contar_letras(struc1):
    #["texto,letas",""]
    lista = struc1[0].split(",")
    letras = lista[1]
    texto= lista[0]
    lista=""
    for letra in letras:
        contador=0
        for i in texto:
            if i == letra:
                contador = contador+1
        lista+= letra+str(contador)+","
    lista=lista[:-1]
    struc1[1]=lista #["texto,letras", "lista"]

def capicua (struc1):
    trozo1=""
    trozo2=""
    lista=[]
    cadena_texto = struc1[0]
    for i in cadena_texto: #convierto a lista
        lista.append(i)
    if len(cadena_texto) % 2 != 0: #si es impar quito el elemento del medio
        lista.pop(int(len(cadena_texto)/2))
    print (lista)
    for i in range(len(lista)/2): # mitad izquirda
        trozo1+=lista[i]
    for i in range(len(lista)/2,len(lista)): #mitad derecha
        trozo2+=lista[i]

    print(trozo1)
    print(trozo2)
    trozo2 = trozo2[::-1]
    if trozo1 == trozo2:
        r = "CAPICUA"
    else:
        r = "NO CAPICUA"
    struc1[1]=r

def getResult(struc1):
    return struc1[1]