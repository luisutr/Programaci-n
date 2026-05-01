
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
diasmeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def recorremesesdias(meses,diasmeses):
	for i in range(len(meses)):
		print(meses[i] +" "+ str(i+1)+ " "+ str(diasmeses[i]))


#recorremesesdias(meses, diasmeses)


kilos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def minimo(lista):
	minimo = 99
	for peso in kilos:
		if peso < minimo:
			minimo=peso
	return minimo
#print(minimo(kilos))


frutas = ["manzanas", "peras","freasa", "mandarinas"]
kilos = [20, 15, 19, 21]

def menoskilos(frutas, kilos):
	min = 9999
	minfruta = ""
	for i in range(len(frutas)):
		if min>kilos[i]:
			min = kilos[i]
			minfruta = frutas[i]
	return minfruta
#print(menoskilos(frutas,kilos))


nombres = ["Luis", "Pedro", "jose"]
edades = [40,30,29]

def masmenosjoven(nombres,edades):
	min = 99
	max = 0
	masjoven=""
	menosjovenn=""
	for i in range(len(nombres)):
		if edades[i]<min:
			min = edades[i]
			masjoven=nombres[i]
		if edades[i]>max:
			max = edades[i]
			menosjovenn = nombres[i]
	return "El mas joven es "+ masjoven + " y el menos joven es "+menosjovenn
#print(masmenosjoven(nombres,edades))


def velocidad():
	tiempo = int(input("dame tiempo: "))
	espacio = int(input("dame espacio: "))
	return espacio/tiempo

#print(velocidad())

# Import math Library
import math

# Print the value of pi
print (math.pi)