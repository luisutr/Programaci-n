frutas = ["manzana", "peras", "albaricoque", "naranjas", "uvas", "fresas", "mandarina"]
print(frutas[1:len(frutas)])
pesos = [6,5,3,7,1,2,4]

print(list(range(2,22,5)))
print(list(range(7)))

#RECORRER POR POSCIONES
for posicion, valor in enumerate(frutas):
    print(posicion, valor)

for i in range(len(frutas)):
    print(i, frutas[i])

# ordenar las frutas de menor a mayor segun peso

'''
1 recorro y guardo el mas pequeño, y lo guardo  
2 recorro otra vez y guardo el mas pequeño (voy preguntando si ya lo tengo tengo guardado, si lo tengo no lo quiero)
3. asi sucesivamente cuando la lista donde voy guardando se igual HASTA longitud de la origiinal he acabdo 
'''
def ordenalisa(p, f):
    ordenado=[]
    frutasordenadas = []
    long = len(p)
    while(len(ordenado)<long):
        minimo = calculaminimo(p)
        ordenado.append(minimo)
        frutasordenadas.append(frutas[pesos.index(minimo)])
        p.pop(p.index(minimo))
    return ordenado,frutasordenadas

def calculaminimo(p):
    minimo = 99
    for i in p:
        if i < minimo:
            minimo = i
    return minimo

print(ordenalisa([6,5,3,7,1,2,4], ["manzana", "peras", "albaricoque", "naranjas", "uvas", "fresas", "mandarina"]))


p = [6,5,3,7,1,2,4]
p.sort()
print(p)
listafrutasor = []
for i in p:
    listafrutasor.append(frutas[pesos.index(i)])
print(listafrutasor)
frutas = ["manzana", "peras", "albaricoque", "naranjas", "uvas", "fresas", "mandarina"]

print(list(range(7)))
print(list(range(1,7)))