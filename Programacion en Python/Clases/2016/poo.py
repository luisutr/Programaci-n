__author__ = 'luisutrilla'
# -*- coding: utf-8; mode: python -*-

class Antena(object):
    color = ""
    longitud = ""

class Pelo(object):
    color = ""
    textura = ""

class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""

class Objeto(object):
    color = "verde"
    tamanio = "grande"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()

    def flotar(self):
        print 12

class Dedo(object):
    longitud = "largos"
    forma = "fina"
    color = "claros"

class Pie(object):
    forma = "pezuña"
    color = "claro"
    dedos = Dedo()

# NuevoObjeto sí hereda de otra clase: Objeto
class NuevoObjeto(Objeto):
    pie = Pie()

    def saltar(self):
        pass

et = Objeto()
et.aspecto = "bonito"
print et.color
print et.tamanio
print et.aspecto
et.color = "rosa"
print et.color

ex = NuevoObjeto()
print ex.pie.forma
print ex.pie.dedos.color
print ex.aspecto
print ex.flotar()