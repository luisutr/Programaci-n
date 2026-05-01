#!/usr/bin/python
 
# Importamos la libreria de PySerial
import serial
from mensaje import *

# Abrimos el puerto del arduino a 115200
#PuertoSerie = abrirPort( '/dev/ttyUSB0' )
PuertoSerie = abrirPort( 'COM5', 115200 )

# Creamos un buble sin fin
while True:
    print("Esperando....")
    r = receiveMensaje(PuertoSerie)
    print( 'Respuesta recibida: ', r )
    # añade "_RR" y envía
    sendMensaje(PuertoSerie,r+'_RR')
    # Espera mensaje de confirmación
    r1 = receiveMensaje(PuertoSerie)
    print( 'Respuesta recibida segunda: ', r1 )

