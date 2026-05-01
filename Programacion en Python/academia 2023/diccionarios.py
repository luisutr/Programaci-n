def vecescaracterdicc(cadena):
    dicc={}
    for i in cadena:
        if i in dicc.keys():
            dicc[i]+=1
        else:
            dicc[i] = 1
    return dicc

print(vecescaracterdicc("Clases"))
#{"C":1,"l":1,"a":1,"s":2...}


productos=["pipas", "leche", "cocacola", "jamon", "salmon", "pan", "manzana", "spagueti", "pollo", "ternera"]
precios = [1,0.79,2,7,18,0.9,0.25,1,3,5]

def preciodproductos(productos,precios):
    diccionariosuper={}
    for i in range(len(productos)):
        diccionariosuper[productos[i]]=precios[i]
    return diccionariosuper
print(preciodproductos(productos,precios))
diccionariosuper = preciodproductos(productos,precios)

def devuelveclave(dicc,v):
    for clave, valor in dicc.items():
        if v==valor:
            return clave
    return -1
print(devuelveclave(diccionariosuper,0.79))

def mochila(dicc, dinero):
    comprados=[]
    while(dinero>0):
        precio = min(diccionariosuper.values())
        if precio<=dinero:
            producto = devuelveclave(dicc,precio)
            if producto not in comprados:
                comprados.append(producto)
                dinero = dinero - precio
            # mi ejercicio elimina los proctos que voy comprando para no repetirlos
            dicc.pop(producto)
        else:
            return comprados
    return comprados

print(mochila(diccionariosuper,1))

'''
Entrada: [["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
Salida: 
{
    "Grae Drake": 98110,
    "Bethany Kok": None,
    "Alex Nussbacher": 94101,
    "Darrell Silver": 11201,    
}
'''
def diccionariolista(L):
    d={}
    for i in L:
        if len(i)==2:
            d[i[0]]=i[1]
        elif i[0]:
            d[i[0]]=None
    return d
print(diccionariolista([["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]))

'''
Write a program to rename a key city to a location in the following dictionary.

Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''
def cambiavalordicc(D,a,b):
    valor = D.pop(a)
    D[b]=valor
    return D
print(cambiavalordicc({'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'},"city","location"))

'''
Sacar la clave con el valor minimo
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
'''
def minimodicc(D):
    minimo = 0
    claves = list(D.keys())
    valores = list(D.values())
    minimo = min(valores)
    posicion = valores.index(minimo)
    return claves[posicion]
print(minimodicc({'Physics': 82, 'Math': 65, 'history': 75}))

'''
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]} 
Explanation : Similar items grouped together on occurrences. 
Input : test_list = [7, 7, 7, 7] Output : {7 : [7, 7, 7, 7]} 
Explanation : Similar items grouped together on occurrences.
'''



'''
Input : palabras = ["go","bat","me","eat","goal","boy", "run"]
        arr = ['e','o','b', 'a','m','g', 'l']
Output : go, me, goal.
'''
def posiblepalabra(palabras,L):
    resul=[]
    # recorro las palabras
    for palabra in palabras:
        existe = True
        #por cada palabra miro a ver si existen sus letras en la lista
        for i in palabra:
            if i not in L:
                existe = False
        # si existen todas sus letras--> meto la palabra en resul
        if existe==True:
            resul.append(palabra)
    return resul

print(posiblepalabra(["go","bat","me","eat","goal","boy", "run"],['e','o','b', 'a','m','g', 'l']))

personal = {"Luis":"Informatica", "Paco":"Algebra", "Selene":"recreo", "Lucia":"fiestas","Moya":"Informatica"}

def cuentapersonal(dicc):
    cont=0
    departamentos = list(dicc.values())
    print(departamentos)
    lista=[]
    for i in departamentos:
        if i not in lista:
            lista.append(i)
    for j in lista:
        print(j+"="+str(departamentos.count(i)))
cuentapersonal({"Luis":"Informatica", "Paco":"Algebra", "Selene":"recreo", "Lucia":"fiestas","Moya":"Informatica"})


lista1=[1,2,3,4,5,6,7]
lista2=["a","b","c","d","e","f","g"]
dicczip={}
for i,j in zip(lista1,lista2):
    dicczip[i]=j
print(dicczip)

'''
Recorrer un diccionario 
diccionario.items() devuelve una lista de tuplas(clave, valor) de tal anera que puedo recorrer esa lista y asiganarla en un  bucle a variables c,v
ej: for c,v in diccionario.items():

diccionario.keys() Devuelve una lista de las claves del diccionario 

diccionario.values() Devuelve una lista de los valores del diccionario

que ara guardar nuevos valores, no tienen que existir como clave, por que sino lo que hago sería modificarlos. 
dicc["clave"]="Valor" crea una entrada en el diccionario si "clave" no pertenece a este. 

si existe y lo quiero es modificarlo
dicc["clave"]= "nuevo valor"

borrar se puede utilizar pop()

'''

dicc={1:"uno",2:"dos"}

dicc[3]="tres"
dicc[1]="nuevo uno"

if 2 in dicc.keys():
    dicc[2]=(dicc[2],"nuevo dos")
print(dicc)



dicctuplas = {"a":(1,2),"b":(1,2,3),"c":(1,2,3,4,5),"d":(2,3,4,5)}
#nd={"a":2,"b":3,"c":5...}

nd2={}
for clave, valor in dicctuplas.items():
    nd2[clave]=len(valor)
print(nd2)