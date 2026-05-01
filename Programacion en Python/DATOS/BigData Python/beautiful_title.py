# Importamos las librerias
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, ssl
import time
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

def beautiful_title(url):
    try:
        # using the BeaitifulSoup module
        soup = BeautifulSoup(urlopen(url), "html.parser")

        # displaying the title
        print(soup.title.get_text())
        print(url)
    except:
        # Whoops it wasn't a 200
        print("Error de concexión")
        print(url)


urls = ["https://www.aulaclic.es/excel-2016"]
        #"https://tutorialexcel.com/utilizacion-de-los-comentarios-en-excel/", "https://www.softzone.es/programas-top/excel/como-anadir-editar-eliminar-notas-comentarios-excel/", "https://www.ionos.es/digitalguide/online-marketing/vender-en-internet/control-de-cambios-en-excel/", "https://cincodias.elpais.com/cincodias/2019/12/17/lifestyle/1576579882_881785.html", "https://excelyvba.com/personalizar-la-cinta-de-opciones/", "https://ayudaexcel.com/personalizar-cinta-de-opciones-excel/", "https://www.aulaclic.es/excel-2016/t_6_3.htm#ap_06_04", "https://excelcontabilidadytic.com/excel-funciones-estadisticas-basicas/", "https://exceltotal.com/la-funcion-texto-en-excel/#:~:text=La%20funci%C3%B3n%20TEXTO%20en%20Excel%20nos%20ayuda%20a%20convertir%20un,con%20otra%20cadena%20de%20texto.", "https://tutorialexcel.com/la-validacion-de-datos/", "https://exceltotal.com/validacion-de-datos-en-excel/", "https://www.solvetic.com/tutoriales/article/10205-como-crear-un-esquema-automatico-en-excel/", "https://www.excelfreeblog.com/tabla-vs-lista-estructurada/", "https://www.xataka.com/basics/como-ordenar-alfabeticamente-celdas-excel", "https://www.solvetic.com/tutoriales/article/3659-como-ordenar-y-clasificar-datos-en-excel/", "https://www.ionos.es/digitalguide/online-marketing/vender-en-internet/subtotales-de-excel/", "https://exceltotal.com/activar-excel-solver/", "https://www.solvetic.com/tutoriales/article/6743-como-usar-solver-en-excel-2019-excel-2016/", "https://exceltotal.com/base-de-datos-en-excel/", "https://www.adslzone.net/como-se-hace/excel/base-datos/", "https://funciones.excel-avanzado.com/category/ejemplos-de-funciones-de-base-de-datos/", "https://excelparatodos.com/graficos-en-excel/", "https://excelparatodos.com/graficos-en-excel/", "https://www.ionos.es/digitalguide/online-marketing/vender-en-internet/crear-graficos-en-excel/", "https://excelparatodos.com/funciones-logicas-en-excel/#:~:text=Son%20funciones%20que%20nos%20permiten,y%20el%20%E2%80%9Coperador%20O%E2%80%9D.", "https://support.microsoft.com/es-es/office/funciones-l%C3%B3gicas-referencia-e093c192-278b-43f6-8c3a-b6ce299931f5", "https://www.adslzone.net/como-se-hace/excel/buscar-datos/", "https://www.funcionesexcel.com/", "https://support.microsoft.com/es-es/office/funci%C3%B3n-buscarx-b7fd680e-6d10-43e6-84f9-88eae8bf5929", "https://www.ionos.es/digitalguide/online-marketing/vender-en-internet/excel-buscarh/", "https://excelnoconvencional.com/funcion-indice-y-coincidir-guia-practica/", "https://www.ionos.es/digitalguide/online-marketing/vender-en-internet/habilitar-las-macros-de-excel/", "https://www.ionos.es/digitalguide/online-marketing/vender-en-internet/habilitar-las-macros-de-excel/", "https://support.microsoft.com/es-es/office/compartir-y-colaborar-con-excel-para-la-web-c8ab30a3-c0fa-473e-b508-0f5186bd47a2", "https://es.repairmsexcel.com/blog/excel-co-autoria-vs-libro-de-trabajo-compartido", "https://www.solvetic.com/tutoriales/article/7328-como-compartir-un-archivo-excel-2019/", "https://excel.facilparami.com/introduccion-a-vba-visual-basic-for-applications", "https://indexingdata.com/blog/excel/vba-excel/", "https://www.excel-avanzado.com/28679/quitar-espacios-en-blanco-en-vba.html"]

for i in urls:
    beautiful_title(i)
    time.sleep(2)
