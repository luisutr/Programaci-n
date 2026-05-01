lista = [2,5,6,2,1,0,9]
tupla = (2,3)
print(len(lista))
print(tuple(lista))
print(list(tupla))


'''
append(valor) inserta al final 
insert(posicion, valor)
pop(), pop(posicion) sacar el ultimo elemento
remove(posicion)
reversed() --> te da la vuelta a una lista 
find(valor) --> devuelve la primera posicion que encuentra 
sort() -- > oredena una lista 
'''

#RECORRER LISTAS

#recorrido por valor
for i in lista:
    print(i)
#recorrido por posicion
for i in range(len(lista)):
    print("posicion: ",i)
    print("valor: ", lista[i])

print("RECORRIDO con enumerate ")

for i,v in enumerate(lista):
    print("posicion: ", i)
    print("Valor: ", v)

#recorrido con while
cont = 0
while(cont < len(lista)):
    print(lista[cont])
    cont += 1 # cont = cont + 1
print("LISTAS DOBLES")
listadoble = [1,2,[3,4,5], "abcd", 0.7]
for j in listadoble:
    if type(j) == list:
        for k in j:
            print(k)
    elif type(j) == str:
        for x in j:
            print(x)
    else:
        print(j)


def delistaastring(list1):
    str1 = ''.join(str(e) for e in list1)
    return str1
def destringalista(cadena):
    lista = []
    for i in cadena:
        lista.append(i)
    return lista
