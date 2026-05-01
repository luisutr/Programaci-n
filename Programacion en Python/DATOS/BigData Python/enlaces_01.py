# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

from bs4 import BeautifulSoup
import requests

URL_BASE = "http://jarroba.com/"
MAX_PAGES = 20
counter = 0

url = URL_BASE
req = requests.get(url)
# Comprobamos que la petición nos devuelve un Status Code = 200
statusCode = req.status_code
if statusCode == 200:
    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    soup = BeautifulSoup(req.text, "html.parser")
    redditAll = soup.find_all("a")
    for links in redditAll:
        print(links.get('href'))
