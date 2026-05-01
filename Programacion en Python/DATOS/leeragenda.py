__author__ = 'luisutrilla'

import requests
import xml.etree.ElementTree as ET

def agenda():
    dicctemmun={}
    diccionario={}
    diccxml={}
    r = requests.get("http://www.toledo.es/agenda/")
    if r.status_code != 404:
        xml = r.text.encode('utf_8')
        root = ET.fromstring(xml)
        localidad = root.find('nombre').text
        for dia in root.iter('dia'):
                fecha = str(format(dia.get('fecha')))
                t = dia.find('temperatura')
                maxima = t.find('maxima').text
                minima = t.find('minima').text
                absoluta = int(format(minima)) + int(format(maxima)) / 2
                dicctemmun[fecha] = absoluta
        diccionario[localidad] = dicctemmun
        diccxml[localidad] = fecha
    return diccionario, diccxml

print agenda()
