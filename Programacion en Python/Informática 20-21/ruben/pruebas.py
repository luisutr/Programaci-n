v1 = [1,2,3,4,5, "Luis", "Maria"]

for i in v1:
    if i == "Luis":
        print(i)

v2 = "Hola mundo"

#range(inicio,fin,salto)
#range(fin) inicio = 0
#raneg(inicio, fin) y toma salto de 1 en 1

for i in range(3, len(v2), 2):
    print(i, v2[i])


for i in range(len(v1)):
    if(i >= 3):
        print(i, v1[i])

for i,valor in enumerate(v1):
    print(i, valor)


print(8%2)


def suma_digitos(n):
    while(n>10):
        suma=0
        for i in str(n):
            suma += int(i)
        n = suma
    return n

print(suma_digitos(167))



