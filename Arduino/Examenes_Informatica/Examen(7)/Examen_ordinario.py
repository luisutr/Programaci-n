from mensaje import*

def menu():
    print("0-Salir")
    print("1-Encender")
    print("2-Apagar")
    return input("Elige una opción:")

PuertoSerie = abrirPort('COM3')

opc = '-1'

## Lista de leds ##
## Blanco = 0    ##
## Verde = 1     ##
## Amarillo = 2  ##
## Rojo = 3      ##

while opc != '0':
    opc = menu()
    mensa = opc + ':'
    mensa2 = opc + ':'
    mensa3 = opc + ':'
    leds = ""
    if opc == '1':
        N = input("Introduce el numero de leds que quieres encender:")
        mensa += N + ':'
        for i in range(int(N)):
            leds += input("Introduce segun el menu de leds cuales quieres encender:")
            mensa += leds + ':'
        sendMensaje(PuertoSerie, mensa + '\n')
        conf = receiveMensaje(PuertoSerie)
        print("------------------------------")
        print(conf)
        print("------------------------------")
    if opc == '2':
        sendMensaje(PuertoSerie, mensa2 + '\n')
        conf = receiveMensaje(PuertoSerie)
        print("------------------------------")
        print(conf)
        print("------------------------------")
    if opc == '3':
        print(leds)
        N = int(input("Introduce el numero de leds que desea comprobar: "))
        mensa3 += str(N) + ':'
        for i in range(N):
            mensa3 += input("Introduce los leds que desea comprobar: ") + ':'
        print(mensa3)
        sendMensaje(PuertoSerie, mensa3 + '\n')
        sendMensaje(PuertoSerie, leds + '\n')