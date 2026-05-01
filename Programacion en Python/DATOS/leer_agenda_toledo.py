# -*- coding: utf-8 -*-
import os, sys

import urllib


def obtengocodigo():
    f = urllib.urlopen('http://www.toledo.es/agenda/')
    if f.getcode() != 404:
        # Imprime las 10 primeras líneas
        espera = 0
        imp = False
        fecha = []
        categoria = []
        evento = []
        guardar = False
        contador = 0
        for i,linea in enumerate(f):
            if "mcabc" in linea:
                for j in range(len(linea)):
                    if linea[j] == "<" and linea[j+1] == "/":
                        guardar = False
                    if guardar == True and i == 40:
                        fecha.append(linea[j])
                    if guardar == True and i == 41:
                        categoria.append(linea[j])
                    if linea[j] == ">" and linea[j-1] != "d" and guardar == False:
                        guardar = True
            # mete todos los eventos    
            if "<td nowrap bgcolor=\"lightyellow\" valign=\"top\">" in linea:
                evento.append("<td>")
                contador = 27
            if contador>0:
                evento.append(linea)
                contador -= 1
            #if "#<b><u>" in linea:
               # evento.append(linea)
           #if espera !=0 and imp == True:
            #     espera -= 1
            # if espera == 0 and imp == True:
            #     print linea
            #     imp = False
            # if "#F5DEB3" in linea:
            #     espera = 4
            #     imp = True
        print ''.join(fecha)
        print ''.join(categoria)
        print ''.join(evento)

        # las que tienen nowrap bgcolor="lightyellow" valign="top" y coger siempre 30 lineas html que son las que mandamos a wp
                # o escribo por bbdd como nuevas entrdas portfolio.
                # vinculado con la importacion de ....

          #if i<1669:
            #continue
          #elif i>2389:
              #continue
          #else:
            #print  linea

obtengocodigo()
