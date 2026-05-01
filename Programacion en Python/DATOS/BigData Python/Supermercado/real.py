# -*- coding: utf-8 -*-
import requests,unicodedata
from bs4 import BeautifulSoup
import os, ssl
import time
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


#método de análisis de una dirección web
def analisisDescarga(archivo,html):
    #html = conexion.read()
    soup = BeautifulSoup(html, 'html.parser')
    #obtenemos una lista de String con la condición de atributos class con valores details y price
    nombres = soup.findAll('span', attrs={'class': 'details'})
    precios = soup.findAll('p', attrs={'class': 'price'})
    #la lista alterna valores de nombre de producto y precio
    #   creamos una bandera para diferenciar si es valor o producto
    for i in range(len(nombres)):
            nombre = nombres[i].text.strip()
            precio = precios[i].text.strip()
            #adaptamos unicode a utf-8
            #normalizadonombre=unicodedata.normalize('NFKD', nombre).encode('ascii','ignore')
            #normalizadoprecio = unicodedata.normalize('NFKD', precio).encode('ascii', 'ignore')
            print('producto: ' + nombre)
            archivo.write(nombre + '\t')
            print('precio: '+precio)
            archivo.write(precio+'\n')
            print("--")
#este método se conectará con la web y establece un timeout que obliga a reintentar el fallo
def preparar(archivo,web,x):
    try:
        print(web)
        # Capturamos el hml de la pagina web y creamos un objeto Response
        r = requests.get(web)
        data = r.text
        time.sleep(5)
        analisisDescarga(archivo,data)
    except:
        print("Tiempo de espera agotado, volviendo a intentar")
        preparar(archivo,web,x)

#Programa principal
print('Comienza el programa')
archivo=open('productoPrecio.csv','w')
#El CSV separa las columnas por medio de tabuladores
for x in range(2,9):
    #Ruta de la página web
    url = 'https://www.dia.es/compra-online/productos/c/WEB.000.000.00000?q=%3Aname-asc&page='+str(x)+'&disp='
    #'https://www.dia.es/compra-online/productos/c/WEB.000.000.00000?q=%3Aname-asc&page='+str(x)+'&disp='
    preparar(archivo,url,x)

archivo.close()
print('Fin del programa')
