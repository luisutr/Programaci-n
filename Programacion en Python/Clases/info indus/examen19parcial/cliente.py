# -*- coding: utf-8; mode: python -*-

from mensaje import *

def menu():
    print("0) Salir")
    print("1) Enviar mensaje")
    return input("Escribe S + Intro para salir ")

# Abrimos el puerto del arduino a 9600
PuertoSerie = abrirPort("COM5")  # cambiar al correcto
# Creamos un buble que finaliza con "0"
opc = ""
opc = menu()
while opc != "0":
    mensa = ""
    if opc == "0":
        mensa = "0\n"
        cerrarPort(PuertoSerie)
        sendMensaje(PuertoSerie, mensa)
    elif opc == "1":
        num = input("Dame numero para vector enteros: ")
        vector = ""
        for i in range(int(num)):
            vector += input("Dame entero: ")+":"
        mensa = opc+":"+num+":"+vector[0:-1]
        sendMensaje(PuertoSerie, mensa)
        # leer float o estructura desde servidor
        r = receiveMensaje(PuertoSerie)
        print(r)
    elif opc == "2":
        v = input("Escribe mensaje: ")
        mensa = v + "\n"
        sendMensaje(PuertoSerie, mensa)
        # leer float o estructura desde servidor
        r = receiveMensaje(PuertoSerie)
        if r == "Adios":
            opc = "S"
        print(r)
    elif opc == "3":
        v = input("Escribe mensaje: ")
        mensa = v + "\n"
        sendMensaje(PuertoSerie, mensa)
        # leer float o estructura desde servidor
        r = receiveMensaje(PuertoSerie)
        if r == "Adios":
            opc = "S"
        print( r )