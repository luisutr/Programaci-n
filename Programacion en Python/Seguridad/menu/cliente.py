# -*- coding: utf-8; mode: python -*-
#!/usr/bin/env python#importamos el modulo para trabajar con sockets
import socket

servidor = "localhost"
puerto = 10001
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
#cliente.send("HOLA SERVIDOR");

"Muestra el menú de las opciones y devuelve la seleccionada"
def menu():
    print("0) Salir")
    print("1) Sumar N números enteros")
    print("2) Inserta un comando")
    return input("Elige una opción: ")

opc = "-1" # inicializado a un valor no válido
# Creamos un buble sin fin
while opc!="0":
    opc = menu() # muestra menú y devuelve opción en opc
    r = opc + "||" # El primer valor de la trama es la opción elegida
    if opc=="1": # Si es el caso 1
        N = input("Dame el valor de N: ") # valor N como cadena
        r += N # Añade N en la trama
        for e in range(int(N)): # N valores a la trama
            r += "||" + input("Dame un entero: ")
    elif opc=="2": # Si es el caso 2
        r = opc + "||" # El primer valor de la trama es la opción elegida
        r += input("Escribe ruta a listar");
    # envía trama
    cliente.send(bytes(r, "utf-8"))
    # Recibimos el mensaje, con el metodo recv recibimos datos y como parametro
    # la cantidad de bytes para recibir
    if opc=="1":
        respuesta = cliente.recv(4096)
        print ("[*] Respuesta recibida: " + respuesta)
    if opc=="2":
        while True:
            # Recibimos la longitud que envia el cliente
            recibido = cliente.recv(1024).strip()
            if recibido:
                print ("Recibido:", recibido)
                # Verificamos que lo que recibimos sea un número
                # en caso que así sea, enviamos el mensaje "OK"
                # al cliente indicandole que estamos listos
                # para recibir el archivo
            if recibido.isdigit():
                cliente.send(bytes("OK", "utf-8"))
                # Inicializamos el contador que
                # guardara la cantidad de bytes recibidos
                buffer = 0
                # Abrimos el archivo en modo escritura binaria
                with open("listado2.txt", "wb") as archivo:
                    # Nos preparamos para recibir el archivo
                    # con la longitud específica
                    while (buffer < int(recibido)):
                        data = cliente.recv(1024).decode('utf-8')
                        if not len(data):
                            # Si no recibimos datos
                            # salimos del bucle
                            break
                        # Escribimos cada byte en el archivo
                        # y aumentamos en uno el buffer
                        data = bytes(data, encoding="UTF-8")
                        archivo.write(data)
                        buffer += 1
                        print (buffer, recibido)
                    if buffer == int(recibido):
                        print ("Archivo descargado con éxito")
                    else:
                        print ("Ocurrió un error/Archivo incompleto")
                    archivo.close()
                break
    opc = input("Pulse c para Continuar 0 para Salir")
#Cerramos la instancia del objeto servidor
cliente.close()
