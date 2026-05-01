# -*- coding: utf-8; mode: python -*-

def comunidades_autonomas(ruta):
    comunidadescsv = open(ruta, "r")
    lista_com = []
    lista=[]
    for j in comunidadescsv:
        lista.append(j)
    for i in range(len(lista)):
        if (i > 10 and i < 29):
            fila = lista[i].strip()
            celdas = fila.split(',')
            for numero_columna, celda in enumerate(celdas):
                if numero_columna == 0:
                    lista_com.append(celda)
    comunidadescsv.close()
    return lista_com


print comunidades_autonomas("comunidades.csv")

def aprobados_pau(ruta):
    comunidadescsv = open(ruta, "r")
    dicc = {}
    lista=[]
    for j in comunidadescsv:
        lista.append(j)
    for i in range(len(lista)):
        if (i > 10 and i < 29):
            fila = lista[i].strip()
            celdas = fila.split(',')
            for j in range(len(celdas)):
                if j == 0:
                    comunidad = celdas[j]
                elif j == 11:
                    dicc[comunidad] = int(round(float(celdas[j].strip('"'))))
    comunidadescsv.close()
    return dicc

#print aprobados_pau('comunidades.csv')

def presentados_pau(ruta):
    comunidadescsv = open(ruta, "r")
    dicc = {}
    lista=[]
    for j in comunidadescsv:
        lista.append(j)
    for i in range(len(lista)):
        if (i > 10 and i < 29):
            fila = lista[i].strip()
            celdas = fila.split(',')
            for j in range(len(celdas)):
                if j == 0:
                    comunidad = celdas[j]
                elif j == 1:
                    dicc[comunidad] = float(celdas[j].strip('"'))
    comunidadescsv.close()
    return dicc

def suspuensos_pau(ruta, comunidad):
    presentados = presentados_pau(ruta)
    aprobados = aprobados_pau(ruta)
    for i in presentados:
        if i == comunidad:
            numero_presentados = presentados[i]
    for j in aprobados:
        if j == comunidad:
            numero_aprobados = aprobados[j]

    suspensos = numero_presentados - numero_aprobados
    return suspensos

#print suspuensos_pau("comunidades.csv", "Canarias")

def porcentajeaprobados_pau(ruta):
    comunidadescsv = open(ruta, "r")
    dicc = {}
    lista=[]
    for j in comunidadescsv:
        lista.append(j)
    for i in range(len(lista)):
        if (i > 10 and i < 29):
            fila = lista[i].strip()
            celdas = fila.split(',')
            for j in range(len(celdas)):
                if j == 0:
                    comunidad = celdas[j]
                elif j == 21:
                    naprobados = float(celdas[j].strip('"'))
            dicc[comunidad] = naprobados
    comunidadescsv.close()
    return dicc

def comunidad_mas_aprobados(directorio):
    aprobados = porcentajeaprobados_pau(directorio)
    nota_max = 00000.00
    for j in aprobados:
        if (aprobados[j] > nota_max):
            nota_max = aprobados[j]
            mas_aprobados = j
    return mas_aprobados


#print comunidad_mas_aprobados('comunidades.csv')


def aprobados_mes(ruta, mes):
    comunidadescsv = open(ruta, "rb")
    diccionario = {}
    lista=[]
    for j in comunidadescsv:
        lista.append(j)
    for i in range(len(lista)):
        if (i > 10 and i < 29):
            fila = lista[i].strip()
            celdas = fila.split(',')
            for j in range(len(celdas)):
                if j == 0:
                    comunidad = celdas[j]
                if (j == mes):
                    diccionario[comunidad] = float(celdas[j].strip('"'))
    comunidadescsv.close()
    return diccionario


def comunidad_mas_diferenciada(directorio):
    junio = aprobados_mes(directorio, 23)
    septm = aprobados_mes(directorio, 25)
    diferenciada = 0.000000
    tupladef = 0.00000000
    for i in junio:
        if ((float(junio[i]) - float(septm[i])) > diferenciada):
            diferenciada = float(junio[i]) - float(septm[i])
            mas_diferenciada = i
            tupladef = (mas_diferenciada, diferenciada / 100)
    return tupladef


#print comunidad_mas_diferenciada('comunidades.csv')
