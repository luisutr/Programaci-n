
def eliminavocales(cadena):
    cadena = cadena.lower()
    resultado = ""
    for letra in cadena:
        if letra not in ["a","e","i","o","u"]:
            resultado+=letra
    return resultado


def cogeprimos(lista):
    primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,92]
    resultado=[]
    for num in lista:
        if num  in primos:
            resultado.append(num)
    return resultado

#print(cogeprimos([2,4,6,7,21,45,70,55]))


lista = []
lista.append(1)
print(lista)
lista.append("hola")
print(lista)
lista.append(0.5)
lista.append(5)
lista.append("weee")
print(lista)
print(lista[0])
print(lista[-1])
print(lista[1:])
print(lista[:2])
print(lista[1:-1])

#metodos de listass
a=20
lista.append(a) # añade al final
lista.insert(0,"Inicio")
print(lista)
lista.pop() #elimina el ultimo
lista.pop(0) # elimina el valor de la posicion dada
print(lista)
numeros=[45,2,1,6,99,12]
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)


# Manejo de cadenas
cadena="practicas"
print(cadena)
print(cadena[0])
print(cadena[-1])
print(cadena[1:])
print(cadena[:2])
print(cadena[1:-1])


def sumacifras(numero):
    while numero>9:
        suma = 0
        for n in str(numero):
            suma=suma+int(n)
        numero=suma
    return numero
print(sumacifras(2453))

def cuentapalabras(frase):
    num = 0
    listafrase = frase.split(" ")
    print(listafrase)
    #Manera corta de hacerlo
    print(len(listafrase))
    for i in listafrase:
        num+=1
    print(num)
    num=0
    for i in listafrase:
        if len(i)>2:
            num+=1
    return num
print(cuentapalabras("Esto es un frase corta"))

def maximolista(numeros):
    maximo=0
    print(max(numeros))
    print(min(numeros))
    print(numeros.count(99))
    for num in numeros:
        if maximo<num:
            maximo=num
    return maximo
print(maximolista([2,6,7,8,99]))


numero = 64512746
# devolver dependiendo: tiene más pares o tiene mas impares

def maspares(numero):
    strnum=str(numero)
    pares=0
    impares=0
    for num in  strnum:
        if int(num)%2==0:
            pares+=1
        else:
            impares+=1
    if pares>impares:
        return "mas pares"
    return "mas impares"

print(maspares(64512746))


#comprar productos mientras tenga dinero:

#Sean cual sean, compra mientras tengas dinero, que me diga cuantos a comprado

def encuentraPorMenor(precios, alimentos, lista):
    min=999
    posmin=0
    for i in range(len(precios)):
        if min>precios[i] and alimentos[i] not in lista :
            min=precios[i]
            posmin=i
    return posmin
def compraregulera(precios, dinero, alimentos):
    lista=[]
    numproductos=0
    i=0
    while dinero > min(precios):
        posicionmin=encuentraPorMenor(precios, alimentos, lista)
        if dinero>=precios[posicionmin]:
            numproductos+=1
            lista.append(alimentos[posicionmin])
            dinero=dinero-precios[posicionmin]
        else:
            return lista, numproductos, dinero
        if len(precios)==len(lista):
            return lista, numproductos, dinero
    return  lista, numproductos, dinero

precios = [25, 50, 10, 5, 1, 2 ,3 ,4, 12, 100, 200, 80, 5, 10]
productos=["leche", "pan", "galletas", "cocacola", "vino", "whisky", "panchitos", "mermelada", "fufu", "champu", "limones", "patatas", "cafe", "gominolas"]
dinero = 500

print(compraregulera(precios,dinero, productos))




def ajustevoltios(voltios, pilas):
    lista=[]
    i=0
    while voltios>10:
        if voltios>=pilas[i]:
            lista.append(pilas[i])
            voltios=voltios-pilas[i]
        if len(pilas) - 1 == i:
            i = 0
        else:
            i += 1
    return  lista, voltios


voltios = 325  # de admine un desfade de 10v
pilas = [3, 6, 2, 5, 10]

print(ajustevoltios(voltios, pilas))