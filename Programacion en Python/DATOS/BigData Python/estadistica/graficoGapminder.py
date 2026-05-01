#Se importa las librerias matplitlib, numpy, pandas, seaborn
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")
import pandas as pd
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

my_dpi=96

# Se obtiene los datos en formato csv  y se convierte en un dataframe
url = 'https://python-graph-gallery.com/wp-content/uploads/gapminderData.csv'
data = pd.read_csv(url)

#Se muestra el data frame
data.head()

#Se revisa los tipos de datos de las columnas
data.info()

# Transformar los datos de la columna continente a categoria.
data['continent']=pd.Categorical(data['continent'])
data.head()

#Se vuelve a revisar los tipos de las columnas y ahora se tiene que contienen es categoria
data.info()

'''Ahora se generará las gráficas por año de experanza de vida y PIB por año, 
cada gráfica se almacena con su nombre y año a fin de que luego con Image Magick se convierta en un gif animado'''

# Por cada año
for i in data.year.unique():
    # inicializa la figura
    fig = plt.figure(figsize=(680 / my_dpi, 480 / my_dpi), dpi=my_dpi)
    # se cambia de color con c y alpha, se mapea el color del eje X.
    tmp = data[data.year == i]
    plt.scatter(tmp['lifeExp'], tmp['gdpPercap'], s=tmp['pop'] / 200000, c=tmp['continent'].cat.codes, cmap="Accent",
                alpha=0.6, edgecolors="white", linewidth=2)
    # Se agrega el título, y los ejes.
    plt.yscale('log')
    plt.xlabel("Experanza de vida")
    plt.ylabel("PIB per capita")
    plt.title("Año: " + str(i))
    plt.ylim(0, 100000)
    plt.xlim(30, 90)

    # Se salva el archivo como png, cada archivo por año.
    filename = 'Gapminder_step' + str(i) + '.png'
    plt.savefig(filename, dpi=96)
    plt.gca()

#para hacer los png animados. Usando la terminal  conel siguiente comando
#instalar brew install imagemagick --> http://macappstore.org/imagemagick/
#magick convert *.png animated_gapminder.gif
