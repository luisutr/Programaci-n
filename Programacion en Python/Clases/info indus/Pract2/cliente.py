# -*- coding: utf-8; mode: python -*-

from mensaje import *

def menu():
    print("0) Salir")
    print("1) Asignar A")
    print("2) Asignar B")
    print("3) Minimo")
    print("4) Maximo")
    print("5) Media")
    print("6) Recibir float resultado")
    print("7) Recibir struct completo")
    return input("Elige una opción: ")

# Abrimos el puerto del arduino a 9600
PuertoSerie = abrirPort("COM1")  # cambiar al correcto
# Creamos un buble que finaliza con "0"
opc = ""
while opc != "0":
    opc = menu()
    mensa = ""
    if opc == "0":
        mensa = "0\n"
        sendMensaje(PuertoSerie, mensa)
    elif opc == "1" or opc == "2":
        v = input("Dame el nuevo valor: ")
        mensa = opc + ":" + v + "\n"
        sendMensaje(PuertoSerie, mensa)
    elif opc >= "3" and opc <= "5":
        mensa = opc + "\n"
        sendMensaje(PuertoSerie, mensa)
    elif opc=="6" or opc=="7":
        mensa = opc + "\n"
        sendMensaje(PuertoSerie, mensa)
        # leer float o estructura desde servidor
        r = receiveMensaje(PuertoSerie)
        print( "struct =", r )