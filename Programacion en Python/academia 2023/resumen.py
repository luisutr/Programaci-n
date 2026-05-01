def zodiaco(fecha):
    """
    Aries (21 de marzo al 19 de abril)
    Tauro (20 de abril al 20 de mayo)
    Géminis (21 de mayo al 20 de junio)
    Cáncer (21 de junio al 22 de julio)
    Leo (23 de julio al 22 de agosto)
    Virgo (23 de agosto al 22 de septiembre)
    Libra (23 de septiembre al 22 de octubre)
    Escorpio (23 de octubre al 21 de noviembre)
    Sagitario (22 de noviembre al 21 de diciembre)
    Capricornio (22 de diciembre al 19 de enero)
    Acuario (20 de enero al 18 de febrero)
    Piscis (19 de febrero al 20 de marzo)
    :param fecha:
    :return:
    """
    print(fecha[3:])
    if (int(fecha[0:2]) >= 22 and int(fecha[3:])>=11) or int(fecha[3:])==12:
        return "Sagitario"
    if fecha == "Septiembre":
        return "Virgo"
    if fecha == "Julio":
        return "Leo"


print(zodiaco("15/12"))
pares=[]
for i in range(2,22,2):
  pares.append(i)

print(pares)
print(len(pares))



def rellenalista(N):
    lista=[]
    for i in range(N):
        lista.append(int(input("Dame un valor: ")))
    return lista

#print(rellenalista(5))


def tabla(a):
    for b in range(1,11):
        print(str(a)+"x"+str(b)+"="+str(a*b))

def tablasmulti(n):
    for i in range(1,n+1):
        tabla(i)
        print()

tablasmulti(10)

def notas(n):
    if n < 5:
        return "suspenso"
    elif n>=5 and n<6:
        return "suficiente"
    elif n>=6 and n<7:
        return "bien"
    elif n>=7 and n<9:
        return "notable"
    elif n>=9 and n<=10:
        return "sobresaliente"
    return "La nota introducida es erronea"

print(notas(2.9))
print(notas(5.1))
print(notas(7))
print(notas(9.8))

L = [14,16,19,18,20,31,12,11,19,20,40,32,23,23,23,45,60,12,12,16,20,20,20,20,30,18,17]

def discoteca(lista,n):
    edades=[]
    suma=0
    il=0
    while suma<=n:
        if il >= len(lista):
            return edades
        if lista[il]>=18 and lista[il]<=30:
            suma+=1
            edades.append((il,lista[il]))
        il+=1
    return edades

print(discoteca(L,10))
print(discoteca(L,20))
'''
254638  Si su longitud es mayor de 1 tengo que sumar sus digitos
28      si el resultado es mayor tengo que seguir igual hasta que su suma sea de longitud 1 
10      ese sera el valor que debemos devolver
1 
'''

def sumadigitos(n):
    suma = 0
    for i in str(n):
        suma += int(i)
    return suma

def sumaloca(n):
    p=0
    while(n>=10):
        n = sumadigitos(n)
        p+=1
    return (p,n)

print(sumaloca(768679870798573))

import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)

if "c" in list(string.ascii_lowercase):
    print("minuscula")


def evaluacontrasena(passw):
    #minusculas y mayus
    minus=False
    mayus=False
    numeros=False
    for i in passw:
        if i.islower():
            minus = True
        if i.islower() == False:
            mayus=True
        if i in ["0","1","2"]:
            numeros=True
    if minus==True and mayus==True and numeros==True and len(passw)>=6 and len(passw)<=12:
        return True
    return False
print(evaluacontrasena("Contra10"))

def contrasenas():
    passw=input("dame una contrasena:")
    while(evaluacontrasena(passw)==False):
        passw=input("dame una contrasena:")
    print(passw)
#contrasenas()

numeros = [9,8,7,6,5,4,3,2,1]
print(list(reversed(numeros)))
eliminar=[1,2,3]
resul=[9,8,7,6,5,4]

print("***************")
print(numeros[3:len(numeros)])


def eliminovaloreslista(lista,aeliminar):
    valoresdrop=[]
    # recorro la lista de numeros a eliminar y cojo uno
    for i in aeliminar:
        #recorro la lista con valores y posiciones
        for valr in lista:
            #si el valor coincide guardo su posocion en una nueva lista
            if i == valr:
                valoresdrop.append(valr)
    #ahora ya solo me queda recorrer esas posiciones y aplicar pop a todas ellas en la lista
    for j in valoresdrop:
        lista.remove(j)
    return lista
print(eliminovaloreslista(numeros,eliminar))


def eliminaduplicados(lista):
    unicos=[]
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    return unicos

def sacadosmax(lista):
    dos=[]
    maximo = max(lista)
    dos.append(maximo)
    while(maximo in lista):
        lista.remove(maximo)
    dos.append(max(lista))
    return dos

print(sacadosmax([4, 10, 10, 9] ))

def cadenatodosizquierda(arr,pos):
    cadena=""
    # los de la izquiereda son desde 0 hasta la posicion +1, porque en las listas de python no llegan al ultimo
    for i in range(0,pos+1):
        cadena+=arr[i]+" "
    return cadena[0:-1]
def cadenatodosderecha(arr,pos):
    cadena=""
    # los de la derecha son desde la posicion hasta el final que es len(arr)
    for i in range(pos,len(arr)):
        cadena+=arr[i]+" "
    # lequito el ultimo caracter para que no tenga un espacio al final
    return cadena[0:-1]

def partlist(arr):
    print(len(arr))
    newlist=[]
    for i in range(len(arr)):
        # tengo que ir guardando tuplas [a,b]
        #coge todos los elementos a la izquierda de esa poscion en tipo cadena y los guarda en variable a
        a = cadenatodosizquierda(arr,i)
        #coge todos los elementos a la derecha de esa poscion en tipo cadena y los guarda en variable b
        b = cadenatodosderecha(arr, i)
        #Finalmente mete la tupla [a,b] en la newlist
        newlist.append([a,b])
        for i in newlist:
            print(len(i))
    return newlist, len(newlist)

print(partlist(["az", "toto", "picaro", "zone", "kiwi"]))


def todoizqdesdei(arr,i):
    elem=""
    for j in range(0,i):
        elem+=arr[j]+" "
    return elem[0:-1]

def tododerechadesdei(arr,i):
    elem = ""
    for j in range(i,len(arr)):
        elem += arr[j]+ " "
    return elem[0:-1]

def nuevoconexplicaciondePM(arr):
    L = []
    for i in range(1,len(arr)):
        L.append([todoizqdesdei(arr,i), tododerechadesdei(arr,i)])
    return L

print(nuevoconexplicaciondePM(["az", "toto", "picaro", "zone", "kiwi"]))

def approx_equals(a, b):
    a = round(a, 3)
    b = round(b, 3)
    print(a,b)
    if a+0.001==b or b+0.001==a or a==b:
        return True
    return False
print(approx_equals(1456.3652, 1456.3641), False)


def warn_the_sheep(queue):
    if queue[-1]=="wolf":
        return "Pls go away and stop eating my sheep"
    queue.reverse()
    N=queue.index("wolf")
    return "Oi! Sheep number "+str(N)+"! You are about to be eaten by a wolf!"

print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
print(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')


