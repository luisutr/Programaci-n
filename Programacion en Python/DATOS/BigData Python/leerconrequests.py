# -*- coding: utf-8 -*-
import os, sys
import requests

r = requests.get('http://www.aemet.es/xml/municipios/localidad_28013.xml')
# Si r.status_code in range(200,300) entonces r.text es el documento
doc = r.text
print (r.status_code)
# Imprimir las 5 primeras líneas
print ('\n'.join(doc.split('\n')[:5]))