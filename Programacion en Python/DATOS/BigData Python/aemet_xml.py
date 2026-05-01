#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sitio: http://www.pythondiario.com
# Autor: Diego Caraballo

# Haciendo pruebas con BeautifulSoup y requests

# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import time
import os

# Creamos el Bucle infinito
while True:

 # Capturamos la url
 url = "http://www.aemet.es/es/eltiempo/prediccion/municipios/madrid-id28079"

 # Capturamos el hml de la pagina web y creamos un objeto Response
 r  = requests.get(url)
 data = r.text

 # Creamos el objeto soup y le pasamos lo capturado con request
 soup = BeautifulSoup(data, 'lxml')

 # Buscamos el div para sacar los grados
 temp = soup.find_all('h2', class_="titulo")

 # Buscamos el div para sacar la sensacion termica
 sTerm = soup.find_all('div', class_="no_wrap")

        # Con [0] saco el primer elemento y con [1] el segundo
 print ("La temperatura en Madrid: " + temp[0].text)
 for i in range(len(sTerm)):
    print ("La sesacion termica: " + sTerm[i].text)

 # Tiempo en segundos para ejecutarse nuevamente
 time.sleep(5)

 # Boramos los datos viejos, para Windows es "cls"
 # Boramos los datos viejos, para Mac es "clear"
 os.system("cls")
