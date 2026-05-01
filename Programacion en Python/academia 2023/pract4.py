def iter_enlazadas(n):
    for i in range(n):
        rango=(str(list(range(i+1))))
        print(str(i+1)+":"+rango[1:-1]+",")

iter_enlazadas(5)
'''
rango=(str(list(range(5))))
print(rango[:-2])
print(rango[0:-2])
print(rango[1:-2])
print(rango[2:])
print(rango[2:-1])
print(rango[0])
print(rango[-2])
'''

def quitocomas(cadena):
    s=""
    for i in cadena:
        if i != ",":
            s+=i
    return s
def tabla_suma(n,m):
    for i in range(1,10):
        rango=(str(list(range(i+n,i+m+1))))
        s = quitocomas(rango)
        print(str(i)+": "+s[1:-1])

tabla_suma(3,5)


print(str(list(range(5,17))))

# d) Devuelva una nueva lista con las posiciones en las que se encuentran los valores pares en L.
def recorrer_d(L):
    nueva=[]
    for i in range(len(L)):
        if L[i]%2==0:
            nueva.append(i)
    return nueva

def factorial(n):
    fact=1;
    for i in range(1,n+1):
        fact*=i
    return fact

def factoriales(L):
    resul=[]
    for i in L:
        resul.append(factorial(i))
    return resul

print(factoriales([5, 2, 6, 12, 4]))

def cuenta_vocales(cadena):
  resul=[]
  vocales="aeiou"
  for vocal in vocales:
    cuantashay = 0
    for i in cadena:
        if i == vocal:
            cuantashay+=1
    resul.append(cuantashay)
  return resul

print(cuenta_vocales("esta cadena"))

def espaciados(cadena):
    resul=""
    for i in cadena:
        resul+=i+" "
    return resul

def maslarga(frase):
    max=0
    for palabra in frase:
        if max<len(palabra):
            max = len(palabra)
    return  max

def separa(frase):
    #frase = frase[:-1]
    frase = frase.strip(".")
    palabras = frase.split(" ")
    max = maslarga(palabras)+1
    for palabra in palabras:
        print(palabra +(max-len(palabra))*" "+" - Palabra de " +str(len(palabra))+" caracteres: "+espaciados(palabra))

separa("Esta frase es una prueba.")



