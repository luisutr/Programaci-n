# -*- coding: utf-8; mode: python -*-

from mensaje import *

def menu():
    print("0) Salir")
    print("1) Dal la vuelta a cadena")
    print("2) Poner en mayusculas")
    return input("Escribe opción: ")

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM3")  # cambiar al correcto
# Creamos un buble que finaliza con "0"
opc = ""
opc = menu()
while opc != "0":
    mensa = ""
    if opc == "1":
        mensa = opc+":"+input("Escribe cadena de texto: ")+":"+"\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)
    if opc == "2":
        mensa = opc + ":" + input("Escribe cadena de texto: ") + ":" + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)
    opc = menu()
print("Gracias por usar el programa")