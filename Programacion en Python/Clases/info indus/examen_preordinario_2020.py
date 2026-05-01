

# -*- coding: utf-8; mode: python -*-
from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM5")  # cambiar al puerto apropiado

print( "Esperando petición...")
while True:
    mensa = input("Estre esos caractres escribe los valores del mensaje de esta manera: opc#N#int1*int2*int3*intN#int1*int2*int3*intN:\\n")
    sendMensaje(PuertoSerie, mensa)
    #le ha mandado a node el mensaje, node lo opera y me devuelve el vector para calcular la media
    r = receiveMensaje(PuertoSerie)
    r = r[0:-2]
    r = r.split("#")
    print(r)
    opc = r[0]
    if opc == "1":
        tam = r[1]
        lista = r[2]
        lista = lista.split("*")
        print(lista)
        suma = 0.00
        for i in lista:
                suma += float(i)
        media = suma / len(lista)
        print(media)
        mensa = str(media)+"/n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)
    if opc == "2":
        lista = r[1]
        lista = lista.split(",")
        suma = 0
        for i in lista:
            if i.strip():
                suma += float(i)
        media = suma/len(lista)
        print(media)
        mensa = str(media) + "\n"
        print(suma)
        sendMensaje(PuertoSerie, mensa)
