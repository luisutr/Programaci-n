
# coding: utf-8

# # Ejemplo de WebScraping con Python
# ## Obtener Ibex35 bolsa de Madrid

# In[ ]:


# import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# In[3]:


# indicar la ruta
url_page = 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'


# In[4]:


# tarda 480 milisegundos
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")


# In[5]:


# Obtenemos la tabla por un ID específico
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndices'})
tabla


# In[18]:


name=""
price=""
nroFila=0
for fila in tabla.find_all("tr"):
    if nroFila==1:
        nroCelda=0
        for celda in fila.find_all('td'):
            if nroCelda==0:
                name=celda.text
                print("Indice:", name)
            if nroCelda==2:
                price=celda.text
                print("Valor:", price)
            nroCelda=nroCelda+1
    nroFila=nroFila+1


# In[20]:


# Abrimos el csv con append para que pueda agregar contenidos al final del archivo
with open('bolsa_ibex35.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])


############################ Obtener resultados de Futbol #################################
# ## Ejemplo Liga BBVA - España - Primera -  desde marcadores.com

# In[38]:


url_page = 'https://www.marcadores.com/futbol/espana/liga-bbva/?competitionRoundId=486942' # jornada 20


# In[39]:


# tarda 1500 milisegundos
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")


# In[ ]:


# Obtenemos la tabla por un ID específico
tabla = soup.find('table', attrs={'class': 'matches'})
tabla


# In[47]:


data = []
equipo1=""
equipo2=""
resultado=""
nroFila=0
for fila in tabla.find_all("tr"):
    if nroFila>0:
        nroCelda=0
        capturar=False
        for celda in fila.find_all('td'):
            if nroCelda==1 and celda.text=='Fin.':
                capturar=True
            if capturar and nroCelda==2:
                equipo1=celda.text
            if capturar and nroCelda==4:
                equipo2=celda.text
            if capturar and nroCelda==5:
                resultado=celda.text
                print("Partido:", equipo1,'vs',equipo2,resultado)
                data.append((equipo1,equipo2,resultado))
            nroCelda=nroCelda+1
    nroFila=nroFila+1


# In[49]:


# Abrimos el csv con append para que pueda agregar contenidos al final del archivo
with open('partidos_liga_primera.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for equipo1, equipo2,resultado in data:
        writer.writerow([equipo1, equipo2, resultado,datetime.now()])


################### Otros ejemplos de WebScaping ############################

# In[93]:


#supongamos tenemos el siguiente HTML
pagina_web = "<html>"             + "<head></head>"             + "<body>"                 + "<div class='contenedor'>"                     + "<div id='123' name='bloque_bienvenida' class='verde'>"                         + "Bienvenido a mi web"                     + "</div>"                 + "</div>"             + "</body>"             + "</html>"


# In[94]:


soup = BeautifulSoup(pagina_web, "lxml")


# In[95]:


#Obtener por ID:
elTexto = soup.find('div', attrs={'id': '123'}).getText()
print(elTexto)


# In[96]:


#Obtener por Clase CSS:
elTexto = soup.find('div', attrs={'class': 'verde'}).getText()
print(elTexto)


# In[97]:


#Obtener dentro de otra etiqueta anidado:
elTexto = next(soup.div.children).getText() #con next obtiene primer "hijo"
print(elTexto)


# ## Obtener items de un listado

# In[98]:


#supongamos tenemos el siguiente HTML
pagina_web = "<html>"     + "<head></head>"     + "<body>"         + "<div class='contenedor'>"             + "<ul>"                 + "<li>Perro</li>"                 + "<li>Gato</li>"                 + "<li>Tortuga</li>"             + "</ul>"         + "</div>"     + "</body>"     + "</html>"


# In[99]:


soup = BeautifulSoup(pagina_web, "lxml")


# In[100]:


for child in soup.ul.children:
    print(child.getText())


# In[101]:


items = soup.find_all('li')
for item in items:
    print(item.getText())


# ## Obtener Enlaces

# In[102]:


#supongamos tenemos el siguiente HTML
pagina_web = "<html>"     + "<head></head>"     + "<body>"         + "<div class='contenedor'>"             + "<ul>"                 + "<li><a href='http://www.google.com'>Google</a></li>"                 + "<li><a href='http://www.yahoo.com'>Yahoo</a></li>"                 + "<li><a href='http://www.bing.com'>Bing</a></li>"             + "</ul>"         + "</div>"     + "</body>"     + "</html>"


# In[103]:


soup = BeautifulSoup(pagina_web, "lxml")


# In[105]:


items = soup.find_all('a')
for item in items:
    print(item['href'])


# ## Ejemplo completo Extraer enlaces

# In[107]:


url_page = 'https://www.lifeder.com/cientificos-famosos/'
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")
contenido = soup.find('div', attrs={'class': 'td-post-content'})
items = contenido.find_all('a')
for item in items:
    print(item['href'])


# El artículo completo en www.aprendemachinelearning.com
