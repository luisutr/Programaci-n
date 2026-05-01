diccionario = {
    "001":"Luis",
    "002":"Ruben",
    "003":"Maria",
    "004":"Carlota"
}


posicion = "002"
for c,v in diccionario.items():
    if c==posicion:
        diccionario[c]=(diccionario[c],"Carlos")
print(diccionario["002"])
posicion="003"
if posicion in diccionario.keys():
    diccionario[posicion]=(diccionario[posicion],"Juan")
print(diccionario)
valor = "Carlota"
if valor in diccionario.values():
    for c,v in diccionario.items():
        if valor == v:
            diccionario[c]=(v,input("dame un nombre: "))

#Insertar
print(diccionario["003"])
diccionario["005"]="Carlos"

#Modificar
print(diccionario)
diccionario["005"] = "Felipe"

#Eliminar o sacar
diccionario.pop("005")
print(diccionario)

#listar mis claves
claves = diccionario.keys()
print(list(claves))

#puedo listar mis valores
valores= diccionario.values()
print(list(valores))

#recorrer diccionarios
for clave, valor in diccionario.items():
    print(clave,valor)


cartas= {"11":"pareja",
		"1111":"poker de ases",
		"77": "pareja",
		"567SCR":"ecalera"}
def poker():
    lista=["1","R"]
    '''
    for de 4 veces para que guarde en mano variable tipo lista 4 cartas aleatrorias cogidas de de la lista
    primero a mano jugador 1 y luego mano jugador dos
    una evz tenemos las dos manos 
    saco del diccionario los valores de cada uno 
    los comparo y digo quien ha ganado 
    '''
    return 0