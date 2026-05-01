# -*- coding: utf-8; mode: python -*-

from mensaje import *

def menu():
    print("0) Salir")
    print("1) Suma pares de un vector")
    print("2) Media de un vector")
    return input("Escribe S + Intro para salir ")

# Abrimos el puerto del arduino a 9600
PuertoSerie = abrirPort("COM5")  # cambiar al correcto
# Creamos un buble que finaliza con "0"
opc = ""
while opc != "S":
    opc = menu()
    mensa = ""
    listac = input("dame los numeros separados por coma")
    lista = listac.split(",")
    long = str(len(lista))
    if opc == "S":
        mensa = "0\n"
        sendMensaje(PuertoSerie, mensa)
    elif opc == "1":
        mensa = opc +":"+long+":"+ listac + "\n" # Siempre envio cadenas de texto
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)
    elif opc == "2":
        mensa = opc +":"+long+":"+ listac + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)