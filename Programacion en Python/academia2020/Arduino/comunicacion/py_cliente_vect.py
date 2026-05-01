#!/usr/bin/python

# Importamos la libreria de PySerial
import serial
from mensaje import *

# Abrimos el puerto del arduino a 115200
# PuertoSerie = abrirPort( '/dev/ttyUSB0' )
PuertoSerie = abrirPort('COM3', 115200)

def menu():
    print("1 - Calcular suma del vector")
    print("2 - Calcular media del vector")
    print("3 - Salir")

# Creamos un buble sin fin
while True:
    print("Esperando....")
    long = input("Dame la longitud del vector: ")
    vect = input("Dame el vector separado por : cada nuemro: ")
    menu()
    op = input("Slecciona opcion: ")
    r = op+":"+long+":"+vect
    sendMensaje(PuertoSerie, r)
    # Espera mensaje de confirmación
    r1 = receiveMensaje(PuertoSerie)
    print('Respuesta recibida segunda: ', r1)

