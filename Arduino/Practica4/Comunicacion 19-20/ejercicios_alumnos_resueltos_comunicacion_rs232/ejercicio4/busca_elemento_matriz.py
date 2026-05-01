# Importamos la libreria de PySerial
from mensaje import *

# lee un vector como una lista
def leerMatriz(fil, col):
    s = ''
    for i in range(fil):
        s += '{'
        for j in range(col):
            if j!=col-1: s += input('Dame un char') + ','
            else: s += input('Dame un char') + '},'
    return s[:-1]

FIL = 3
COL = 4
# Abrimos el puerto del arduino a 115200
# modificar el puerto al que este conectado nodeMCU
PuertoSerie = abrirPort( 'COM5', 115200 )
s = ''
# Creamos un bucle sin fin
while s!='s':
    s = input("Deseas salir (s/n)")
    if s!='s':  # si no se quiere salir
        # matriz = leerMatriz(FIL, COL)
        # se puede comentar la línea anterior y poner esto para no introducir los valores
        matriz = '{1,2,3,4},{5,6,7,8},{9,0,A,B}'
        elem = input('Dame el elemento a buscar')
        mensaje = elem + ':' + matriz
        print( mensaje )
        sendMensaje(PuertoSerie, mensaje)
        print( 'Esperando recibir ... ' )
        r = receiveMensaje(PuertoSerie) # recibe la respuesta
        print( r ) # muestra por pantalla la respuesta recibida
cerrarPort(PuertoSerie) # se cierra el puerto serie

