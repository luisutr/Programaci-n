def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
print(factorial_recursivo(5))

def cuentapalabras_recursivo(cadena):
    if len(cadena)==0:
        return 0
    else:
        return 1 + (cuentapalabras_recursivo(cadena[0:-1]))
print(cuentapalabras_recursivo("hola"))


'''
1,2, -->  3,5,8,13,21,
n = (n-1)+(n-2)
'''
def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

print(fibonacci_recursivo(12))

# saca los numeros de una variable que mezcla numeros y listas
l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15, [16, [17, ]], 19]]]]]]]
def sacanumeros(l,numeros=[]):
    for item in l:
        if type(item) is list:
            sacanumeros(item)
        else:
            numeros.append(item)
    return numeros

print(sacanumeros(l))

def posiciones_de(a,b,pos=[],orgigen=0):
    if a.count(b)==len(pos):
        return pos
    else:
        pos.append(a.find(b,orgigen))
        return posiciones_de(a,b,orgigen=pos[-1]+1)


print(posiciones_de("Un tete a tete con Tete", "te"))
#[3, 5, 10, 12, 21]

def arbolalista(arbol, numeros=[]):
    for item in arbol:
        if type(item) is tuple:
            arbolalista(item)
        elif type(item) is int:
            numeros.append(item)
    return numeros

def buscar(arbol, n):
    lista = arbolalista(arbol)
    if n in lista:
        return True
    return False

print(buscar((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))),13))
print(buscar((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))),12))


def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num // 2) + str(num % 2)
def decimal_a_binario_sinr(num):
    if num <= 0:
        return "0"
    binario = ""
    while num > 0:
        resto = int(num % 2)
        num = int(num / 2)
        binario = str(resto) + binario
    return binario

print(decimal_a_binario_sinr(5))


def maximo_comun_divisor(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor(b, a % b)

def palindromas_sin_r(cadena):
  #Metemos la palabra en una lista
  cadena=list(cadena.lower())
  cadena_revertida=cadena[::-1]
  es_palindromo=0
  for x,y in zip(cadena,cadena_revertida):
    if x != y:
      es_palindromo+=1
  if es_palindromo == 0:
    return True
  return False
palindromas_sin_r('Sometemos')

def palindroma(Word):
    if len(Word) < 2:
        return True
    if Word[0] != Word[-1]:
        return False
    return palindroma(Word[1:-1])

print(palindroma("sometemos"))

cadena = "sometemos"
print(cadena[1:-1])

def sinDuplicados(lista):
    for i,valor in enumerate(lista):
        if lista.count(valor)>1:
            lista.pop(i)
    return lista
def sinDuplicados2(lista):
    sindup=[]
    for valor in lista:
        if valor not in sindup:
            sindup.append(valor)
    return sindup

def sinDuplicadosrecu(lista, sindup=[]):
    if len(lista)<2:
        return sindup
    else:
        if lista[0] not in sindup:
            sindup.append(lista[0])
        return sinDuplicadosrecu(lista[1::], sindup)

print(sinDuplicados([2,2,3,4,5,3]))
#[2,3,4,5]
print(sinDuplicados2([2,2,3,4,5,3]))
print(sinDuplicadosrecu([2,2,3,4,5,3]))

def funcion(cadena):
    c1=cadena[0:len(int(cadena/2))]
    c2=cadena[len(int(cadena)/2)+1::]
    for i in c1:
        print(i)
    for j in c2[::-1]:
        print(j)
    return c1,c2