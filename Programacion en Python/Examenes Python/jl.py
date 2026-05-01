def vocales_a_numeros(palabra):
    resultado=[]
    for i in palabra:
        if i in "aeiouAEIOU":
            if i=='a' or i=='A':
                resultado.append(4)
            if i=='e' or i=='E':
                resultado.append(3)
            if i=='o' or i=='O':
                resultado.append(0)
            if i=='i' or i=='I':
                resultado.append(1)
        else:
            resultado.append(i)
    return resultado
####print vocales_a_numeros('Examen')



def iniciales(cadena):
    lista=[]
    for i in range(len(cadena)):
        if i==0:
            lista.append(cadena[0])
        if cadena[i]== " ":
            lista.append(cadena[i+1])
    return " ".join(str(x)for x in lista)
####print iniciales("la frase de prueba")

from numpy import trace
def traza(m):
    return trace(m)

##print traza([[1,2,3],[4,5,6],[7,8,9]])
### traza ([[1,0,0],[0,1,0],[0,0,1]])

def larga(lista):
    contador =0
    aux = ""
    for i in lista:
            if contador < len(i):
                contador = len(i)
                aux = i
    return aux
####print larga(["la", "palabra", "mas", "larga"])

def traza1(m):
    suma=0
    countador=0
    for i in m: ## i tiene la primera lista
        if countador <= len(i):
            suma += i[countador]
            countador += 1
    return suma
#### traza1([[1,2,3],[4,5,6],[7,8,9]])


def riman(a,b):
    longa=len(a)-1
    longb=len(b)-1
    rima=0
    if a[longa]!= b[longb]:
        return "no riman"
    for i in range(3):
        if a[longa-i]== b[longb-i]:
            rima += 1
    if rima == 3:
        return "Riman"
    elif rima == 2:
        return "Riman un poco"
    else:
        return "no riman"

print riman("cabra","cara")