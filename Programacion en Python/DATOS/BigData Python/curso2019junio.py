def elsabio(years):
    nombre = "Luis"
    for letra in nombre:
        print(letra)
    # la siguiente linea convierte a cadena de texto
    years = str(years)
    suma = 0
    for numero in years:
        suma = suma + int(numero)
    print(suma)
    salir = input("quieres salir")
    while salir == "si":
        print("Adios")
        salir = input("quieres salir")
    return "Gracias por quedarte"


print(elsabio(36))