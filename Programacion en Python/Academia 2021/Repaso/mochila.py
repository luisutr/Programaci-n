#va comprando si el primero que encuentro tengo dinero
def mochila_ineficionte(pasta):
    compra=[] # productos
    productos = ["pan", "vino", "cocacola", "hielo", "pipas", "ron"]
    precios = [0.60, 1, 1.50, 1, 0.25, 12]
    for i in range(len(precios)):
        if pasta > precios[i]:
            compra.append(productos[i])
            pasta-=precios[i]
    return compra
print("MOCHILA INEFICIENTE")
print("####################")
print(mochila_ineficionte(3))
print(mochila_ineficionte(5))
print(mochila_ineficionte(17))

def mochila_eficiente_sort(pasta):
    compra=[] # productos
    productos = ["pan", "vino", "cocacola", "hielo", "pipas", "ron"]
    precios = [0.60, 1, 1.50, 1, 0.25, 12]
    #hacemos copia de lista
    preciosordenados = []
    for p in precios:
        preciosordenados.append(p)
    preciosordenados = list(sorted(preciosordenados))
    for precio in preciosordenados:
        if pasta > precio:
            posicionprecio = precios.index(precio)
            compra.append(productos[posicionprecio])
            pasta-=precio
    return compra
print("MOCHILA EFICIENTE CON SORT")
print("##########################")
print(mochila_eficiente_sort(3))
print(mochila_eficiente_sort(5))
print(mochila_eficiente_sort(17))
# 5€ --> [pan, vino, cocacola, hielo, pipas]


def mochilaeficiente_min(pasta):
    productos = ["pan", "vino", "cocacola", "hielo", "pipas", "ron"]
    precios = [0.60, 1, 1.50, 1, 0.25, 12]
    compra=[] # productos
    while(pasta>min(precios) or len(compra)<len(productos)):
        minimo = min(precios)
        posmin = precios.index(minimo)
        if pasta > minimo:
            compra.append(productos[posmin])
            pasta-=minimo
            productos.pop(posmin)
            precios.pop(posmin)
    return compra
print("MOCHILA EFICIENTE COGE PRECIO MIN")
print("##################################")
print("*",mochilaeficiente_min(2))