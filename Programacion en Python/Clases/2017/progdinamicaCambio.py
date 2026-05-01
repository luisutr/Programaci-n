matrizCambio = 0
vectorMonedas = 0
cantidad = 0
vectorSeleccion = 0


def calcularMonedas(cantidad, monedas):
    # matrizCambio = new int[monedas.length + 1][cantidad + 1];

    for i in range(len(monedas)):
        matrizCambio[i][0] = 0

    for j in cantidad:
        matrizCambio[0][j] = 99;

    for i in range(len(monedas)):
        for j in cantidad:
            if (j < monedas[i - 1]):

                matrizCambio[i][j] = matrizCambio[i - 1][j]
            else:
                minimo = 0
                minimo = min(matrizCambio[i - 1][j], matrizCambio[i][j - monedas[i - 1]] + 1)
                matrizCambio[i][j] = minimo
    return matrizCambio


def seleccionarMonedas(c, monedas, tabla):
    i, j = 0, 0
    seleccion = []
    for i in range(len(monedas)):
        seleccion[i] = 0;
    i = monedas.length;
    j = c;
    while (j > 0):
        if (i > 1 and tabla[i][j] == tabla[i - 1][j]):
            i -= 1
        else:
            seleccion[i - 1] += 1
            j = j - monedas[i - 1]
    return seleccion


def Cambio(cantidad, monedas):
    cantidad = cantidad
    vectorMonedas = monedas
    matrizCambio = calcularMonedas(cantidad, monedas)
    vectorSeleccion = seleccionarMonedas(cantidad, monedas, matrizCambio)


def min(a,b):
    if (a < b):
        return a
    else:
        return b

c = Cambio(12, [1, 6, 10])
