# -*- coding: utf-8 -*-
import pandas as pd
import codecs
def cursos():
    df = pd.read_excel('cursos.xlsx', sheet_name='Hoja1')
    salida = codecs.open("cursos.html", "w+")
    columnas = ["CD", "NOMBRE", "AREA", "MODALIDAD", "PLAZAS", "HORAS", "EDICIONES"]
    '''CD	NOMBRE	AREA	MODALIDAD	PLAZAS	HORAS	EDICIONES'''
    df_seleccionados = df[columnas]
    print(df_seleccionados)
    for i in range(len(df_seleccionados)):
        '''
        Codigo del curso
        Nombre
        Plazas
        Horas
        Modalidad
        Número de ediciones
        Area 
        '''
        if(str(df_seleccionados["CD"][i])) != "NaN":
            salida.write("<h2>"+str(df_seleccionados["NOMBRE"][i]) + "</h2>")
            salida.write("<p class='MsoNormal''>")
            salida.write("<b>Código del curso: </b>"+str(df_seleccionados["CD"][i]))
            salida.write("</p>")
            salida.write("<p class='MsoNormal''>")
            salida.write("<b>Nombre del curso: </b>" + str(df_seleccionados["NOMBRE"][i]))
            salida.write("</p>")
            salida.write("<p class='MsoNormal''>")
            salida.write("<b>Plazas: </b>" + str(int(df_seleccionados["PLAZAS"][i])))
            salida.write("</p>")
            salida.write("<p class='MsoNormal'>")
            salida.write("<b>Horas del curso: </b>"+str(int(df_seleccionados["HORAS"][i])))
            salida.write("</p>")
            salida.write("<p class='MsoNormal'>")
            salida.write("<b>Modalidad: </b>" + str(df_seleccionados["MODALIDAD"][i]))
            salida.write("</p>")
            salida.write("<p class='MsoNormal'>")
            salida.write("<b>Ediciones del curso: </b>"+str(int(df_seleccionados["EDICIONES"][i])))
            salida.write("</p>")
            salida.write("<p class='MsoNormal'>")
            salida.write("<b>Área: </b>" + str(df_seleccionados["AREA"][i]))
            salida.write("</p> ***-")

cursos()