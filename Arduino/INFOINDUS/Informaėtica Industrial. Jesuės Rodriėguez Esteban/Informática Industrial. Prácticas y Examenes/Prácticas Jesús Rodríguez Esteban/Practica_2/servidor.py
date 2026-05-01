# -*- coding: utf-8; mode: python -*-
import struc as st
from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM2")  # cambiar al puerto apropiado
# [a, b, result]
struct = [" ", " "] #Definimos de esra forma el struc por comodidad-[0] corresponde a A y [1] a r
r = [-1]  # a -1 para que no sea 0 y entre en el while
while r[0] !="0":
    print( "Esperando petición...")  #Esperará petición hasta que introduzcamos una de las ordenes
    r = PuertoSerie.readline()
    r = r.decode()[0:-1]
    r = r.split(":")
    print( r )
#Describimos la estructura en la opción 1 pero son idénticas en las demás opciones
    if r[0] =="1":  #Sumador y Sumario
        st.setA(struct, r[1])  #Fijamos el valor de a
        st.sumatorio(struct)  #Función que se encarga de resolver la orden elegida
        sendMensaje(PuertoSerie, str(st.getResult(struct)) + "\n")  #Envía mensaje y almacena

    elif r[0] =="2":  #Cuadrados
        st.setA(struct, r[1])
        st.cuadrados(struct)
        sendMensaje(PuertoSerie, str(st.getResult(struct)) + "\n")

    elif r[0] =="3":  #Contar letras
        st.setA(struct, r[1])
        st.contar_n(struct)
        sendMensaje(PuertoSerie, str(st.getResult(struct)) + "\n")

    elif r[0] =="4":  #Palindromo
        st.setA(struct, r[1])
        st.palindromo(struct)
        sendMensaje(PuertoSerie, str(st.getResult(struct)) + "\n")

    elif r[0] == "5":  # Devolución última orden
        sendMensaje(PuertoSerie, str(st.getResult(struct)) + "\n")
