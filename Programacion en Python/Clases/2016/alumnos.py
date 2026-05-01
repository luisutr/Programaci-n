__author__ = 'luisutrilla'
# -*- coding: utf-8; mode: python -*-

class Alumno:
    'Clase para alumnos'
    numalumnos = 0
    sumanotas = 0

    def __init__(self, nombre, nota):
        print "Se creo alumno"
        self.nombre = nombre
        self.nota = nota
        Alumno.numalumnos += 1
        Alumno.sumanotas += nota

    def mostrarNombreNota(self):
        return(self.nombre, self.nota)

    def mostrarNumAlumnos(self):
        return(Alumno.numalumnos)

    def mostrarSumaNotas(self):
        return(Alumno.sumanotas)

    def mostrarNotaMedia(self):
        if Alumno.numalumnos > 0:
            return(Alumno.sumanotas/Alumno.numalumnos)
        else:
            return("Sin alumnos")


alumno1 = Alumno("Maria", 8)
alumno2 = Alumno("Carlos", 6)

print(alumno1.nombre)  # María
print(alumno1.nota)  # 8

alumno1.nombre = "Carmela"

print(Alumno.numalumnos)  # 2
print(Alumno.sumanotas)  # 14

print(alumno1.mostrarNombreNota())  # ('Carmen', 8)
print(alumno2.mostrarNombreNota())  # ('Carlos', 6)

del alumno1.nombre
