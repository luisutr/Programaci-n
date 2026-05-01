# -*- coding: utf-8 -*-
import csv
import codecs
import time
ruta = 'vanessa2016.csv'


def textos(archivo):
    f = codecs.open(archivo, "rb")
    salida = codecs.open("vanessa2016.html", "w+")
    salida.write("<!doctype html><html><head><meta charset='UTF-8'><title>vanessa2016</title></head><body style='text-align: center'>")
    reader = csv.reader(f)
    mes = "ENERO"
    auxmes = ""
    for fila in reader:
        #print(fila)
        celdas = fila[0].split(';')  # separa los caracteres en este caso por una coma (split)
        for numcolumna,celda in enumerate(celdas):
            if numcolumna == 1:
                piefoto = ("<p>"+celda+"</p>")
            if numcolumna == 2:
                #salida.write("<figure><img src='"+celda+"' alt='' width='100%'/>")
                imagen = ("<figure><img src='" + celda + "' alt='' width='100%'/>")
            if numcolumna == 4:# fecha
                fecha = ("<figcation><p>"+celda+"</p></figcation></figure>")
                listames = celda.split(' ')
                if len(listames) > 1:
                    mes = listames[2]
                if auxmes != mes.upper():
                    salida.write("|***" + mes.upper() + "***|")
                    auxmes = mes.upper()
                salida.write(imagen)
                salida.write(fecha)
                salida.write("-***-"+piefoto+"-***-</br>")

            #time.sleep(1)
    f.close()
    salida.write("</body></html>")

    salida.close()

textos(ruta)

