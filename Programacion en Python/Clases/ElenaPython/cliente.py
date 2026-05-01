import sys
import socket
from threading import Thread

class TeleTerminal():  #ES EL CAJERO, OSEA EL CLINETE, ES EL QUE MARDA LA ORDEN

    def __init__(self, ip_address, port):
        self.ip_address = str(ip_address)         #AQUI LA IP Y EL PUERTO ES LA DEL TELEBANCO
        self.port = int(port)
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.ip_address, self.port))
        except OSError:
            print("Socket already used")
            # But first we need to disconnect
            self.s.close()
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.ip_address, self.port))
        pass

    def ejecutar_orden(self, orden):
        self.s.send(str.encode(orden))
        print("envio orden", orden)
        res = self.s.recv(2048).decode("utf-8")
        print("devuelve", res)
        return res



def pruebas():
    #mi_tele_banco = TeleBanco('127.0.0.1', 5341)
    #thread_tele_banco = Thread(target=mi_tele_banco.start)
    #thread_tele_banco.start()

    mi_tele_terminal = TeleTerminal('127.0.0.1', 5000)

    mi_tele_terminal.ejecutar_orden("crear Cliente1 123123X CC0987654321 700 3")
    #mi_tele_terminal.ejecutar_orden("crear Cliente2 123121X CC0987654322 0 2")

    saldo1 = mi_tele_terminal.ejecutar_orden("consulta CC0987654321")
    #saldo2 = mi_tele_terminal.ejecutar_orden("consulta CC0987654322")

    print("700", saldo1)
    #print("0", saldo2)

pruebas()