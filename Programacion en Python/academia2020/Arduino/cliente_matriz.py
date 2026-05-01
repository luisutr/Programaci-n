#!/usr/bin/python

# Importamos la libreria de PySerial
import serial
from mensaje import *

# Abrimos el puerto del arduino a 115200
# PuertoSerie = abrirPort( '/dev/ttyUSB0' )
PuertoSerie = abrirPort('COM3', 115200)

def menu():
    print("1 - Enviar matriz y devuelve diagonal")
    print("2 - Salir")

# Creamos un buble sin fin
while True:
    r = ""
    print("Esperando....")
    menu()
    op = input("Dame una opcion:  ")
    if op == "1":
        dimesion = int(input("Dame la dimension de la matriz cuadrada: "))
        sendMensaje(PuertoSerie, str(dimesion))
        r = receiveMensaje(PuertoSerie)
        if r == "ok":
            for i in range(dimesion):
                fila=""
                print("A continuacion dame lo numeros de la fila "+str(i))
                for j in range(dimesion):
                    elemento = input("Da numero")
                    fila+=elemento+","
                sendMensaje(PuertoSerie, fila[0:-1])
                r = receiveMensaje(PuertoSerie)
                print(r)
    # Espera mensaje de confirmación
    r = receiveMensaje(PuertoSerie)
    puntos = input(r)
    sendMensaje(PuertoSerie, puntos)
    diagonal = receiveMensaje(PuertoSerie)
    print('La diagonal de la Matriz es: ', diagonal)

