import requests
from bs4 import BeautifulSoup
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

url = "http://es.wikipedia.org/wiki/Paraguay"
e = requests.get(url)
data = e.text

soup = BeautifulSoup(data, 'html.parser')

# Ejemplo de como imprimir todo
# print soup.prettify()

# Obtenemos la tabla

tabla_paraguay = soup.find_all('table', 'wikitable')[1]

# Obtenemos todas las filas
rows = tabla_paraguay.find_all("tr")

for row in rows:
    # obtenemos todas las columns
    cells = row.find_all("td")
    linea = ""
    for cell in cells:
        linea += cell.get_text() + '\t'

    #imprimos la fila
    print (linea)
