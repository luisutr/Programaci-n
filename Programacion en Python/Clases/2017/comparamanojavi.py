def dibujar_cuadrado(altura):
    altura == int
    fila1= "+"+"-"*(altura-3)+"+"
    print(fila1)
    for i in range((altura/2)-2):
        filacentro="|"+" "*(altura-3)+"|"
        print(filacentro)
    filaultima="+"+"-"*(altura-3)+"+"
    print(filaultima)


def codigo_cesar(texto):
    abecedario="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codificada=""
    for i in texto:
        for j in range(len(abecedario)):
            if j < len(abecedario)-3:
                if i == abecedario[j]:
                    codificada += abecedario[j+3]
            if texto=="X":
                return "a"
            if texto=="Y":
                return "b"
            if texto=="Z":
                return "c"
    return codificada


def es_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma = suma + i
    if suma == numero:
        return True
    else:
        return False


def cifras(numero):
    lista=[]
    #para recorrerlo tiene que ser un string, pero lo que metes en la lista, creo que debe ser enteros
    for i in str(numero):
        lista.append(int(i))
    return lista


def compara_mano(manoA,manoB):
    sumaA=0
    sumaB=0
    cartas1=[1,2,3,4,5,6,7,10,11,12]
    cartas2=[10,11,12]
    for i in manoA:
        if i in cartas1:
            sumaA += 1
        elif i in cartas2:
            sumaA += 0.5
    for i in manoB:
        if i in cartas1:
            sumaB += 1
        elif i in cartas2:
            sumaB += 0.5
    if sumaA == 7.5 and sumaB<7.5:
        return 1
    if sumaA == 7.5 and sumaB == 7.5:
        return 0
    if sumaA <= 7.5 and sumaB > 7.5:
        return 1
    #Quedan hacer todos los otros casos


print dibujar_cuadrado(8)
print codigo_cesar("abcdxyz XYZ")
print es_perfecto(24)
print cifras(1982)
print (compara_mano([1,5,12], [7,10]))