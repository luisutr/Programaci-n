from mensaje import*

def menu():
    print("0-Salir")
    print("1-Cuadrados")
    print("2-Media")
    print("3-Pares")
    print("4-S.Lista")
    return input("Elige una opción:")

PuertoSerie = abrirPort('COM3')

opc = '-1'

while opc != '0':
    opc = menu()
    if opc == '1':
        sendMensaje(PuertoSerie, opc + '\n')
        N = int(input("¿Cuantos números vas a introducir?:"))
        sendMensaje(PuertoSerie, str(N) + '\n')
        num = ""
        for i in range(N):
            num += input("Introduce los numeros que desea operar:") + ":"
        sendMensaje(PuertoSerie, num + '\n')
        result = receiveMensaje(PuertoSerie)
        print(result)
    if opc == '2':
        sendMensaje(PuertoSerie, opc + '\n')
        N = int(input("Indique cuantos números de tipo float introducira:"))
        sendMensaje(PuertoSerie, str(N) + '\n')
        num = ""
        for i in range(N):
            num += input("Introduce los números decimales que quieres introducir:") + ":"
        sendMensaje(PuertoSerie, num + '\n')
        result = receiveMensaje(PuertoSerie)
        print(result)
    if opc == '3':
        sendMensaje(PuertoSerie, opc + '\n')
        cadena = (input("Introduce la cadena de caracteres:"))
        sendMensaje(PuertoSerie, cadena + '\n')
        result = receiveMensaje(PuertoSerie)
        print(result)
        conf = "------ACK-------"
        sendMensaje(PuertoSerie, conf + '\n')
    if opc == '4':
        sendMensaje(PuertoSerie, opc + '\n')
        N = input("Introduce la cantidad de numeros:")
        mensa = N + ":"
        for i in range(int(N)):
            mensa += input("Introduce los numeros:") + ":"
        sendMensaje(PuertoSerie, mensa + '\n')
        lista = receiveMensaje(PuertoSerie)
        lista = lista.split(";")
        sumador = 0
        for i in lista:
            sumador += int(i)
        print(sumador)
        sendMensaje(PuertoSerie, str(sumador) + '\n')
        conf = receiveMensaje(PuertoSerie)
        print(conf)