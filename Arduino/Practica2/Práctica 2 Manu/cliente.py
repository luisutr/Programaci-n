from mensaje import *
def menu():
    print("0) Salir")
    print("B) Asignar A")
    print("A) Asignar B")
    print("S) Suma")
    print("R) Resta")
    print("M) Multiplicar")
    print("D) Dividir")
    print("O) Recibir float resultado")
    print("L) Recibir struct completo")
    return input('Elige una opción: ')

# Abrimos el puerto del arduino a 9600
PuertoSerie = abrirPort('COM1')

# Creamos un buble que finaliza con '0'
opc = ''
while opc != '0':
    opc = menu()
    mensa = ''
    if opc=='0':
        mensa = '0\n'
        sendMensaje(PuertoSerie, mensa)
    elif opc=="A":
        a=input("dame valor de a:")
    elif opc=="B":
        b=input("dame valor de b:")
    elif opc == 'S' or opc == 'R' or opc == 'M' or opc == 'D':
        mensa = "["+opc+"]-"+a+";"+b+'\n'
        sendMensaje(PuertoSerie, mensa)
    elif opc == 'O' or opc == 'L':
        mensa = opc + '\n'
        sendMensaje(PuertoSerie, mensa)
        # leer float o estructura desde servidor
        r = receiveMensaje(PuertoSerie)
        print('struct =', r)
