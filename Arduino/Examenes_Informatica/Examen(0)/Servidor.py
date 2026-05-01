# Importamos la libreria de PySerial y mensaje

import serial
from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort( 'COM5' ) #En mi caso es COM5, cambiar si fuera necesario
while True: # Creamos un buble sin fin
    print("Esperando....")
    r = receiveMensaje(PuertoSerie)
    r_nuevo=r.split(':')
    if r_nuevo[0]=='+': #Aplica la suma de 1 al numero que le pasamos
        print('La respuesta recibida es sumar: ', int(r_nuevo[1])+1)
    if r_nuevo[0]=='-': #Aplica la resta de 1 al numero que le pasamos
        print('La respuesta recibida es restar: ', int(r_nuevo[1])-1)
    else: #Si ocurre un error lanza el siguiente mensaje:
        print( 'Vuelve a introducir los datos' )

    # añade "_RR" y envía
    sendMensaje(PuertoSerie,r+'_RR\n')

    # Espera mensaje de confirmación
    r1 = receiveMensaje(PuertoSerie)
    print( 'Respuesta recibida segunda: ', r1 )