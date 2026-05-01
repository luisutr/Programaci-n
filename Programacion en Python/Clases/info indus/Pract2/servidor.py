# -*- coding: utf-8; mode: python -*-
from Seguridad import struc1 as st
from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM2")  # cambiar al puerto apropiado
# [a, b, result]
struct = [0, 0, 0.0]
r = [-1]  # a -1 para que no sea 0 y entre en el while
while r[0] !="0":
    print( "Esperando petición...")
    r = PuertoSerie.readline()
    r = r.decode()[0:-1]
    r = r.split(":")
    print( r )
    if r[0] =="1":  # Asignar A
        st.setA(struct, int(r[1]))
    elif r[0] =="2":  # Asignar B
        st.setB(struct, int(r[1]))
    elif r[0] =="3":  # minimo
        st.minimo(struct)
    elif r[0] =="4":  # maximo
        st.maximo(struct)
    elif r[0] =="5":  # media
        st.media(struct)
    elif r[0] =="6":  # peticion de result
        sendMensaje(PuertoSerie, str(st.getResult(struct)) +"\n" )
    elif r[0] =="7":  # envio de la estructura completa
        sendMensaje(PuertoSerie, str(struct) +"\n" )
    print("struct =", struct)