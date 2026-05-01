# -*- coding: utf-8 -*-
import csv


def columnas(num_fila, linea):
    celdas = []
    if (num_fila > 10 and num_fila < 29):
        fila = linea.strip()
        celdas = fila.split(',')
    return celdas


def comunidades_autonomas(directorio):
    documento = open(directorio, "r")
    lista_comunidades = []
    for num_fila, linea in enumerate(documento):
        celdas = columnas(num_fila, linea)
        for num_columna, celda in enumerate(celdas):
            if num_columna == 0:
                lista_comunidades.append(celda)
    documento.close()
    return lista_comunidades


def aprobados_pau(directorio):
    documento = open(directorio, "r")
    diccionario = {}
    for num_fila, linea in enumerate(documento):
        celdas = columnas(num_fila, linea)
        for num_columna, celda in enumerate(celdas):
            if num_columna == 0:
                comunidad = celda
            elif num_columna == 11:
                diccionario[comunidad] = float(celda.strip('"'))
    documento.close()
    return diccionario


def porcentaje_aprobado_pau(directorio):
    documento = open(directorio, "r")
    diccionario = {}
    for num_fila, linea in enumerate(documento):
        celdas = columnas(num_fila, linea)
        for num_columna, celda in enumerate(celdas):
            if num_columna == 0:
                comunidad = celda
            elif num_columna == 21:
                diccionario[comunidad] = float(celda.strip('"'))
    documento.close()
    return diccionario


def presentados_pau(directorio):
    documento = open(directorio, "r")
    diccionario = {}
    for num_fila, linea in enumerate(documento):
        celdas = columnas(num_fila, linea)
        for num_columna, celda in enumerate(celdas):
            if num_columna == 0:
                comunidad = celda
            elif num_columna == 1:
                diccionario[comunidad] = float(celda.strip('"'))
    documento.close()
    return diccionario


def suspensos_pau(directorio, comunidad):
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


def comunidad_mas_aprobados(directorio):
    aprobados = porcentaje_aprobado_pau(directorio)
    nota_maxima = 0
    for j in aprobados:
        if (aprobados[j] > nota_maxima):
            nota_maxima = aprobados[j]
            mas_aprobados = j
    return mas_aprobados


def comunidad_mas_diferenciada(directorio):
    documento = open(directorio, "r")
    junio, septm = {}, {}
    diferenciada = 0.0
    for num_fila, linea in enumerate(documento):
        celdas = columnas(num_fila, linea)
        for num_columna, celda in enumerate(celdas):
            if (num_columna == 0):
                comunidad = celda
            if (num_columna == 23):
                junio[comunidad] = float(celda.strip('"'))
            elif (num_columna == 25):
                septm[comunidad] = float(celda.strip('"'))
    for comunidad in junio:
        if ((float(junio[comunidad]) - float(septm[comunidad])) > diferenciada):
            diferenciada = float(junio[comunidad]) - float(septm[comunidad])
            tupla = (comunidad, diferenciada / 100)
    return tupla
