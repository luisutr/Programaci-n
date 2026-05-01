# -*- coding: utf-8; mode: python -*-

from mensaje import *

def menu():
    print("0) Salir")
    print("1) Vector leds")
    return input("Escribe opción: ")

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM3")  # cambiar al correcto
# Creamos un buble que finaliza con "0"
opc = ""
opc = menu()
while opc != "0":
    if opc == "1":
        vector = input("Dame vector tipo 0,1,1,0: ")
    mensa = opc+":"+vector+"\n"
    sendMensaje(PuertoSerie, mensa)
    r = receiveMensaje(PuertoSerie)
    print(r)
    input("Presiona Enter para continuar")
    opc = menu()
print("Gracias por usar el programa")