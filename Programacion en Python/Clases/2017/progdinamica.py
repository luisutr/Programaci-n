# -*- coding: utf-8; mode: python -*-
#Ejemplo de programaciÃ³n dinÃ¡mica en lenguaje python
#PROGRAMA QUE OPTIMIZA EL CAMBIO A DEVOLVER DE UNA CANTIDAD
#Y CON LAS MONEDAS QUE TU LE INDIQUES
#”Codeado” por villa en enero-2006
#referencias : Fundamentos de algoritmia – Prentice hall,python.org

class Cambio:

    def __init__(self,cambio):
        self.cambio = cambio
        self.monedas = self.pedir_monedas()
        self.cambios = self.crear_matriz(cambio,len(self.monedas))

def resolver(self):
    matriz = self.cambios
    monedas = self.monedas
    for moneda in range(len(monedas)):
    #la primera fila siempre va a ser valor 0
        matriz[0][moneda] = 0
    for cambio in range(1,len(matriz)):
        for moneda in range(len(monedas)):
        #si solo hay una moneda y el cambio es menor que la moneda mas pequeÃ±a, es imposible
            if (moneda == 0 ) and (cambio):
                if cambio == 'q':
                    return monedas
                monedas.append(int(cambio))

def crear_matriz(self,filas,columnas):
    matriz = []
    for i in range(filas+1):
        matriz.append([0]*columnas)
    return matriz

if __name__ == "__main__":
    cambio = raw_input("introduce el valor de la cantidad que quieres cambiar")
problema = Cambio(7)
print "La solucion optima es devolver ",problema.resolver(), " monedas"