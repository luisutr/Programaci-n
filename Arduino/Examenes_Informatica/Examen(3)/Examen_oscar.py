from mensaje import*
def menu():
    print("0-Salir")
    print("DL")
    print("BL")
    return input("Seleccione una opción:")
PuertoSerie = abrirPort('COM3')
opcion = '-1'
while opcion != '0':
    opcion = menu()
    envio = opcion + '-'
    if opcion == "DL":
        envio += input("Introduce la fila origen:") + ','
        envio += input("Introduce la columna origen:") + '-'
        envio += input("Introduce la fila destino:") + ','
        envio += input("Introduce la columna destino:")
        sendMensaje(PuertoSerie, envio + '\n')
        ACK = receiveMensaje(PuertoSerie)
        print(ACK)
    if opcion == "BL":
        envio += input("Introduce la fila origen:") + ','
        envio += input("Introduce la columna origen:") + '-'
        envio += input("Introduce la fila destino:") + ','
        envio += input("Introduce la columna destino:")
        sendMensaje(PuertoSerie, envio + '\n')
        ACK = receiveMensaje(PuertoSerie)
        print(ACK)