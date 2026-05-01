__author__ = 'PORTATIL'

# -*- coding: utf-8 -*-
import csv

# ejercicio 1

archivo = 'comunidades.csv'

def comunidades_autonomas(directorio):
    archivo = open(directorio, "r")  #r nos dice que lee el archivo
    lista_comunidades = []  #creamos una lista en la que posteriormente anadiremos comunidades con append
    for num_fila, linea in enumerate(archivo):
        if (num_fila > 10 and num_fila < 29):
            fila = linea.strip()  # elimina espacios en blanco de delante y detras de la linea(strip)
            celdas = fila.split(',')  # separa los caracteres en este caso por una coma (split)
            for num_columna, celda in enumerate(celdas):
                if num_columna == 0:
                    lista_comunidades.append(celda)
    archivo.close()
    return lista_comunidades


print comunidades_autonomas(archivo)


#ejercicio2

def aprobados_pau(directorio):
    archivo = open(directorio, "r")
    diccionario = {}
    for num_fila, linea in enumerate(archivo):  #enumerate= a cada linea del archivo le da un valor, numero de fila
        if (num_fila > 10 and num_fila < 29):
            fila = linea.strip()
            celdas = fila.split(',')
            for num_columna, celda in enumerate(celdas):
                if num_columna == 0:
                    comunidad = celda
                elif num_columna == 11:
                    diccionario[comunidad] = int(round(float(celda.strip('"'))))

                    #Le hago el strip de " porque cuando lo anado al diccionario ya es un string
                    # y lo inerta con comillas simples y luego luego dobles. De esta manera, hago que quite una de esas
                    #comillas y con la funcion float hago que ese string lo convierta a decimal.
    archivo.close()
    #la funcion close, lo que hace es cerrar el proceso abierto en memoria del equipo que hace que este usando el archivo
    #de esta manera libero este proceso para que no este en memoria, cuando haya terminado de usarlo.
    #esta es una buena practica de programador y eficiencia de uso del equipo.
    #return sorted(dicc.items())
    #sorted lo malo es que en vez de devolver un diccionario, devuelve una lista de tuplas.
    #que luego no voya poder trabajar igual que si fuese un diccionario. Como en el enunciado no es
    #un requisito que el diccionario devuelto este ordenado, he preferido usarlo asi.
    return diccionario


#print "Aprobados PAU:",
#print aprobados_pau("C:\Users\PORTATIL\Downloads\pcaxis637310428.csv")


def porcentaje_aprobado_pau(directorio):
    archivo = open(directorio, "r")
    diccionario = {}
    for num_fila, linea in enumerate(archivo):
        if (num_fila > 10 and num_fila < 29):
            fila = linea.strip()
            celdas = fila.split(',')
            for num_columna, celda in enumerate(celdas):
                if num_columna == 0:
                    comunidad = celda
                elif num_columna == 21:
                    diccionario[comunidad] = float(celda.strip('"'))
    archivo.close()
    return diccionario


##ejercicio3

def presentados_pau(directorio):
    archivo = open(directorio, "r")
    diccionario = {}
    for num_fila, linea in enumerate(archivo):
        if (num_fila > 10 and num_fila < 29):
            fila = linea.strip()
            celdas = fila.split(',')
            for num_columna, celda in enumerate(celdas):
                if num_columna == 0:
                    comunidad = celda
                elif num_columna == 1:
                    diccionario[comunidad] = int(round(float(celda.strip('"'))))
    archivo.close()
    #return sorted(dicc.items()) #para que te ordene por orden alfabetico la lista
    return diccionario  #no te ordena la lista por orden alfabetico


#print "Presentados PAU:",
#print presentados_pau("C:\Users\PORTATIL\Downloads\pcaxis637310428.csv")


def suspensos_pau(directorio, comunidad):
    #suspensos = 00000.0
    presentados = presentados_pau(directorio)
    aprobados = aprobados_pau(directorio)
    for i in presentados:
        if i == comunidad:
            numero_presentados = presentados[i]
    for j in aprobados:
        if j == comunidad:
            numero_aprobados = aprobados[j]

    suspensos = numero_presentados - numero_aprobados
    return suspensos


#print "Suspensos Pau en Canarias: ",
#print suspuensos_pau("C:\Users\PORTATIL\Downloads\pcaxis637310428.csv","Canarias")


##ejercicio4

def comunidad_mas_aprobados(directorio):
    aprobados = porcentaje_aprobado_pau(directorio)
    nota_maxima = 00000.00
    for j in aprobados:
        if (aprobados[j] > nota_maxima):
            nota_maxima = aprobados[j]
            mas_aprobados = j
    return mas_aprobados


#print "Comunidad mas Aprobados:",
#print comunidad_mas_aprobados("C:\Users\PORTATIL\Downloads\pcaxis637310428.csv")


##ejercicio5

def aprobados_mes(directorio, mes):
    archivo = open(directorio, "r")
    reader = csv.reader(archivo)
    contador = 0
    diccionario = {}
    for num_fila, row in enumerate(reader):
        if (num_fila + 1 > 11):
            for num_columnas, columnas in enumerate(row):
                if (num_columnas == 0):
                    comunidad = columnas
                    contador = contador + 1
                if (num_columnas == mes):
                    diccionario[comunidad] = columnas
                    contador = contador + 1
        else:
            contador = contador + 1

    archivo.close()
    return diccionario


def comunidad_mas_diferenciada(directorio):
    #comunidad con mayor direfencia entre aprobados en junio y septiembre
    junio = aprobados_mes(directorio, 23)
    septm = aprobados_mes(directorio, 25)
    diferenciada = 0.0
    for i in junio:
        if ((float(junio[i]) - float(septm[i])) > diferenciada):
            diferenciada = float(junio[i]) - float(septm[i])
            mas_diferenciada = i
            tupla = (mas_diferenciada, diferenciada)
    return tupla

#print "Comunidad mas diferenciada: ",
#print comunidad_mas_diferenciada("C:\Users\PORTATIL\Downloads\pcaxis637310428.csv")
