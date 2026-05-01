#FUNCIONAMIENTO DE LA PRÁCTICA 2
#Ejecutar programa VSPE para poder comunicar los puertos COM1 y COM2
#Correr cliente y servidor. Todas los operaciones y resultados se mostrarán en el cliente
#Introducir operación deseada (0,1,2,3,4 o 5)
#Seguir los pasos que se indican en los ejemplos dentro de cada operación e introducir valores indicados
#Cada vez que se ejecute una operación, se mostrará el resultado también en el cliente y se podrá volver a elegir otra acción

# -*- coding: utf-8; mode: python -*-

from mensaje import *

def menu():      #Definimos un menú con todas las operaciones que queremos hacer
    print("\n")
    print("0) Salir")
    print("1) Devolución del sumario de valores comprendidos entre a y b (incluidos) y devolución del resultado")
    print("2) Devolución de los n cuadrados de n números enviados en un mensaje")
    print("3) Contar el número de veces que aparecen n letras en un texto")
    print("4) ¿Es palindromo?")
    print("5) Devolución de la última orden recibida")
    return input("Elige una opción: ")

# Abrimos el puerto del arduino a 9600
PuertoSerie = abrirPort("COM1")  # cambiar al correcto
# Creamos un buble que finaliza con "0"

opc = ""
while opc != "0":  #Cuando pulsamos el 0, salimos del programa
    opc = menu()
    mensa = ""
    if opc == "0":
        mensa = "0\n"
        sendMensaje(PuertoSerie, mensa)
    elif opc == "1":  #Introducimos valores a y b
        v = input("Introduce valor inicial:   [Ej: 2]")
        w = input("Introduce valor final: [Ej: 3]:  ")
        mensa = opc + ":" + v + "," + w + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r) #Para mayor comodidad, en todas las opciones mostraremos el resultado en la ventana Cliente
    elif opc == "2":  #Introducimos cantidad de números y números seperados por -
        v = input("Introduce cantidad de números:  [Ej: 3]")
        w = input("Introduce los  números separados por un guión [Ej: 4-5-6]:  ")
        mensa = opc + ":" + v + "," + w +  "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print("Resultados:", r)

    elif opc == "3":  #Cadena de texto donde queremos buscar y letras que queremos buscar
        v = input("Introduce cadena de texto: [Ej: ttxxuu]") #
        w = input("Introduce letras que quieres buscar [Ej: tx]:  ")
        mensa = opc + ":" + v + "," + w + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)

    elif opc == "4": #Introducimos la cadena que queremos ver si es o no palindromo
        v = input("Introduce cadena: [Ej: ABBA]:  ")
        mensa = opc + ":" + v + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print(r)

    elif opc == "5":  #La opción 5 nos devuelve la última orden que está almacenada en r
        mensa = opc + ":" + "\n"
        sendMensaje(PuertoSerie, mensa)
        r = receiveMensaje(PuertoSerie)
        print("La última orden recibida fue:", r)