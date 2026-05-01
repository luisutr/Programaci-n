#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket
from threading import Thread

class Banco:

    def __init__(self):
        self.lista_clientes = []

    def ejecutar_orden(self, orden):
        orden = orden.split(' ')
        res = ""
        if orden[0] == 'crear':
            self.crear_cuenta(orden)

        if orden[0] == 'consulta':
            for cliente in self.lista_clientes:
                if cliente.mirar_si_existe_cuenta(orden[1]):
                    cuenta = cliente.consultaencuenta(orden[1])
                    res = cuenta.consulta()
        return res

    def crear_cuenta(self, orden):
        # ['crear', 'Cliente1', '123123X', 'CC0987654321', '700', '3']
        # [   '0',      '1',        '2',        '3',        '4', '5']
        operacion, nombre, dni, ncc, saldo, interes = orden
        # en vez de las posiciones puedes poner variables, al usar la fila de arriba a cada posicion se le asigana su variable
        if len(self.lista_clientes) != 0:
            listadni = []
            for cliente in self.lista_clientes:
                listadni.append(cliente.get_dni)
            if orden[2] not in listadni:
                usuario = Persona(nombre, dni)
                cuenta = Cuenta(ncc, saldo, interes)
                usuario.agregar_cuenta(cuenta)
                self.lista_clientes.append(usuario)

            elif cliente.get_dni == dni:
                if cliente.contar_cuentas() < 3 and cliente.mirar_si_existe_cuenta(ncc):
                    cuenta = Cuenta(ncc, saldo, interes)
                    cliente.agregar_cuenta(cuenta)

        else:
            usuario = Persona(nombre, dni)
            cuenta = Cuenta(ncc, saldo, interes)
            usuario.agregar_cuenta(cuenta)
            self.lista_clientes.append(usuario)


class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.lista_cuentas = []

    def get_dni(self):
        return self.dni

    def contar_cuentas(self):
        return len(self.lista_cuentas)

    def agregar_cuenta(self, saldo):
        self.lista_cuentas.append(saldo)

    def mirar_si_existe_cuenta(self, saldo):
        for cuenta in self.lista_cuentas:

            if cuenta.get_ccuenta() == saldo:
                return True

    def consultaencuenta(self, saldo):
        for cuenta in self.lista_cuentas:
            if cuenta.get_ccuenta() == saldo:
                return cuenta

    pass


class Cuenta:
    def __init__(self, ccuenta, saldo, interes):
        self.ccuenta = ccuenta
        self.saldo = saldo
        self.interes = interes

    def consulta(self):
        return self.saldo

    def get_ccuenta(self):
        return self.ccuenta

    def set_ccuenta(self, saldo):
        self.ccuenta = saldo

    def ingresar(self, valor):
        if valor > 0:
            self.saldo = str(int(self.saldo)) + int(valor)
        else:
            print("Ingrese algo de dinero")
        return self.saldo

    def pago(self, valor):
        if valor > 0:
            self.saldo = str(int(self.saldo)) - (int(valor))
        else:
            print("Para pagar tiene que introudcr una valor positivo")
        return self.saldo

    def haymora(self):
        if int(self.saldo) < 0:
            return "sihaymora"

        else:
            return "nohaymora"

    def transferencia(self, cuenta_recibe, valor):
        if valor > 0:
            self.saldo = str(int(self.saldo)) - int(valor)
            cuenta_recibe.saldo = str(int(cuenta_recibe.saldo)) + int(valor)

    def calcular_interes(self):
        self.saldo = str(int(self.saldo) + int(self.saldo) * (int(self.interes) / 100))


#CLASE TELEBANCO Y TELETERMINAL
#EL TELETERMINAL ENVIA LA ORDEN AL TELEBANCO YY EL TELEBANCO LA PROCESA Y DEVUELVE EL RESULTADO DE ESA ORDEN


class TeleBanco(Cuenta,Banco):  #RECIBE LA ORDEN Y LA PROCESA

    def __init__(self, ip_address, port):
        self.ip_address= str(ip_address)
        self.port= int(port)                     #AQUI LA IP Y EL PUERTO SON PARA ESCUCHAR PETICIONES DEL CLIENTE
        self.MAX_OPEN_REQUESTS = 2
        self.conectar()

    def process_client(clientsocket):
        print(clientsocket)
        send_message = 'Conexion establecida'
        # Serializing the data to be transmitted
        send_bytes = str.encode(send_message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        recibido = clientsocket.recv(2048).decode("utf-8")
        while recibido != 'salir':
            print("Read from the server:", recibido)
            mensaje = input('Introduce el mensaje que quieres enviar:RESPUESTA')
            clientsocket.send(str.encode(mensaje))
            recibido = clientsocket.recv(2048).decode("utf-8")

        clientsocket.close()
    def conectar (self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mibanco = Banco()
        try:
            serversocket.bind((self.ip_address, self.port))  # QUIERO ESTAR A LA ESCUCHA DE ESTA MAQUINA (IP) Y ESTE PUERTO
            serversocket.listen(self.MAX_OPEN_REQUESTS) #soy el servidor
            while True:
                print("Waiting for connections at %s %i" % (self.ip_address, self.port))
                (clientsocket, address) = serversocket.accept()
                self.process_client(clientsocket)
                mensaje_recibido = serversocket.recv(4096).decode("utf-8")
                print(mensaje_recibido)
                resultado = mibanco.ejecutar_orden(mensaje_recibido)
                pass

        except socket.error:
            print("Problemas using port %i. Do you have permission?" % self.port)

class TeleTerminal(Persona):  #ES EL CAJERO, OSEA EL CLINETE, ES EL QUE MARDA LA ORDEN

    def __init__(self, ip_address, port):
        self.ip_address = str(ip_address)         #AQUI LA IP Y EL PUERTO ES LA DEL TELEBANCO
        self.port = int(port)
        self.conectar()
    def conectar(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:

            s.connect(self.ip_address,self.port)

        except OSError:
            print("Socket already used")
            # But first we need to disconnect
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip_address, self.port))
        print("Read from the server", s.recv(2048).decode("utf-8"))
        mensaje = input('Introduce el mensaje que quieres enviar: la orden')
        s.send(str.encode(mensaje))

        while mensaje != 'salir':
            print("Read from the server:", s.recv(2048).decode("utf-8"))
            mensaje = input('Introduce el mensaje que quieres enviar: la orden')
            s.send(str.encode(mensaje))
            '''
            El constructor recibe dirección IP y puerto del telebanco y establece una conexion con él.
            Args:
            ip_address (str): dirrección IP para escuchar y recibir conexiones.
            port (int): puerto para escuchar y recibir conexiones.
            '''
            pass
