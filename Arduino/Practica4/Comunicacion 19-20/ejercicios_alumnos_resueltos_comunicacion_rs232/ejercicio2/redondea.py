# Importamos la libreria de PySerial
from mensaje import *

# lee un vector como una lista
def leerVector(tam):
    s = ''
    for i in range(tam):
        s += input('Dame un valor float') + ','
    return s[:-1]

# Abrimos el puerto del arduino a 115200
# modificar el puerto al que este conectado nodeMCU
PuertoSerie = abrirPort( 'COM5', 115200 )
s = ''
# Creamos un bucle sin fin
while s!='s':
    s = input("Deseas salir (s/n)")
    if s!='s':  # si no se quiere salir
        tam = int( input('Dame el tamaño del vector') )
        vector = leerVector( tam ) # lee el vector como 'v0,v1,...,vtam-1'
        mensaje = str(tam) + ':' + vector
        print( mensaje )
        sendMensaje(PuertoSerie, mensaje)
        print( 'Esperando recibir ... ' )
        entero = receiveMensaje(PuertoSerie) # recibe la respuesta
        print( entero )
        real = receiveMensaje(PuertoSerie) # recibe la respuesta
        print( real ) # muestra por pantalla la respuesta recibida
cerrarPort(PuertoSerie) # se cierra el puerto serie

