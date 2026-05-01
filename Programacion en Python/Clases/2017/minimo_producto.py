__author__ = 'luis'


def producto_min (producto):
    for valor in reversed(range(2,10)):
        if producto%valor == 0:
            producto = producto / valor
    if producto == 1:
        yield valor
    else:
        yield producto_min(producto)

valor = producto_min(300)

for i in valor:
    print("valor: "+str(i))