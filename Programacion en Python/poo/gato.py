__author__ = 'luisutrilla'
# -*- coding: utf-8; mode: python -*-

class Perro:
   def ruge(self):
       print('El perro ladra')

#polimorfismo
def rugir(animal):
    animal.ruge()

class Mascota:
    def __init__(self):
        print('se creo la mascota')

    def sientate(self):
        print('La mascota se sento')

class Felino:
    def __init__(self):
        print('se creo el felino')

    def ruge(self):
        print('El felino dio un rugido')

class Gato(Felino, Mascota):
    def __init__(self, energia, hambre):
        self.energia = energia
        self.hambre = hambre
        print('Se creo un gato', energia, hambre)


    def tomar_leche(self, leche_en_litros):
        self.hambre += leche_en_litros
        print('el gato toma su leche')

    def acariciar(self):
        print('prrrrr...')

    def jugar(self):
        if self.energia <= 0 or self.hambre <=1:
            print('el gato no quiero jugar')
        else:
            self.energia = self.energia - 1
            self.hambre -= 2
            print('al gato le encanta jugar')

    def dormir(self, horas):
        self.energia += horas
        print('el gato tomo una siesta')

def imprimemenu():
    print("1. Crear tu mascota gatuna")
    print("2. Jugar con tu gato")
    print("3. Dar de comer")
    print("4. Poner a dormir")
    #...
    op=input("Qué opción quieres elegir?: ")
    return op



'''
gato = Gato(5, 5)
# Se creo un gato
gato.acariciar()
# prrrrr...

gato.jugar()
# al gato le encanta jugar

gato.jugar()
# al gato le encanta jugar

gato.jugar()
# el gato no quiero jugar

print(gato.energia)
# 3

print(gato.hambre)
# 1

##SEGUNDA RONDA
gato.tomar_leche(4)
# el gato toma su leche
print(gato.hambre)
#gato.hambre
# 5
gato.jugar()
# al gato le encanta jugar print

gato.hambre
# 3

print(gato.energia)
# 2

gato.dormir(4)
print(gato.hambre)
print(gato.energia)

gato.sientate()


perro = Perro()

rugir(gato)
# 'El gato maulla'

rugir(perro)
# 'El perro ladra'

'''