# _*_ coding: utf_8 _*_

import requests
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def Principal():
    municipios = {'28': 'Madrid', '48': 'Bizkaia', '43': 'Tarragona', '34': 'Palencia', '24': 'Leon',
                  '25': 'Lleida', '26': 'La Rioja', '27': 'Lugo', '20': 'Gipuzkoa', '21': 'Huelva', '22': 'Huesca',
                  '49': 'Zamora', '46': 'Valencia', '47': 'Valladolid', '44': 'Teruel', '45': 'Toledo',
                  '42': 'Soria', '29': 'Malaga', '40': 'Segovia', '41': 'Sevilla', '1': 'Alava',
                  '3': 'Alacant/Alicante', '2': 'Albacete', '5': 'Avila', '4': 'Almeria',
                  '7': 'Illes Balears', '6': 'Badajoz', '9': 'Burgos', '8': 'Barcelona', '10': 'Caceres',
                  '39': 'Cantabria', '12': 'Castellon', '14': 'Cordoba',
                  '11': 'Cadiz', '51': 'Ceuta', '13': 'Ciudad Real', '38': 'Santa Cruz de Tenerife',
                  '15': 'A Coruna', '23': 'Jaen', '17': 'Girona', '16': 'Cuenca', '19': 'Guadalajara',
                  '32': 'Ourense', '31': 'Navarra', '30': 'Murcia', '37': 'Salamanca', '36': 'Pontevedra',
                  '35': 'Las Palmas', '52': 'Melilla', '33': 'Asturias', '18': 'Granada'}
    contador = 0
    listaxml = []
    print "\n\t\t\tTrabajo en Grupo: Procesamiento de datos meteorológicos en XML"
    print " -------------------------------------------------------------------------------------------------"
    print "| (1)Seleccione codigo  para encontrar el  municipio de la provincia que mayor temperatura        |"
    print "| absoluta va a tener en los próximos días, cuál será esta temperatura y en qué día se producirá. |"
    print "|                                                                                                 |"
    print "| (2)Se mostrara una gráfica de sensación térmica máxima y mínima para este municipio incluyendo  |"
    print "| además todos los valores disponibles (datos para las 6, 12, 18 y 24 del próximo día).           |"
    print " -------------------------------------------------------------------------------------------------\n"
    for i in municipios:
        contador += 1
        print i,
        print " ",
        print municipios[i],
        print"\t",
        if (contador == 11):
            contador = 0
            print "\n"

    codigo_numerico = raw_input('\nElige un digito entre 0-52 para elegir su comunidad:')
    principio = (int(codigo_numerico) * 1000)
    final = principio + 2

    for i in range(principio, final):
        if len(str(i)) < 5:
            x = "0" + str(i)
            listaxml.append("http://www.aemet.es/xml/municipios/localidad_" + x + ".xml")
        else:
            listaxml.append("http://www.aemet.es/xml/municipios/localidad_" + str(i) + ".xml")
    return listaxml

def MunicipiosXML ():
    diccionario = {}
    dicctemmun = {}
    diccxml = {}
    listaxml = Principal()
    for i in listaxml:
        r = requests.get(i)
        if r.status_code == 200:
            xml = r.text.encode('utf_8')
            root = ET.fromstring(xml)
            localidad = root.find('nombre').text
            for dia in root.iter('dia'):
                fecha = str(format(dia.get('fecha')))
                t= dia.find('temperatura')
                tmax = t.find('maxima').text
                tmin = t.find('minima').text
                tempabs = int(format(tmin))+int(format(tmax))/2
                dicctemmun[fecha]=tempabs
            diccionario[localidad]=dicctemmun
            diccxml[localidad] = i
    return diccionario, diccxml


def ObtenerTempMax():
    auxdicc, diccxml = MunicipiosXML()
    auxtemp = 0
    auxfecha = ''
    auxmuni = []
    temp = 0
    diatem = {}
    for j in auxdicc:
        muni = auxdicc[j]
        for dia in muni:
            if muni[dia] > temp:
                temp = muni[dia]
                fecha = dia
                diatem['fecha'] = fecha
                diatem['temperatura'] = temp
                # *** Tener en cuenta que puede haber misma temperatura en varios dias.
        if diatem['temperatura'] > auxtemp:
            auxtemp = diatem['temperatura']
            auxfecha = diatem['fecha']
    #Si hay mas de un pueblo, lo guardo en un diccionario
    for j in auxdicc:
        if diatem['temperatura'] == auxtemp:
            auxmuni.append(j)
    print auxmuni
    print auxtemp
    print auxfecha

    return auxmuni, diccxml


def ObtenerSensaMax(munixml):
    r = requests.get(munixml)
    xml = r.text.encode('utf_8')
    root = ET.fromstring(xml)
    diccsenmax = {}
    diccsenmin = {}
    listseis = []
    listdoce = []
    listdiezyocho = []
    listveinticuatro = []
    for dia in root.iter('dia'):
        fecha = str(format(dia.get('fecha')))
        t = dia.find('sens_termica')
        tmax = str(format(t.find('maxima').text))
        tmin = str(format(t.find('minima').text))
        for sensa in t.findall('dato'):
            hora = sensa.get('hora')
            if hora == '06':
                listseis.append(sensa.text)
            if hora == '12':
                listdoce.append(sensa.text)
            if hora == '18':
                listdiezyocho.append(sensa.text)
            if hora == '24':
                listveinticuatro.append(sensa.text)
        diccsenmax[fecha] = tmax
        diccsenmin[fecha] = tmin
    return diccsenmin, diccsenmax, listseis, listdoce, listdiezyocho, listveinticuatro

def hacergrafica():
    muni, diccxml = ObtenerTempMax()
    smax=[]
    smin=[]
    fechas=[]
    diccsenmin, diccsenmax, s06, s12, s18, s24 = ObtenerSensaMax(diccxml[muni[0]])
    for j in diccsenmin.keys():
        fechas.append(j)
    #lista con sensaciones minimas
    for i in diccsenmax:
        smin.append(diccsenmax[i])
    #lista con sensaciones maximas
    for k in diccsenmin:
        smax.append(diccsenmin[k])

    plt.title(u'Sensación Termica en Municipio Max y Min', fontsize='x-large')
    plt.xlabel('dia')
    plt.ylabel(u'sensación (ºC)')
    plt.xticks(range(7),fechas)

    plt.plot(smax, 'ro--', label=u'máxima')
    plt.plot(smin, 'bo--', label=u'mínima')
    leyenda = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.show()
    plt.savefig('plot.pdf')


    plt.title(u'Sensación Termica en Municipio Horas', fontsize='x-large')
    plt.xlabel('dia')
    plt.ylabel(u'sensación (ºC)')
    plt.xticks(range(7),fechas)

    plt.plot(s06, 'ro--', label=u'06')
    plt.plot(s12, 'bo--', label=u'12')
    plt.plot(s18, 'ro--', label=u'18')
    plt.plot(s24, 'bo--', label=u'24')
    leyenda = plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.show()
    plt.savefig('plot2.pdf')


hacergrafica()
