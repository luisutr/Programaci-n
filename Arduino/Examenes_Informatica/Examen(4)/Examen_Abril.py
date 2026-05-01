from mensaje import*

def menu():
    print("0-Salir")
    print("1-Apagar")
    print("2-Encender")
    print("3-Lista")
    print("4-Aleatorio")
    return input("Elige una opción:")

PuertoSerie = abrirPort('COM3')

opc = '-1'

while opc != '0':
    opc = menu()
    mensa = opc + ':'

    if opc == "1":
        sendMensaje(PuertoSerie, mensa + '\n')
        res = receiveMensaje(PuertoSerie)
        print("------------------------------------------------")
        print(res)
        print("------------------------------------------------")

    if opc == "2":
        col = input("Introduce la columna que desea encender:") + ':'
        mensa += col
        sendMensaje(PuertoSerie, mensa + '\n')
        res = receiveMensaje(PuertoSerie)
        print("------------------------------------------------")
        print(res)
        print("------------------------------------------------")

    if opc == "3":
        N = input("Introduzca el numero de columnas que desea encender:")
        mensa += N + ':'
        for i in range(int(N)):
            col = input("Introduce las columnas que desea encender:") + ':'
            mensa += col
        sendMensaje(PuertoSerie, mensa + '\n')
        res = receiveMensaje(PuertoSerie)
        print("------------------------------------------------")
        print(res)
        print("------------------------------------------------")
        conf = "ACK"
        sendMensaje(PuertoSerie, conf + '\n')

    if opc == "4":
        N = input("Introduzca el numero de columnas que quieres encender:")
        mensa += N + ':'
        sendMensaje(PuertoSerie, mensa + '\n')
        res = receiveMensaje(PuertoSerie)
        print("------------------------------------------------")
        print(res)
        print("------------------------------------------------")
        conf = "ACK"
        sendMensaje(PuertoSerie, conf + '\n')

