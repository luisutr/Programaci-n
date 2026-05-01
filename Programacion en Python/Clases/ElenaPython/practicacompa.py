#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket
import time


class Banco():
    def __init__(self, cuentas=[]):
        self.cuentas = cuentas

    def ejecutar_orden(self, input):
        # '''Esta función retorna el resultado de ejecutar una orden bancaria.'''

        '''
        Esta función retorna el resultado de ejecutar una orden bancaria.

        Args:
            orden (str): la orden de que el banco debe procesar.

        Returns:
            resultado (str): el resultado de la orden.
                            En minusculas. Sin acentos.
                            Todos los valores se han de convertir al tipo string.
        '''
        orden = Orden(input)
        try:
            if orden.get_modo() == 'crear':
                # crear <nombre> <dni> <codigo_cuenta> <valor> <interes>
                res = self.crea(orden.get_nombre(), orden.get_dni(), orden.get_codigo_cuenta(), orden.get_valor(),
                                orden.get_interes())

            elif orden.get_modo() == 'consulta':
                # consulta <codigo_cuenta>
                res = self.consulta(orden.get_codigo_cuenta())

            elif orden.get_modo() == 'ingreso':
                # ingreso <codigo_cuenta> <valor>
                res = self.ingresa(orden.get_codigo_cuenta(), orden.get_valor())

            elif orden.get_modo() == 'pago':
                # pago <codigo_cuenta> <valor>
                res = self.paga(orden.get_codigo_cuenta(), orden.get_valor())

            elif orden.get_modo() == 'transferencia':
                # transferencia <codigo_cuenta> <codigo_cuenta> <valor>
                res = self.transferencia(orden.get_cuenta_pago(), orden.get_cuenta_ingreso(), orden.get_valor())

            elif orden.get_modo() == 'haymora':
                # haymora <dni>
                res = self.haymora(orden.get_dni())

            elif orden.get_modo() == 'intereses':
                # intereses <cuenta>
                res = self.intereses(orden.get_codigo_cuenta())
            else:
                res = 'La orden introducida no se puede ejecutar.'

            return str(res)
        except Exception:
            return 'Error tipo ', sys.exc_info()[0], ' en  <<ejecutar_orden,metodos>>.'

        # res = procesar_orden()

    def consulta(self, num_cuenta):
        try:
            cuenta = self.cuentas[num_cuenta]
            saldo = cuenta.get_saldo()
            return saldo
        except Exception:
            print('Error tipo ', sys.exc_info()[0], ' en  <<consulta>>')

    def ingresa(self, num_cuenta, cantidad):
        try:
            cuenta = self.cuentas[num_cuenta]
            saldo = cuenta.get_saldo()
            cuenta.set_saldo(str(int(saldo) + int(cantidad)))
            return 'El ingreso se ha realizado correctamente'
        except Exception:
            return 'Error tipo ', sys.exc_info()[0], ' en  <<Ingreso>>'

    def paga(self, num_cuenta, cantidad):
        try:
            cuenta = self.cuentas[num_cuenta]
            saldo = cuenta.get_saldo()
            cuenta.set_saldo(str(int(saldo) - int(cantidad)))
            return 'El pago se ha realizado correctamente'
        except ImportError:
            return 'Error tipo ', sys.exc_info()[0], ' en  <<pago>>'

    def transferencia(self, cuenta_pago, cuenta_ingreso, cantidad):
        try:
            self.paga(cuenta_pago, cantidad)
            self.ingresa(cuenta_ingreso, cantidad)
            return 'La tranferencia se ha realizado correctamente'
        except Exception:
            Banco.ingresa(self, cuenta_pago, cantidad)
            return 'Error tipo ', sys.exc_info()[0], ' en  <<tranferencia>>'

    def haymora(self, DNI):
        try:
            for cuenta in self.cuentas.values():
                if cuenta.get_dni() == DNI:
                    saldo = float(cuenta.get_saldo())
                    if saldo < 0:
                        mora = 'sihaymora'
                    else:
                        mora = 'nohaymora'
            return mora
        except Exception:
            return 'Error tipo ', sys.exc_info()[0], ' en  <<haymora>>'

    def crea(self, nombre, dni, codigo_cuenta, valor, interes):
        try:
            persona = Persona(nombre, dni)
            cuenta = Cuenta(persona, dni, codigo_cuenta, valor, interes)
            claves = []
            valores = []
            if len(self.cuentas) != 0:
                for key, value in self.cuentas.items():
                    claves.append(key)
                    valores.append(value)
            claves.append(codigo_cuenta)
            valores.append(cuenta)
            self.cuentas = dict(zip(claves, valores))
            return 'La cuenta se ha creado correctamente'
        except Exception:
            return 'Error tipo ', sys.exc_info()[0], ' en  <<crea>>'

    def intereses(self, num_cuenta):
        try:
            cuenta = self.cuentas[num_cuenta]
            intereses = str(float(cuenta.get_saldo()) * (float(cuenta.get_interes()) * 0.01))
            return intereses
        except Exception:
            return 'Error tipo ', sys.exc_info()[0], ' en  <<Intereses>>'


