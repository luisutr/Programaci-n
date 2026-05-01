__author__ = 'luisutrilla'

temp = {
'Vina del Mar': ( 9, 26),
'Valparaiso': (10, 24),
'Quilpue' : ( 7, 30),
'Olmue': ( 5, 29),
'Limache': ( 9, 23),
'Villa Alemana': ( 9, 22),
}

def crear_reporte(fecha, temperaturas):
    anio, mes, dia = fecha
    archivo = open("reporte-"+str(anio)+"-"+str(mes)+"-"+str(dia)+".txt", "w")
    for ciudad, tupla in temperaturas.items():
        minimo, maximo = tupla
        if maximo > 25:
            linea = ciudad.upper()+': max '+str(maximo)+', min '+str(minimo)+"\n"
        else:
            linea = ciudad+': max '+str(maximo)+', min '+str(minimo)+"\n"
        print linea,
        archivo.write(linea)
    archivo.close()

crear_reporte((2011,5,14), temp)