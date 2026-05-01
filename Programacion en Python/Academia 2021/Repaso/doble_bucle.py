

print("+------------------+")
for i in range(5):
    print("|                  |")
print("+------------------+")


print("-"*10)
print("("+("0"*10)+")")


def cuadrado(n):
    print("+"+'-'*n*4+"+")
    for i in range(n):
        print('|'+(' '*((n*4)))+'|')
    print("+"+'-'*n*4+"+")

print(cuadrado(5))


def tabla_multiplicar():
    for i in range(1,11):
        for j in range(1,11):
            print(str(i)+' x '+str(j)+' = '+str(i*j))
        print()

#Llamada a la funcion
tabla_multiplicar()


#1- Estructuras de patrones
#2- Permuntaciones o combinaciones de elementos de dos listas
#3- Recorrer matrices

[[1,2,3],[4,5,6],[7,8,9]]

l1 = ["a","b","c"]
l2 = ["1","2","3"]

def combinaciones(l1,l2):
    lista = []
    for i in l1:
        for j in l2:
            lista.append(i + j)
    return lista

print(combinaciones(l1,l2))