class Orden():
    def __init__(self, orden):
        orden = orden.replace('\n', '')
        orden = orden.split()
        self.modo = orden[0]
        if self.modo == 'crear':
            # crear <nombre> <dni> <codigo_cuenta> <valor> <interes>
            self.nombre = orden[1]
            self.dni = orden[2]
            self.codigo_cuenta = orden[3]
            self.valor = orden[4]
            self.interes = orden[5]
        elif self.modo == 'consulta' or self.modo == 'intereses':
            # consulta <codigo_cuenta>
            # intereses <cuenta>
            self.codigo_cuenta = orden[1]
        elif self.modo == 'pago' or self.modo == 'ingreso':
            # ingreso <codigo_cuenta> <valor>
            # pago <codigo_cuenta> <valor>
            self.codigo_cuenta = orden[1]
            self.valor = orden[2]
        elif self.modo == 'transferencia':
            # transferencia <codigo_cuenta> <codigo_cuenta> <valor>
            self.cuenta_pago = orden[1]
            self.cuenta_ingreso = orden[2]
            self.valor = orden[3]
        elif self.modo == 'haymora':
            # haymora <dni>
            self.dni = orden[1]

        pass

    def get_modo(self):
        return self.modo

    def get_nombre(self):
        return self.nombre

    def get_dni(self):
        return self.dni

    def get_codigo_cuenta(self):
        return self.codigo_cuenta

    def get_cuenta_ingreso(self):
        return self.cuenta_ingreso

    def get_cuenta_pago(self):
        return self.cuenta_pago

    def get_valor(self):
        return self.valor

    def get_interes(self):
        return self.interes


class Persona():
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

    pass

    def get_nombre(self):
        return self.nombre

    def get_dni(self):
        return self.dni


class Cuenta():
    def __init__(self, persona, dni, codigo_cuenta, valor, interes):
        self.codigo_cuenta = codigo_cuenta
        self.dni = dni
        self.persona = persona
        self.saldo = valor
        self.interes = interes

    pass

    def get_saldo(self):
        return self.saldo

    def get_interes(self):
        return self.interes

    def get_dni(self):
        return self.dni

    def set_saldo(self, saldo):
        self.saldo = saldo
        return


class TeleBanco(Banco):

    def __init__(self, ip_address, port, cuentas=[], MAX_OPEN_REQUESTS=5):
        '''
        El constructor recibe dirección IP y puerto donde ha de escuchar peticiones de clientes.

        Args:
            ip_address (str): dirección IP para escuchar y recibir conexiones.
            port (int): puerto para escuchar y recibir conexiones.
        '''

        # TODO:
        #   - Crear socket para recibir conexiones
        #   - Enlaces de interés:
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.bind
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.listen
        #       - https://docs.python.org/3.6/library/socket.html#example
        Banco.__init__(self, cuentas)
        self.IP = ip_address
        self.PORT = int(port)
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.serversocket.bind((self.IP, self.PORT))
            self.serversocket.listen(MAX_OPEN_REQUESTS)

        except socket.error:
            print("Problemas using port %i. Do you have permission?" % self.PORT)
        pass

    def start(self):
        '''
        Este método llama al método `accept` del socket del servidor.
        Se procesan las conexiones entrantes de clientes.
        '''

        # TODO:
        #   - Aceptar y procesar conexiones entrantes.
        #   - El servidor primero lee la orden y luego contesta.
        #   - Si la orden es incorrecta (no cumple formato), contesta con un error.
        #   - Si se recibe la orden `stop`, se llama al método '.stop()' y el programa termina.

        #   - Enlaces de interés:
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.accept
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.recv
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.send
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.sendall
        try:
            print("Waiting for connections at %s %i" % (self.IP, self.PORT))
            (self.clientsocket, address) = self.serversocket.accept()
            # self.clientsocket.send(str.encode('Bienvenido al TeleBanco, gracias por su confianza.'))
            orden = self.clientsocket.recv(2048).decode("utf-8")
            while orden != 'stop':
                res = self.ejecutar_orden(orden)
                self.clientsocket.send(str.encode(res))
                orden = self.clientsocket.recv(2048).decode("utf-8")
            self.clientsocket.close()
            self.stop()
        except:
            res = 'Error tipo ', sys.exc_info()[0], ' en <<Start,TeleBanco>>'
        pass

    def stop(self):
        self.serversocket.close()
        '''
        Este método cierra el socket del servidor.
        El programa se para.
        '''

        # TODO:
        #   - Enlaces de interés:
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.close

        pass


