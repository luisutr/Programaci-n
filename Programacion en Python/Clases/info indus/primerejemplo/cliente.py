# -*- coding: utf-8; mode: python -*-

from mensaje import *

def menu():
    print("0) Salir")
    print("1) Enviar mensaje")
    return input("Escribe S + Intro para salir ")

# Abrimos el puerto del arduino a 9600
PuertoSerie = abrirPort("COM1")  # cambiar al correcto
# Creamos un buble que finaliza con "0"
opc = ""
opc = menu()
while opc != "S":
    mensa = ""
    if opc == "S":
        mensa = "0\n"
        sendMensaje(PuertoSerie, mensa)
    else:
        v = input("Escribe mensaje: ")
        mensa = v + "\n"
        sendMensaje(PuertoSerie, mensa)
        # leer float o estructura desde servidor
        r = receiveMensaje(PuertoSerie)
        if r == "Adios":
            opc = "S"
        print( r )