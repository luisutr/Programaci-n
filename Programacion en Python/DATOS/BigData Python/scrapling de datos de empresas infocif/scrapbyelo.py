# Sacar datos de empresas desde infocif.es
# Eloy R. M.- 2019

from bs4 import BeautifulSoup
import urllib2, requests, re


#URLs:
url_base = "http://www.infocif.es/ranking/ventas-empresas/espana?pagina="
		
		

def test(url_base):
	for i in range(1,670):
		URL = url_base+str(i)
		html_page = urllib2.urlopen(URL)
		soup = BeautifulSoup(html_page,"html5lib")
		for l in soup.findAll('a', attrs={'href': re.compile("^http://www.infocif.es/ficha-empresa")}):
			file = open("ListadoURLEmpresas.txt", "a+")
			file.write(l.get('href')+"\n")
			file.close()


def procesarDatos():
	# Imprime el nombre de la empresa + CIF + telefono y luego la URL de la información
	with open("ListadoURLEmpresas.txt") as texto:
		for line in texto:
			datos = []
			num_pat = "\d{9}"
			html_page = urllib2.urlopen(line)
			soup = BeautifulSoup(html_page,"html5lib")
			nombre = soup.find('h1',attrs={'class':"title title-sm title-margin mtnone roboto mbnone"}).text
			for info in soup.findAll('div', attrs={'id':'fe-informacion-izq'}):
				try:
					cif = info.find('h2').text
					print nombre+", CIF: "+cif+", Tlf: ",
					for p_tag in info.findAll('p', attrs={'class':'editable col-md-10 col-sm-9 col-xs-12 mb10 text-right'}):
						numero = re.findall(num_pat,p_tag.text)
						if numero != []:
							print numero[0]
				except:
					pass
				
			print line
			
			
