# -*- coding: utf-8; mode: python -*-
from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM1")  # cambiar al puerto apropiado

opc = "X"
while True and opc != "S":
    print( "Esperando petición...")
    r = receiveMensaje(PuertoSerie)
    if r == "0":
        opc = "S"
        r = "Adios muy buenas!"
    print(r)
    v = input("Escribe mensaje: ")
    mensa = v + "\n"
    sendMensaje(PuertoSerie, mensa )
