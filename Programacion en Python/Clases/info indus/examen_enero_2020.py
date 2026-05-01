# -*- coding: utf-8; mode: python -*-
from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM5")  # cambiar al puerto apropiado

print( "Esperando petición...")
while True:
    mensa = input("#opc:n_fil:n_col:M0,0,M0,1,M0,2:M1,0,M1,1,M1,2:M2,0,M2,1,M2,2 :M3,0,M3,1,M3,2: ")
    sendMensaje(PuertoSerie, mensa)
    #recibo resultado como 1:{B,2,D}:{D,6,E,A}”
    r = receiveMensaje(PuertoSerie)
    r = r.split(":")
    print(r)
    opc = r[0]
    if opc == "1":
        lista1 = r[1]
        lista2 = r[2]
        lista1 = lista1.split(",")
        lista2 = lista2.split(",")
        print(lista1, lista2)

