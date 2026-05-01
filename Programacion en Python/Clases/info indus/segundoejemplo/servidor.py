# -*- coding: utf-8; mode: python -*-
from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM1")  # cambiar al puerto apropiado


while True:
    print( "Esperando petición...")
    r = receiveMensaje(PuertoSerie)
    r = r.split(":")
    opc = r[0]
    if opc == "1":
        lista = r[1]
        lista = lista.split(",")
        suma = 0
        for i in lista:
            if int(i)%2 == 0:
                suma += int(i)
        mensa = str(suma) + "\n"
        print(suma)
        sendMensaje(PuertoSerie, mensa)
    if opc == "2":
        lista = r[1]
        lista = lista.split(",")
        suma = 0
        for i in lista:
                suma += int(i)
        mensa = str(suma/len(lista)) + "\n"
        print(suma)
        sendMensaje(PuertoSerie, mensa)
