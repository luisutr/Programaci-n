#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Banco():

    def ejecutar_orden(self, orden):
        orden=orden.split()
        if orden[0]== "crear":
            self.crear(orden)
        if orden [0]== "consulta":
            return self.consulta(orden)
        if orden[0]== "ingreso":
            self.ingreso(orden)
        if orden[0]=="pago":
            self.pago(orden)
        if orden[0]== "transferencia":
            self.transferencia(orden)
        if orden[0]== "haymora":
            print(self.haymora(orden))
            return self.haymora(orden)
        if orden[0]=="intereses":
            self.interes(orden)


    def __init__(self):
        self.usuario={} #creo diccionario para los datos de usuario
        self.cuenta={} #creo diccionario que almacena las cuentas de usuario

    def crear(self,orden):
        # "crear Cliente1 123123X CC0987654321 700 3"
        operacion, nombre, DNI, cc, saldo, interes= orden
        if nombre not in self.usuario:
            usuario= Persona(nombre, DNI)
            self.usuario[usuario.DNI]=usuario
        else:
            usuario= self.usuario[DNI]
            cuenta= Cuenta(cc, saldo, interes)
            usuario.añadircuenta(cuenta)
            if usuario.añadircuenta(cuenta.cc):
                self.cuenta[cuenta.cc]=cuenta


    def consulta(self,orden):
        operacion, cc= orden
        if cc in self.cuenta:
            cuenta= self.cuenta[cc]
            res=cuenta.consultar()
        return res

    def ingreso(self,orden):
        operacion, cc, valor = orden
        if cc in self.cuenta:
            cuenta=self.cuenta[cc]
            cuenta.ingresar(valor)
        return

    def pago(self,orden):
        operacion, cc, valor = orden
        if cc in self.cuenta:
            cuenta = self.cuenta[cc]
            cuenta.pagar(valor)
        return

    def transferencia(self,orden):
        operacion, cc, cc2, valor = orden
        if float(valor)<0:
            print("Es imposible transfererir saldo negativo")
        else:
            if cc2 in self.cuenta:
                cuenta=self.cuenta[cc]
                cuenta.ingresar(valor)
            if cc in self.cuenta:
                cuenta=self.cuenta[cc2]
                cuenta.pagar(valor)
        return

    def haymora(self):
        operacion, dni= orden
        if dni in self.usuario:
            usuario=self.usuario[dni]
            res= persona.haymora()
            print (res)
        return res


    def interes(self):
        if orden[1] in self.cuentas:
            cuenta = self.cuentas[orden[1]]
            cuenta.interes()
        return

    def buscar_cuenta(self, orden):
        cc=orden
        if cc in self.cuentas:
            print(self.cuentas[cc])
        return

    def buscar_cliente(self, orden):
        orden = dni
        if dni in self.usuario:
            usario = self.usuario[dni]
            print(usuario, "tiene", len(persona.lista_cuentas), "cuentas")


class Persona():
    def __init__(self, cliente, DNI, cuenta):
        self.cliente=cliente
        self.DNI=DNI
        self.cuenta=cuenta
    def getdni(self):
        return self.DNI
    def getcliente(self):
        return self.cliente
    def haymora(self):
        for cuenta in self.lista_cuentas:
            if int(cuenta.saldo) < 0:
                return 'sihaymora'
            else:
                return 'nohaymora'
    def añadircuenta(self, cc):
        if len(self.lista_cuentas)>3:
            return False
        else:
            self.lista_cuentas.append(cc)
            return True


class Cuenta():
    def __init__(self, cc, saldo, interes):
        self.cc=cc
        self.saldo=saldo
        self.interes=interes
    def consultar(self):
        return self.saldo
    def ingresar(self):
        if int(valor)>= 0:
            self.saldo=(str(int(self.saldo)+ int(valor)))
        return self.saldo
    def pagar(self):
        if int(valor)>= 0:
            self.saldo=(str(int(self.saldo)+int(valor)))
        return self.saldo
    def transferencia(self, valor, cuenta2):
        self.saldo=(str(int(self.saldo)+int(valor)))
        cuenta2.saldo=(str(int(cuentarecibe.saldo)-int(valor)))
        return self.saldo, cuenta2.saldo
    def interes(self):
        self.saldo=str(int(self.saldo)+int(self.saldo)*int(self.interes)/100)
    def modificarsaldo(self):
        self.cc=saldo

def main(argv):
    argv.pop(0)
    banco= Banco()

    if argv[0]== "-":
        argv.pop(0)
        orden= input("Introduzca una orden")
        while orden != "salir":
            orden = input("Introducir una orden")
            banco.ejecutar_orden(orden)
    else:
        nombre_fichero=argv[0]
        try:
            with open (nombre_fichero, 'r') as filedesc:
                for linea in filedesc:
                    linea = linea.replace("\n", "")
                    linea = linea.replace('  ', " ")
                    linea = linea.replace('   ', " ")
                    orden=linea
                    if orden + "-" != "-":
                        print(banco.ejecutar_orden(orden))
        except FileNotFoundError:
            print("No se ha encontrado el fichero")
    pass


if __name__ == "__main__":
   main(sys.argv)