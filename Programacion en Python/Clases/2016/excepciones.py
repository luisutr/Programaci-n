__author__ = 'luisutrilla'

def division(a, b):
    #variables deben estar definidas
    z=0
    try:
        z = a / b
        return z
    except ZeroDivisionError:
        print "Division por cero"


print division(1, 0)

def listas():
    lista1=['juan','ana','carlos']
    try:
        print lista1[5]
    except IndexError:
        print 'Intenta acceder a un elemento no existente a la lista'

listas()

def creartxt():
    try:
        archi=open('datos.txt','w')
        archi.close()
    except IOError:
        print 'No se pudo crear el archivo'

def leertxt():
    try:
       archi=open('noexiste.txt','r')
       linea=archi.readline()
       while linea!="":
           print linea
           linea=archi.readline()
       archi.close()
    except IOError:
        print 'El archivo no existe'


def frutas():
    frutas={'naranjas':1.5,'manzanas':2.3,'peras':1.5}
    try:
        print frutas['sandias']
    except KeyError:
        print 'No existe dicha fruta'


#raise
#muestra el codigo de error que da el interprete pero con el mensaje modificado
def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        raise ZeroDivisionError("El divisor no puede ser cero")

dividir(1,0)