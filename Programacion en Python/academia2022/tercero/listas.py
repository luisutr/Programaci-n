


listas = [1,2,3,4, "luis", 0.3, True]


print(listas)
print(listas[4])
print(listas[-1])
print(listas[0])

#MODIFICAR

listas[0] = "Juan"
print(listas[0])
#AÑADIR
listas.append(99)
print(listas)

#ELIMINAR
listas.remove(99)
print(listas)

#SACAR O ELMINAR
listas.pop(0)
print(listas)
ultimo = listas.pop() # elimina la ultima si no le digo nada
print(listas)
print(ultimo)

listafantasma=[0,0,0,0,0]
enterofantasma = 0
def modifvecfantasma(L,e):
    e = 9
    for i in range(len(L)):
        L[i]=int(input("Dame nuevo numero: "))

modifvecfantasma(listafantasma,enterofantasma)

print(listafantasma)
print(enterofantasma)
