__author__ = 'juancarlos'

import csv

archivo = 'comunidades.csv'

##ejercicio 1

def comunidades_autonomas (archivo):
   f  = open(archivo, "rb")
   reader = csv.reader(f)
   listacomunidadesautonomas= []
   c = 0
   for numfila,i in enumerate(reader):
       if numfila > 10:
           for columna in i:
               if numfila == c:
                   listacomunidadesautonomas.append(columna)
                   c = c+1
       else:
           c = c+1
   f.close()
   return listacomunidadesautonomas
print comunidades_autonomas(archivo)

##ejercicio 2
def aprobados_porcentajetotal(archivo):
   f = open(archivo, "rb")
   diccionario = {}

   for numfila,linea in enumerate(f) :

       if(numfila > 10) and (numfila < 29):
           fila = linea.strip()

           celda = fila.split(',')
           for numcolumna, celda in enumerate(celda):
               if numcolumna == 0:
                   comunidad = celda
               elif numcolumna == 21:
                   diccionario[comunidad] = float(celda.strip('"'))
   f.close()
   return diccionario


def aprobados_pau(archivo):
   f = open(archivo, "rb")
   diccionario = {}
   for numfila,linea in enumerate(f):
       if(numfila > 10) and (numfila < 29):
           fila = linea.strip()
           celda = fila.split(',')
           for numcolumna, celda in enumerate(celda):
               if numcolumna == 0:
                   comunidad = celda
               elif numcolumna == 11:
                   diccionario[comunidad] = int(round(float(celda.strip('"'))))
   f.close()
   return diccionario
##print aprobados_pau(archivo)

##ejercicio 3
def presentados_pau (archivo):
   f  = open(archivo, "rb")
   diccionario = {}
   for numfila,linea in enumerate(f):
       if(numfila > 10) and (numfila < 29):
           fila = linea.strip()
           celda = fila.split(',')
           for numcolumna, cel in enumerate(celda):
               if numcolumna == 0:
                   comunidad = cel
               elif numcolumna == 1:
                   diccionario[comunidad] = int(round(float(cel.strip('"'))))
   f.close()
   return diccionario

##ejercicio 3

def suspensos_pau(archivo,comunidad):
   presentados = presentados_pau(archivo)
   aprobados = aprobados_pau(archivo)
   for i in presentados:
       if i == comunidad:
           numpresentados = presentados[i]
   for j in aprobados:
       if j == comunidad:
           numaprobados = aprobados[j]
   suspensos = (numpresentados-numaprobados)
   return suspensos
##print suspensos_pau(archivo, comunidad)


## ejercicio 4

def comunidad_mas_aprobados(archivo):
   aprobados = aprobados_porcentajetotal(archivo)
   maxima = 00000.00
   for i in aprobados:
       if aprobados[i]>maxima:
           maxima=aprobados[i]
           mas_aprobados = i
   return mas_aprobados
print comunidad_mas_aprobados(archivo)

##ejercicio 5

def aprobados_mes(archivo, mes):
   f  = open(archivo, "rb")
   reader = csv.reader(f)
   diccionario = {}
   c = 0
   for numfila, colum in enumerate(reader):
       if(numfila +1) > 11:
           for numcol,col in enumerate(colum):
               if(numcol == 0):
                   comunidad = col
                   c = c+1
               if (numcol == mes):
                   diccionario[comunidad] = col
                   c = c+1
       else:
           c = c+1
   f.close()
   return diccionario

def comunidad_mas_diferencia(archivo):
   junio = aprobados_mes(archivo, 23)

   septiembre = aprobados_mes(archivo, 25)

   dif = 0.0
   for i in junio:
       if ((float(junio[i]) - float(septiembre[i])) > dif):
           dif = (float(junio[i])-float(septiembre[i]))
           resultadopor= dif/100
           masdif = i
   return (masdif,resultadopor)

print comunidad_mas_diferencia(archivo)

