from mensaje import*

def menu():
    print("0-Salir")
    print("E-Escribir")
    print("B-Borrar")
    return input("Elige una opción:")

PuertoSerie = abrirPort('COM3')

opcion = '-1'

while opcion != '0':
    opcion = menu()
    mensaje = opcion + '|'

    if opcion == "E":
        N = input("Introduzca el numero de posiciones:")
        mensaje += N + '|'
        for i in range(int(N)):
            mensaje += input("Introduce la fila :") + ','
            mensaje += input("Introduce la columna :") + '|'
        sendMensaje(PuertoSerie, mensaje[:-1] + '\n')
        print(mensaje)
        OK = receiveMensaje(PuertoSerie)
        print(OK)
    if opcion == "B":
        N = input("Introduzca el numero de posiciones:")
        mensaje += N + '|'
        for i in range(int(N)):
            mensaje += input("Introduce la fila :") + ','
            mensaje += input("Introduce la columna :") + '|'
        sendMensaje(PuertoSerie, mensaje[:-1] + '\n')
        print(mensaje)
        OK = receiveMensaje(PuertoSerie)
        print(OK)