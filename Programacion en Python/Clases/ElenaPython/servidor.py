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


import socket

PORT = 5000
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5
SERVICE_PRICE_EUROS = 20
# RMB is the China currency: Renminbi is the currency, Yuan is the unit
SERVICE_PRICE_RM = SERVICE_PRICE_EUROS/0.13

class TeleBanco(Cuenta,Banco):  #RECIBE LA ORDEN Y LA PROCESA

    def __init__(self, ip_address, port):
        self.ip_address= str(ip_address)
        self.port= int(port)                     #AQUI LA IP Y EL PUERTO SON PARA ESCUCHAR PETICIONES DEL CLIENTE
        self.MAX_OPEN_REQUESTS = 2
        self.mibanco = Banco()
        # Creamos un objeto socket tipo TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.socket_tcp:
            self.socket_tcp.bind((self.ip_address, self.port))
            self.socket_tcp.listen(5)  # Esperamos la conexión del cliente
            conn, addr = self.socket_tcp.accept()  # Establecemos la conexión con el cliente
            with conn:
                print('[*] Conexión establecida')
                while True:
                    # Recibimos bytes, convertimos en str
                    data = conn.recv(2048).decode("utf-8")
                    print('[*] Datos recibidos: '+data)
                    res = self.mibanco.ejecutar_orden(data)
                    conn.send(str.encode(res))  # Hacemos echo convirtiendo de nuevo a bytes


mi_tele_banco = TeleBanco('127.0.0.1', 5000)