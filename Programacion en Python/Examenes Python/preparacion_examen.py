'''
0 1 2 3 4 5 0
1 2 3 4 5 1
2 3 4 5 2
3 4 5 3
4 5 4
5 5
6
'''

def piramide(n):
    for i in range(n):
        cadena = ""
        for j in range(i,n):
            #print(j,end="")
            cadena += str(j)+" "
        #print(i)
        cadena+=str(i)
        print(cadena)
    print(str(n))
#piramide(12)

#Raíz digital:

def digital_root(n):
    while len((str(n)))!=1:
        suma=0
        for i in str(n):
            suma+=int(i)
        n = suma
    return suma


#print(digital_root(493193))


#####Date un paseo de 10 minutos
#Vives en la ciudad de Cartesia donde todas las calles estan formando una cuadricula perfecta.
# Llegas con diez minutos de adelanto a una cita y decides aprovechar la oportunidad para dar un corto paseo.
# La ciudad proporciona a sus ciudadanos una App para generar paseos de forma automatica en sus telefonos.
#Cada vez que se pulsa un boton recibes
# una lista de cadenas de una letra que representan las direcciones a tomar. Sabes que se
#tarda un minuto en recorrer el ancho
# de una manzana, asi que crea una funcion que devuelva True si el paseo de la App tomara exactamente diez minutos
# (no quieres llegar tarde ni demasiado pronto) y si ademas el paseo termina en el punto de inicio. Devuelve False en caso contrario.
#Nota: Siempre recibiras una lista valida que contiene una coleccion aleatoria de letras (s,n,s,e,w..)
# Nunca se proporcionar una lista vacia (eso no seria un paseo, seria permanecer de pie)

def diezmin(paseo):
    if len(paseo)!=10:
        return False
    else:
        n = paseo.count("n")
        s = paseo.count("s")
        o = paseo.count("o")
        e = paseo.count("e")
        if n-s== 0 and e-o==0:
            return True
        else:
            return False
#print(diezmin(["n","n","s","s","o","o","e","e","n","s"]))

###Persistencia
#Escribe una funcion persistence que toma un entero positivo como argumento y devuelve su persistencia multiplicativa,
#que es el numero de veces que se deben multiplicar los digitos entre si para obtener un solo digito.
#Por ejemplo:
#persistence(39)
#3 # Porque 3*9=27, 2*7=14, 1*4=4
#persistence(999)
#4 # Porque 9*9*9=729, 7*2*9=126, 1*2*6=12, 1*2=2
#persistence(4)
# Porque 4 ya tiene un digito

def persistencia(numero):
    num = str(numero)
    pers = 0
    while len(num) > 1:
        pers = pers + 1
        n = 1
        for i in num:
            n = n*int(i)
        num = str(n)
    return pers

#print(persistencia(999))

def piramide(n):
    c = 0
    lista = ""
    while c < n:
        for i in range(c,n):
            lista += (str(i))
            if (i == n-1):
                lista += (str(c) + '\n')

        c = c + 1
    return lista


#partimos de una matriz de ceros de dimensión 20x15
m = \
[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

lista =["a","b","c"]

fila = m[0]
print(fila[-1])
m[round((len(m)/2))-1][round(len(m[0])/2)]=1
m[-1][-1]=1



def mostrarmatriz(m):
    for fila in m:
        con=""
        for elemnto in fila:
            #print(elemnto,end="")
            con += str(elemnto)
        print(con)

def pintahoriz(n,m):
    for i in range(len(m[n])):
        m[n][i]=1
    return m

def pintarayavertical(n,m):
    for i in range(len(m)):
        m[i][n] = 1
    return m
def pintadiagonal(n,m):
    for i in range(len(m)):
        m[i][i] = 1
    return m

def principal(m):
    mostrarmatriz(m)
    print("Pinta rayas")
    n = int(input("Dame numero de fila para pintar rayas: "))
    m = pintahoriz(n,m)
    mostrarmatriz(m)
    print("------------------------------")
    m = pintarayavertical(n,m)
    mostrarmatriz(m)
    print("------------------------------")
    m = pintadiagonal(n, m)
    mostrarmatriz(m)
    print("------------------------------")

#principal(m)


tupla = [0,0,0]

tupla = 255

print(tupla)

pesos = [2,5,10,2,3,4,9,15,1]

mochila = 20

# busca la mejor combinacion de elemtos para meter el mayor numero de ellos en la mochila
from itertools import combinations

def lamaslarga(posibles):
  max = 0
  posicion = 0
  for i, comb in enumerate(posibles):
    if len(comb)>max:
      max = len(comb)
      posicion = i
  return posibles[posicion]

def combinacionesposibles():
    posibles = []
    for i in range(2, len(pesos)):
        combs = combinations(pesos, i)
        for comb in combs:
            if sum(comb) <= mochila:
                posibles.append(comb)
    return posibles

def llenamochila(pesos, mochila):
    posibles = combinacionesposibles(pesos,mochila)
    return lamaslarga(posibles)


print(llenamochila(pesos, mochila))
