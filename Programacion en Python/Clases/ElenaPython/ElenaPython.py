#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Cuenta():
    def __init__(self, ccuenta, saldo, interes):
        self.ccuenta = ccuenta
        self.saldo = saldo
        self.interes = interes
    def get(self):
        return self.ccuenta
    def consulta(self):
        return self.saldo

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

    def transferencia(self, cuenta_recibe, valor):
        if valor > 0:
            self.saldo = str(int(self.saldo)) - int(valor)
            cuenta_recibe.saldo = str(int(cuenta_recibe.saldo)) + int(valor)

    def haymora(self):
        if self.saldo > 0:
            return "sihaymora"
        else:
            return "nohaymora"

class Persona():
    def __init__(self, cliente, DNI, cuentas):
        self.cliente = cliente
        self.DNI = DNI
        self.cuentas = cuentas

    def crearcuenta(self, ccuenta, saldo, interes):
        if len(self.cuentas)<3:
            nuevacuenta = Cuenta(ccuenta, saldo, interes)
            self.cuentas.append(nuevacuenta)
        else:
            print("no se pueden hacer mas de 3 cuentas")

    def getdni(self):
        return self.DNI

    def consultaencuenta(self, ncc):
        for cuenta in self.cuentas:
            if cuenta.get() == ncc:
                return cuenta.saldo




class Banco():
    def __init(self):
        self.usu = Persona()
        print("Se creo el banco")

    # ("crear Cliente1 123123X CC0987654321 700 3")#
    def ejecutar_orden(self, orden):
        self.orden = orden
        orden = orden.split(' ')
        # ['crear', 'Cliente1', '123123X', 'CC0987654321', '700', '3']
        operacion = orden[0]
        if operacion == 'crear':
            operacion, nombre, dni, ncc, saldo, interes = orden
            #creo la persona y una lista de cuentas vacias
            cliente = Persona(nombre, dni, [])
            #le creo una cuenta con los datos
            cliente.crearcuenta(ncc,saldo,interes)
            self.usu = cliente
        if operacion == "consulta":
            #consulta CC0987654321
            ncc = orden[1]
            print(self.usu.consultaencuenta(ncc))






mibanco = Banco()
mibanco.ejecutar_orden("crear Cliente1 123123X CC0987654321 700 3")
mibanco.ejecutar_orden("consulta CC0987654321")
mibanco.

'''

########################TEST############################

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


class BancoLeerFicheroTest(unittest.TestCase):
    def test_ejecutar_orden_ingreso_pago(self):
        output = []
        print = output.append

        main(['banco.py', './test_ordenes_1.txt'])
        res = [s for s in output if (s.find('7112') >= 0)]
        self.assertTrue(res)

    def test_ejecutar_orden_transferencia(self):
        output = []
        print = output.append

        main(['banco.py', './test_ordenes_2.txt'])
        res = [s for s in output if (s.find('1700') >= 0)]
        self.assertTrue(res)

    def test_ejecutar_orden_haymora(self):
        output = []
        print = output.append

        main(['banco.py', './test_ordenes_3.txt'])
        res = [s for s in output if (s.find('nohaymora') >= 0)]
        self.assertTrue(res)

'''