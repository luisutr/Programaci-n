import csv

archivo = 'C:/Users/horus/OneDrive/OneDrive - Universidad de Castilla-La Mancha/CURSOS/FEMPCLM/EVALUACION EXTERNA/ENCUESTA/'

##ejercicio 1

def tests(archivo):
   f  = open(archivo, "rb")
   reader = csv.reader(f)
   listacomunidadesautonomas= []
   c = 0
   for numfila,i in enumerate(reader):
        for columna in i:
            if numfila == c:
                   listacomunidadesautonomas.append(columna)
                   c = c+1
       else:
           c = c+1
   f.close()
   return listacomunidadesautonomas
#print (comunidades_autonomas(archivo))


def principal():
    nombre = "ENCUESTA ALUMNOS CURSO "
    lista = []
    for i in range(1,3):
        tests(archivo+nombre+str(i))


print(principal())