class TeleTerminal():

    def __init__(self, ip_address, port, ops='-'):
        '''
        El constructor recibe dirección IP y puerto del telebanco y establece una conexión con él.

        Args:
            ip_address (str): dirección IP para escuchar y recibir conexiones.
            port (int): puerto para escuchar y recibir conexiones.
        '''

        # TODO:
        #   - Crear socket para comunicarse con el TeleBanco
        #   - Enlaces de interés:
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket
        #       - https://docs.python.org/3.6/library/socket.html#example
        self.IP = ip_address
        self.PORT = int(port)
        self.ops = ops
        try:
            self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serv.connect((self.IP, self.PORT))
        except OSError:
            print("Socket already used")
            self.serv.close()
            self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serv.connect((self.IP, self.PORT))

        pass

    def cliente(self):
        # print(self.serv.recv(2048).decode("utf-8"))
        if '-' == self.ops:
            orden = input('Introduzca la orden que quiere ejecutar:')
            while orden != 'stop':
                print(self.ejecutar_orden(orden))
                orden = input('Introduce el mensaje que quieres enviar:')
            self.serv.send(str.encode('stop'))
        else:
            fichero = self.ops
            try:
                with open(fichero, 'r') as filedesc:
                    for linea in filedesc:
                        if linea.strip():
                            orden = linea.replace('\n', '')
                            print(TeleTerminal.ejecutar_orden(self, orden))
                    TeleTerminal.ejecutar_orden(self, 'salir')
            except IOError:
                print("Fichero no encontrado")
            except Exception:
                print('Error tipo ', sys.exc_info()[0], ' en <<cliente>>')
        self.stop()

    def ejecutar_orden(self, orden):
        '''
        Este método retorna el resultado de ejecutar una orden bancaria.

        Args:
            orden (str): la orden de que el banco debe procesar.

        Returns:
            resultado (str): el resultado de la orden.
                            En minúsculas. Sin acentos.
                            Todos los valores se han de convertir al tipo string.
        '''

        # TODO:
        #   - Conectarse al TeleBanco y enviarle las ordenes.
        #   - Tras conectarse, el cliente envía la orden, cliente inicia la comunicación.
        #   - Enlaces de interés:
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.connect
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.recv
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.send
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.sendall

        # res = procesar_orden()
        # res = "resultado_orden"
        # self.serv.connect((self.IP, self.PORT))
        self.serv.send(str.encode(orden))
        res = self.serv.recv(2048).decode("utf-8")
        return res

    def stop(self):
        '''
        Este método cierra el socket del cliente.
        El programa se para.
        '''

        # TODO:
        #   - Enlaces de interés:
        #       - https://docs.python.org/3.6/library/socket.html#socket.socket.close

        self.serv.close()
        pass


class Introduccion():
    def __init__(self, lista):
        try:
            lista.pop(0)
            self.modo = lista[0]
            self.IP = lista[1]
            self.PORT = lista[2]
            self.ops = lista[3]

        except IndexError:
            if self.modo == 'teleterminal':
                self.ops = '-'
        except Exception:
            print('Error tipo ', sys.exc_info()[0], ' en <<Introduccion,INIT>>')


def main(argv):
    try:
        orden = Introduccion(argv)
        if orden.modo == 'telebanco':
            servidor = TeleBanco(orden.IP, orden.PORT)
            servidor.start()
        elif orden.modo == 'teleterminal':
            cliente = TeleTerminal(orden.IP, orden.PORT, orden.ops)
            cliente.cliente()
        else:
            print('Error tipo ', sys.exc_info()[0], ' en <<main,modo>> ')
        pass
    except KeyboardInterrupt:
        if orden.modo == 'telebanco':
            servidor.close()
        elif orden.modo == 'teleterminal':
            cliente.close()
    # TODO:
    #   - Si se interrumpe la ejecución (Control-C), cerrar el socket, ya se de cliente o de servidor.
    #   - Enlaces de interés:
    #       - https://docs.python.org/3.6/library/exceptions.html#KeyboardInterrupt
    #       - https://stackoverflow.com/questions/15318208/capture-control-c-in-python


if __name__ == "__main__":
    main(sys.argv)