from mensaje import *
PuertoSerie = abrirPort( 'COM5' )

def menu():
    print("1) Operqación 1. ")
    print("2) Operación 2.")
    print("0) Para Salir")
    opc = input()
    return opc

o = ''
while o != '0':
    o = menu()
    if (o == '1'):
        a = input("dame un entero")
        b = input("dame otro entero")
        sendMensaje(PuertoSerie, o+";2;"+a+";"+b)
        print(receiveMensaje(PuertoSerie))
    if (o == '2'):
        N = input("Dame longitud del vector de float")
        vect=""
        for i in range(int(N)):
            if (i <= int(N)-1):
                vect += input("Dame un float tipo 0.0: ")+";"
            else:
                vect += input("Dame un float tipo 0.0: ")
        sendMensaje(PuertoSerie, o + ";" + N + ";" + vect)
        print(receiveMensaje(PuertoSerie))



    o = input('Desea continuar? (1 (Si) // 0 (No))')