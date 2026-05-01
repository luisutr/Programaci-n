#!/usr/bin/python
 
# Importamos la libreria de PySerial
import serial
from mensaje import *

# Abrimos el puerto del arduino a 115200
#PuertoSerie = abrirPort( '/dev/ttyUSB0' )
PuertoSerie = abrirPort( 'COM4', 115200 )

# Creamos un buble sin fin
while True:
    print("Esperando....")
    r = receiveMensaje(PuertoSerie)
    print( 'Orden recibida: ', r )
    # añade "_RR" y envía
    result = 'no_result'
    l = r.split(':')
    print(l)
    if l[1]=='+': result = int(l[0])+int(l[2])
    if l[1]=='-': result = int(l[0])-int(l[2])
    if l[1]=='*': result = int(l[0])*int(l[2])
    if l[1]=='%': result = int(l[0])%int(l[2])

    sendMensaje(PuertoSerie,str(int(result)))

