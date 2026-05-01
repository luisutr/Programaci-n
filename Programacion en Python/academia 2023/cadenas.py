cadena = "15 12 1982"
print(cadena[0])
print(cadena[-1])

ano = cadena[-4:]

if int(ano) > 2000:
    print("es mayor que 2000")
else:
    print("es menor")


print(list(range(99)))
print(list(range(1,21)))

print(list(range(2,42,2)))
print(len(list(range(2,42,2))))

def pares20():
    return list(range(2,42,2))

def posparesmenor20():
    lista = pares20()
    listapame20=[]
    suma=0
    for posicion,valor in enumerate(lista):
        if posicion%2==0:
            if suma+valor>=20:
                return listapame20
            else:
                suma += valor
                listapame20.append(valor)
    return listapame20

print(posparesmenor20())

