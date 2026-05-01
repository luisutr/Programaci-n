numero = 999999
decimal = 9823649.981
cadena = "Buenos dias Lucia Ohhhh"

vocales = ["a","e","i","o","u"]
for letra in cadena:
    if letra.lower() in vocales:
        print(letra + " Es una vocal")


for letra in str(numero):
    print(letra)


print("+++++++++ LISTAS +++++++++")
lista_enteros= [2,3,4,5,5,-1,0,9999,-111]
lista_rara = [2,0.9,"Pera",[1,2,3],999,"Otra cosa"]


for elemento in lista_rara:
    print(elemento)

lista_listas = [[1,2,3],[2,3,4],[3,4,5]]
#                 0        1        2
sumatorio = 0
for elemento in lista_listas:
    if 3 in elemento:
        sumatorio+=1
print(sumatorio)
print(lista_listas[2])


print("+++++++++++ recorro por posiciones+++++")
posiciones = [0,1,2]
#        0,1,2          3
for i in range(len(lista_listas)):
    print(lista_listas[i])

def elementospares(lista):
    pares = []
    for valor in lista:
        if valor % 2 == 0:
            pares.append(valor)
    return pares
print(elementospares([1,2,3,4,5,6,7,8,9]))

def posicionespares(lista):
    pares = []
    for posicion in range(len(lista)):
        if lista[posicion]%2==0:
            pares.append(posicion)
    return pares

def posicionespares2(lista):
    pares = []
    for posicion,valor in enumerate(lista):
        if valor%2==0:
            pares.append(posicion)
    return pares

print(posicionespares([1,2,3,4,5,6,7,8,9]))
print(posicionespares2([1,2,3,4,5,6,7,8,9]))


print(list(enumerate(["a","b","c","d"])))


frutas=["Albaricoque", "Melon", "Sandia", "Aguacate"]

productos=["pipas", "leche", "cocacola", "jamon", "salmon", "pan", "manzana", "spagueti", "pollo", "ternera"]
precios = [1,0.79,2,7,18,0.9,0.25,1,3,5]

print(precios.index(min(precios)))

def mochila(productos, precios, dinero):
    comprados=[]
    while(dinero>0):
        if min(precios)<=dinero:
            posmin = precios.index(min(precios))
            if productos[posmin] not in comprados:
                comprados.append(productos[posmin])
                dinero = dinero - precios[posmin]
            # mi ejercicio elimina los proctos que voy comprando para no repetirlos
            precios.pop(posmin)
            productos.pop(posmin)
        else:
            return comprados
    return comprados

print(mochila(productos,precios,5))


cadena = "Don Quijote de la Mancha​ es una novela escrita por el español Miguel de Cervantes Saavedra. Publicada su primera parte con el título de El ingenioso"
lista = []
for i in cadena:
    lista.append(i)
print(lista)

lista = list(cadena)

cadena1="".join(lista)
print (cadena1)

print(cadena1.split("."))
print("E".islower())
print("H".lower())

numero = 5.98796
# función me devuelva solo la parte decimal 0.9
cadena = str(numero)
pospunto = cadena.index(".")
print(float("0"+cadena[pospunto::]))

def esmultiplo(m,i):
    if i%m==0:
        return True
    else:
        return False

def asteriscosenmultipllo(m,L):
    resul=[]
    for i in L:
        if esmultiplo(m,i):
            resul.append("*")
        else:
            resul.append(i)
    return resul

print(asteriscosenmultipllo(3,[2,3,5,6,7,9,18,81]))

def censura(frase):
    resul=[]
    lista = frase.split(" ")
    palabrotas = ["puta", "cago", "ostias"]
    for palabra in lista:
        if palabra.lower() in palabrotas:
            resul.append("*"*len(palabra))
        else:
            resul.append(palabra)
    return " ".join(resul)

print(censura("Me cago en la puta aunque tenia que haber alguna palabra que no fuera mal sonante OSTIAS"))