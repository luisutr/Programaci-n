# -*- coding: utf-8; mode: python -*-
# Importamos la libreria de PySerial
from Seguridad.mensaje import *

"Muestra el menú de las opciones y devuelve la seleccionada"
def menu():
    print("0) Salir")
    print("1) Sumar N números enteros")
    print("2) Incrementar 3 números float en M (float) cada uno")
    return input("Elige una opción: ")

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort( "COM4" ) # Cambiar si necesario

opc = "-1" # inicializado a un valor no válido
# Creamos un buble sin fin

while opc!="0":
    opc = menu() # muestra menú y devuelve opción en opc
    r = opc + ":" # El primer valor de la trama es la opción elegida
    if opc=="1": # Si es el caso 1
        N = input("Dame el valor de N: ") # valor N como cadena
        r += N # Añade N en la trama
        for e in range(int(N)): # N valores a la trama
            r += ":" + input("Dame un entero: ")
    elif opc=="2": # Si es el caso 2
        r += "3" # Añade 3 en la trama
        for e in range(3): # añade los 3 valores a la trama
            r += ":" + input("Dame un float: ")
        r += ":" + input("Dame el valor de M (float): ") # M a la trama
        r += "\n" # añade carácter final a la trama
        print(r[:-1]) # formato trama opc:N:v1...vN:M, M sólo en caso 2
    if opc>="1" and opc<="2": # Si es una opción válida
        # envía trama
        sendMensaje(PuertoSerie, r) # Envía la trama al nodeMCU
        s = receiveMensaje(PuertoSerie) # Recibe la trama de respuesta
        print( s ) # Muestra por pantalla la respuesta