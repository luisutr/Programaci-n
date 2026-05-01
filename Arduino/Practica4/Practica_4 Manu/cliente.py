# -*- coding: UTF-8 -*-
################################ AL EJECUTAR POR PRIMERA VEZ EL PROGRAMA DA UNA FALLO DE MEMORIA ######################################
############## SEGUIDAMENTE SI SE VUELVE A EJECUTAR EL PROGRAMA FUNCIONA CORECTAMENTE SIN NINGUN TIPO DE FALLO ###############
from mensaje import *

def menu():
    print("\n")
    print("0) Salir")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicar")
    print("4) Dividir")
    return input("Seleccione una opc: ")

PuertoSerie = abrirPort("COM3")  #Seleccionamos el puerto COM3#

opc = ""
while opc != "0":  #Cuando pulsamos el 0 salimos
    opc = menu()
    mensa = ""
    if opc == "0":
        mensa = "0\n"
        sendMensaje(PuertoSerie, mensa)
    if opc == "1":
        va = input("Introduce valor de a: ")
        vb = input("Introduce valor de b: ")
        mensa = opc + ":" + va + "," + vb + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)
    elif opc == "2":
        va = input("Introduce valor de a:")
        vb = input("Introduce valor de b:")
        mensa = opc + ":" + va + "," + vb + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)

    elif opc == "3":
        va = input("Introduce valor de a:")
        vb = input("Introduce valor de b:")
        mensa = opc + ":" + va + "," + vb + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)

    elif opc == "4":
        va = input("Introduce valor de a:")
        vb = input("Introduce valor de b:")
        mensa = opc + ":" + va + "," + vb + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)

