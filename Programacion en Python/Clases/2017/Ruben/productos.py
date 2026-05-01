__author__ = 'Luis'


def compra(lista1,lista2,dinero):
    productos=[]

    while dinero > min(lista2):
        for i in range(len(lista2)):
            if (dinero-lista2[i])>0:
                dinero -= lista2[i]
                productos.append(lista1[i])
    return productos

print compra(["Peras", "Manzanas", "Uvas"], [0.80,0.50,0.30],2)
