# _*_ coding: utf_8 _*_

import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

municipios = {'28': 'Madrid', '48': 'Bizkaia', '43': 'Tarragona', '34': 'Palencia', '24': 'Leon',
              '25': 'Lleida', '26': 'La Rioja', '27': 'Lugo', '20': 'Gipuzkoa', '21': 'Huelva', '22': 'Huesca',
              '49': 'Zamora', '46': 'Valencia', '47': 'Valladolid', '44': 'Teruel', '45': 'Toledo',
              '42': 'Soria', '29': 'Malaga', '40': 'Segovia', '41': 'Sevilla', '1': 'Alava',
              '3': 'Alicante', '2': 'Albacete', '5': 'Avila', '4': 'Almeria',
              '7': 'Illes Balears', '6': 'Badajoz', '9': 'Burgos', '8': 'Barcelona', '10': 'Caceres',
              '39': 'Cantabria', '12': 'Castellon', '14': 'Cordoba',
              '11': 'Cadiz', '51': 'Ceuta', '13': 'Ciudad Real', '38': 'Santa Cruz de Tenerife',
              '15': 'A Coruna', '23': 'Jaen', '17': 'Girona', '16': 'Cuenca', '19': 'Guadalajara',
              '32': 'Ourense', '31': 'Navarra', '30': 'Murcia', '37': 'Salamanca', '36': 'Pontevedra',
              '35': 'Las Palmas', '52': 'Melilla', '33': 'Asturias', '18': 'Granada'}


def formarxml():
    urllist = []
    print municipios
    codmun = input('\nSeleccione provincia: ')
    print "Ha seleccionado: "+str(municipios[str(codmun)])
    x = codmun * 1000
    y = x + 2
    for i in range(x, y):
        if len(str(i)) < 5:
            i = "0" + str(i)
            urllist.append("http://www.aemet.es/xml/municipios/localidad_" + i + ".xml")
        else:
            urllist.append("http://www.aemet.es/xml/municipios/localidad_" + str(i) + ".xml")
    return urllist


def xml():
    diccionario = {}
    dicctemmun = {}
    diccxml = {}
    urllist = formarxml()
    for i in urllist:
        r = requests.get(i)
        if r.status_code != 404:
            xml = r.text.encode('utf_8')
            root = ET.fromstring(xml)
            localidad = root.find('nombre').text
            for dia in root.iter('dia'):
                fecha = str(format(dia.get('fecha')))
                t = dia.find('temperatura')
                maxima = t.find('maxima').text
                minima = t.find('minima').text
                absoluta = int(format(minima)) + int(format(maxima)) / 2
                dicctemmun[fecha] = absoluta
            diccionario[localidad] = dicctemmun
            diccxml[localidad] = i
    return diccionario, diccxml


def tempabsmax():
    diccaux, diccxml = xml()
    temperatura = 0
    fecha = ''
    municipio = []
    for j in diccaux:
        dicc = fecha_temperatura(diccaux[j])
        if dicc['temperatura'] > temperatura:
            temperatura = dicc['temperatura']
            fecha = dicc['fecha']
    for j in diccaux:
        dicc = fecha_temperatura(diccaux[j])
        if dicc['temperatura'] == temperatura:
            municipio.append(j)
    print "La temperatura mas alta es de: "+str(temperatura)+",el dia: "+str(fecha)+" , en el municipio de: ",
    for k in municipio:
        print k+" ",

    return municipio, diccxml


def fecha_temperatura(muni):
    valor = ''
    temperatura = 0
    fecha = {}
    for dia in muni:
        if muni[dia] > temperatura:
            temperatura = muni[dia]
            valor = dia
    fecha['fecha'] = valor
    fecha['temperatura'] = temperatura
    return fecha


def obtenersensacionmun(munixml):
    r = requests.get(munixml)
    xml = r.text.encode('utf_8')
    root = ET.fromstring(xml)
    diccsenmax = {}
    diccsenmin = {}
    listseis = []
    listdoce = []
    listdieciocho = []
    listveinticuatro = []
    for dia in root.iter('dia'):
        fecha = str(format(dia.get('fecha')))
        t = dia.find('sens_termica')
        maxima = str(format(t.find('maxima').text))
        minima = str(format(t.find('minima').text))
        for sensa in t.findall('dato'):
            hora = sensa.get('hora')
            if hora == '06':
                listseis.append(sensa.text)
            if hora == '12':
                listdoce.append(sensa.text)
            if hora == '18':
                listdieciocho.append(sensa.text)
            if hora == '24':
                listveinticuatro.append(sensa.text)
        diccsenmax[fecha] = maxima
        diccsenmin[fecha] = minima
    return diccsenmin, diccsenmax, listseis, listdoce, listdieciocho, listveinticuatro


def Trabajo_Grupo():
    muni, diccxml = tempabsmax()
    maxima=[]
    minima=[]
    fechas=[]
    diccsenmin, diccsenmax, seis, doce, dieciocho, vainticuatro = obtenersensacionmun(diccxml[muni[0]])
    for j in diccsenmin.keys():
        fechas.append(j)
    for i in diccsenmax:
        minima.append(diccsenmax[i])
    for k in diccsenmin:
        maxima.append(diccsenmin[k])

    plt.title(u'Sensación Termica en Municipio Max y Min', fontsize='x-large')
    plt.xlabel('dia')
    plt.ylabel(u'sensación (ºC)')
    plt.xticks(range(7), fechas)

    plt.plot(maxima, 'ro--', label=u'máxima')
    plt.plot(minima, 'bo--', label=u'mínima')
    leyenda = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.show()
    plt.savefig('maxmin.pdf')

    plt.title(u'Sensación Termica en Municipio Horas', fontsize='x-large')
    plt.xlabel('dia')
    plt.ylabel(u'sensación (ºC)')
    plt.xticks(range(7), fechas)

    plt.plot(seis, 'ro--', label=u'06')
    plt.plot(doce, 'bo--', label=u'12')
    plt.plot(dieciocho, 'ro--', label=u'18')
    plt.plot(vainticuatro, 'bo--', label=u'24')
    plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.savefig('porhoras.pdf')
    plt.show()


Trabajo_Grupo()
