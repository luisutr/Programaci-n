__author__ = 'luisutrilla'


def frequent_browsers(ruta):
    archivo = open(ruta, "r")  # r nos dice que lee el archivo
    lista_accesos = []
    resultado = []
    line = None
    while line != "":
        line = archivo.readline()
        ip = line.rsplit(" ")[0]
        linea = line.split(" ")
        for i in range(len(linea)):
            if i == 11:
                datos = linea[i].split("/")
                lista_accesos.append((ip, datos[0]))
    for j in range(len(lista_accesos)):
        aux_ip = lista_accesos[j][0]
        porcentaje = 0
        for k in range(len(lista_accesos)):
            if aux_ip == lista_accesos[k][0]:
                porcentaje += 1
        if porcentaje > 5:
            resultado.append((lista_accesos[j][1], str(porcentaje)+"%"))
    archivo.close()
    return resultado




print (frequent_browsers("ejemplo_access.log"))