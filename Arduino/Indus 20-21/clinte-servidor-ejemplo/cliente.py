import serial
from mensaje import *

def menu():
    print("0) Salir")
    print("1) Sumar N números enteros")
    print("2) Incrementar 3 números float en M (float) cada uno")
    return input('Elige una opción: ')

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort( 'COM5', 115200 ) # Cambiar si necesario

opc = '-1' # inicializado a un valor no válido
while opc!='0':
    opc = menu() # muestra menú y devuelve opción en opc
    r = opc + ':'  # El primer valor de la trama es la opción elegida
    if opc=='1': # Si es el caso 1
        N = input('Dame el valor de N: ') # N recibe el valor N como cadena
        r += N # Añade N en la trama
        for e in range(int(N)):
            r += ':' + input('Dame un entero: ') # añade los N valores a la trama
    elif opc=='2': # Si es el caso 2
        N = input('Dame el valor de N: ')  # N recibe el valor N como cadena
        r += N
        for e in range(int(N)):
            r += ':' + input('Dame un float: ') # añade los 3 valores a la trama
        r += ':' + input('Dame el valor de M (float): ') # añade M a la trama
    #r += '\n' # añade carácter final a la trama
    print(r) # formato trama opc:N:v1:v1...vN:M, M sólo en caso 2
    if opc>='1' and opc<='2': # Si es una opción válida
        # envía trama
        sendMensaje(PuertoSerie, r) # Envía la trama al nodeMCU
        s = receiveMensaje(PuertoSerie) # Recibe la trama de respuesta
        print( s ) # Muestra por pantalla la respuesta
