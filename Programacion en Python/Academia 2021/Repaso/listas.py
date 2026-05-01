#REPASO DE LISTAS

lista = ["a","b","c",1,2,3,True,False]

print(lista[-1]) #posicion ultima
print(lista[-2])
print(lista[0])
print(len(lista))
print(list(range(len(lista))))
print(lista.pop())
print(lista.pop(0))
lista.insert(0,"Nuevo")
print(lista)
lista.append("ultimo")
print(lista)
print(lista.index("c"))

#ordenar
numeros = [3,6,3,5,1,9,4,1,2,3,4,9,8,7]
ordenados = sorted(numeros)
print(ordenados)




print("-----------------------------------")



# recibe un texto largo y tiene que devolver la palabra mas larga
# si hay más de una devuelve la primera que encuentre

def devuelvelarga(lista):
    longitudes=[]
    for i in lista:
        longitudes.append(len(i))
    maximo = max(longitudes)
    posicionmax = longitudes.index(maximo)
    return lista[posicionmax]

def palabramaslarga(texto):
    maslarga = ""
    #cadena.split(carcter) es un metodo que divide una cadena por un caracter divisori, en nuestro caso el espacio
    texto = texto.replace(",","")
    texto = texto.replace(".","")
    palabras = texto.split(" ")
    # necesitamos una funcion que nos devuelve la cadena más larga de una lista
    maslarga = devuelvelarga(palabras)
    return maslarga


print(palabramaslarga("Es un metodo que divide una cadena por un caracter divisori, en nuestro caso el espacio."))

# lo mismo pero devuelve la ultima

def devuelvelarga2(palabras):
    max = 0
    maslarga = ""
    for i in palabras:
        if len(i)>=max:
            max = len(i)
            maslarga = i
    return maslarga

def palabramaslarga2(texto):
    maslarga = ""
    #cadena.split(carcter) es un metodo que divide una cadena por un caracter divisor, en nuestro caso el espacio
    texto = texto.replace(",","")
    texto = texto.replace(".","")
    palabras = texto.split(" ")
    # necesitamos una funcion que nos devuelve la cadena más larga de una lista
    maslarga = devuelvelarga2(palabras)
    return maslarga


print(palabramaslarga2("Es un metodo que divide una cadena por un caracter divisori, en nuestro caso el espacio el."))


# ¿Que fruta es la mas cara?
def maximo(lista):
    max = 0
    for i in lista:
        if max < i:
            max = i
    return max

def mas_caras(frutas,precios):
    resultado = []
    posiciones=[]
    #saco las posiciones de los precios más caros
    max = maximo(precios)
    for i in range(len(precios)):
        if max == precios[i]:
            posiciones.append(i)
    for j in posiciones:
        resultado.append(frutas[j])
    return resultado

frutas  = ["manzana","peras","uvas","naranja","fresas","melon"]
precios = [2,2.5,1.5,1.5,3,3]

print(mas_caras(frutas,precios))