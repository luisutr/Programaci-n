#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


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



def main(argv):
    banco = Banco()

    if argv[0] == "-":
        orden = input("Introducir orden con información correspondiente")
        banco.ejecutar_orden(orden)

    else:
        nom_fichero = argv[0]
        try:
            with open(nom_fichero, 'r') as filedesc:
                for linea in filedesc:
                    linea = linea.replace("\n", "")
                    # linea = linea.replace(' ', '')
                    orden = linea
                    banco.ejecutar_orden(orden)
        except FileNotFoundError:
            print("No se ha encontrado documento")

    pass

def pruebas():
        mibanco = Banco()

        mibanco.ejecutar_orden("crear Cliente1 123123X CC0987654321 700 3")
        mibanco.ejecutar_orden("crear Cliente2 123121X CC0987654322 0 2")

        saldo1 = mibanco.ejecutar_orden("consulta CC0987654321")
        saldo2 = mibanco.ejecutar_orden("consulta CC0987654322")

        print("700", saldo1)
        print("0", saldo2)

pruebas()

'''
# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

class BancoTest(unittest.TestCase):
    def test_ejecutar_consulta(self):
        mibanco = Banco()

        mibanco.ejecutar_orden("crear Cliente1 123123X CC0987654321 700 3")
        mibanco.ejecutar_orden("crear Cliente2 123121X CC0987654322 0 2")

        saldo1 = mibanco.ejecutar_orden("consulta CC0987654321")
        saldo2 = mibanco.ejecutar_orden("consulta CC0987654322")

        self.assertEqual("700", saldo1)
        self.assertEqual("0", saldo2)


if __name__ == "__main__":
    unittest.main()
'''