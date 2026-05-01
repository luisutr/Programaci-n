def divisors(n):
    lista = []
    for i in range(1, n + 1):
        if n % i == 0:
            lista.append(i)
    return lista
print(divisors(12)); # should return [2,3,4,6]
divisors(25); # should return [5]
divisors(13); # should return "13 is prime"

'''
El ácido desoxirribonucleico (ADN) es una sustancia química que se encuentra en el núcleo de las células
 y lleva las "instrucciones" para el desarrollo y funcionamiento de los organismos vivos.
Si quieres saber más: http://en.wikipedia.org/wiki/DNA
En las cadenas de ADN, los símbolos "A" y "T" son complementarios entre sí, como "C" y "G". 
Su función recibe un lado del ADN (cadena, excepto Haskell); necesitas devolver el otro lado complementario. 
La hebra de ADN nunca está vacía o no hay ADN en absoluto (de nuevo, a excepción de Haskell).
Más ejercicios similares se encuentran aquí: http://rosalind.info/problems/list-view/ (fuente)
Ejemplo: (entrada --> salida)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
'''

def DNA(cadena):
    resul=""
    for i in cadena:
        if i == "A":
            resul+="T"
        elif i == "T":
            resul+="A"
        elif i == "C":
            resul+="G"
        else:
            resul+="C"
    return resul

print(DNA("ATTGC"))

'''
¿Cuantas letras hay en la palabra que se repitan?
"increible"  --> 2 # letras duplicadas que son la i y la e
'''

def cuntaletrasdupli(cadena):
    n=0
    dupli=[]
    for i in cadena:
        if cadena.count(i)>1:
            if i not in dupli:
                n+=1
                dupli.append(i)
    return n

print(cuntaletrasdupli("increible"))

'''
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''

def filter_list(L):
    resul=[]
    for i in L:
        if type(i)==int:
            resul.append(i)
    return resul
print(filter_list([1,2,'a','b']))


'''
[1, 1, 2, 3, 1, 2, 3, 4], [1, 3] -> [2, 2, 4]
[1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2] -> [5, 6, 7, 8]
[8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3] -> [8, 7, 6, 5, 1]
'''

def removemark(L,l):
    resul = []
    for i in L:
        if i not in l:
            resul.append(i)
    return resul
print(removemark([1, 2, 3, 4, 5], [1, 2]))

'''
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
createDict(keys, values)
'''