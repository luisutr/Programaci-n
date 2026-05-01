# Importamos la libreria de PySerial
from mensaje import *

# lee un vector como una lista
def leerMatriz(fil, col):
    s = ''
    for i in range(fil):
        for j in range(col):
            if j!=col-1: s += input('Dame un valor entre 0 y 15') + ','
            else: s += input('Dame un valor entre 0 y 15')
        s += ':'
    return s[:-1]

# Abrimos el puerto del arduino a 115200
# modificar el puerto al que este conectado nodeMCU
PuertoSerie = abrirPort( 'COM9', 115200 )
s = ''
# Creamos un bucle sin fin
while s!='0':
    s = input("Dame una opción:")
    if s=='1':
        #mensaje = '1:0:2:11,2,13:0,15,6:3,5,14:4,7,10'
        n_fil = input('Dame la fila a obtener entre 0 y 3')
        n_col = input('Dame la columna a obtener entre 0 y 2')
        mensaje = s + ':' + n_fil + ':' + n_col + ':' + leerMatriz(4, 3)
    if s=='2':
        # mensaje = '1:0:2:11,2,13:0,15,6:3,5,14:4,7,10'
        n_fil = input('Dame la fila a obtener el máximo')
        mensaje = s + ':' + n_fil + ':' + leerMatriz(4, 3)
    if s=='3':
        # mensaje = '1:0:2:11,2,13:0,15,6:3,5,14:4,7,10'
        mensaje = s + ':' + leerMatriz(4, 3)
    if s>='1' and s<='3':
        print( mensaje )
        sendMensaje(PuertoSerie, mensaje)
        print( 'Esperando recibir ... ' )
        r = receiveMensaje(PuertoSerie) # recibe la respuesta
        print( r ) # muestra por pantalla la respuesta recibida
cerrarPort(PuertoSerie) # se cierra el puerto serie
