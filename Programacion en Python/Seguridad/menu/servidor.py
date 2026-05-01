# -*- coding: utf-8; mode: python -*-
#!/usr/bin/env python#importamos el modulo para trabajar con sockets
import socket
import threading
from mensaje import * # Importamos la libreria de PySerial y mensaje
from Seguridad import struc as st
import time
# instanciamos un objeto para trabajar con el socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "localhost"
puerto = 10001
# Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
# Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
servidor.bind((ip, puerto))

# Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
# El numero de conexiones entrantes que vamos a aceptar
servidor.listen(2)
print ("[*] Esperando conexiones en %s:%d" % (ip, puerto))
# Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este
# devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
while True: # Creamos un buble sin fin
    cliente, direccion = servidor.accept()
    print ("[*] Conexion establecida con %s:%d" % (direccion[0], direccion[1]))
    # Recibimos el mensaje, con el metodo recv recibimos datos y como parametro
    # la cantidad de bytes para recibir
    mensaje = cliente.recv(1024).decode('utf-8')
    print(type(mensaje))
    mensaje = mensaje.split("||")
    # **************SUPERVISAR como queda la cadena despues de leer
    print(mensaje)
    if mensaje[0] == "1":  # Asignar A
        resultado = st.suma(mensaje)
        cliente.send(resultado)  # Si por alguna razon el mensaje es close cerramos la conexion
        print(mensaje)
    elif mensaje[0] == "2":  # Asignar B
        print(mensaje[1])
        st.ejecutar(mensaje[1])
        time.sleep(1)
        # Abrimos el archivo en modo lectura binaria
        # y leemos su contenido
        with open("./listado.txt", "rb") as archivo:
            buffer = archivo.read()
        while True:
            # Enviamos al servidor la cantidad de bytes
            # del archivo que queremos enviar
            print ("Enviando buffer")
            cliente.send(bytes(str(len(buffer)), "utf-8"))
            # Esperamos la respuesta del servidor
            recibido = cliente.recv(10)
            if recibido == "OK":
                print ("Enviando archivo")
                # En el caso que la respuesta sea la correcta
                # enviamos el archivo byte por byte
                # y salimos del while
                for byte in buffer:
                    print (byte)
                    cliente.send(byte)
                break

servidor.close()
