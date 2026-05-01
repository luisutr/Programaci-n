# -*- coding: utf-8; mode: python -*-
from Seguridad.mensaje import *

PuertoSerie = abrirPort( "COM11" ) #Abrimos el puerto a 115200
# Creamos un buble sin fin
while True:
    s = input("Envia un comentario: ")
    sendMensaje(PuertoSerie,s) # Envía un mensaje (mensaje.py)
    print( "Esperando recibir ... " )
    r = receiveMensaje(PuertoSerie) # Recibe un mensaje (mensaje.py)
    print( "Respuesta recibida: ", r )