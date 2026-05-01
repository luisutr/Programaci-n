from bs4 import BeautifulSoup
import requests

URL = "http://www.infocif.es/ficha-empresa/mercadona-sa"

req = requests.get(URL)

status_code = req.status_code
if status_code == 200:
    html = BeautifulSoup(req.text, "html.parser")
    entradas = html.find_all('div', {'id': 'collapsecargos'})
    entrada = entradas[0]
    cif = entrada.find('h2', {'class': 'editable col-md-10 col-sm-9 col-xs-12 mb10 text-right'}).getText()
    campos = html.find_all('p', {'class': 'editable col-md-10 col-sm-9 col-xs-12 mb10 text-right'})
    print cif
    for num,i in enumerate(campos):
        campo = i.getText()
        if num == 1:
            x = campo.split("\"")
            print x[19]
            print x[27]
            print x[31],
            print x[32]
        elif num != 0:
            print campo.strip()


else:
    print(status_code)
