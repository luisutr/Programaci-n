from mensaje import*

def menu():
    print("0-Salir")
    print("DL-Dibujar linea")
    print("BL-Borrar linea")
    return input("Elige una opción:")

PuertoSerie = abrirPort('COM3')

opc = '-1'

while opc != '0':
    opc = menu()
    mensa = opc + '-'

    if opc == "DL":
        mensa += input("Introduce la fila origen:") + ','
        mensa += input("Introduce la columna origen:") + '-'
        mensa += input("Introduce la fila destino:") + ','
        mensa += input("Introduce la columna destino:") + ' '
        print(mensa)
        sendMensaje(PuertoSerie, mensa + '\n')
        conf = receiveMensaje(PuertoSerie)
        print("---------------------------------")
        print(conf)
        print("---------------------------------")

    if opc == "BL":
        mensa += input("Introduce la fila origen:") + ','
        mensa += input("Introduce la columna origen:") + '-'
        mensa += input("Introduce la fila destino:") + ','
        mensa += input("Introduce la columna destino:") + ' '
        print(mensa)
        sendMensaje(PuertoSerie, mensa + '\n')
        conf = receiveMensaje(PuertoSerie)
        print("---------------------------------")
        print(conf)
        print("---------------------------------")

    if opc == "R":
        mensa += input("Introduce la fila origen:") + ','
        mensa += input("Introduce la columna origen:") + '-'
        mensa += input("Introduce la fila destino:") + ','
        mensa += input("Introduce la columna destino:") + ' '
        print(mensa)
        sendMensaje(PuertoSerie, mensa + '\n')
        conf = receiveMensaje(PuertoSerie)
        print("---------------------------------")
        print(conf)
        print("---------------------------------")