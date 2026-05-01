# _*_ coding: utf_8 _*_

import requests
import xml.etree.ElementTree as ET
import random
import matplotlib.pyplot as plt

def formarxmls():
    municipios = ['abengibre','alatoz','albacete','yeste']
    #municipios = ['abengibre','alatoz','albacete','albatana','alborea','alcadozo','alcala_del_jucar','alcaraz','almansa','alpera','ayna','balazote','ballestero_el','balsa_de_ves','barrax','bienservida','bogarra','bonete','bonillo_el','carcelen','casas_de_juan_nunez','casas_de_lazaro','casas_de_ves','casas_ibanez','caudete','cenizate','chinchilla_de_monte_aragon','corral_rubio','cotillas','elche_de_la_sierra','ferez','fuensanta','fuente_alamo','fuentealbilla','gineta_la','golosalvo','hellin','herrera_la','higueruela','hoya_gonzalo','jorquera','letur','lezuza','lietor','madrigueras','mahora','masegoso','minaya','molinicos','montalvos','montealegre_del_castillo','motilleja','munera','navas_de_jorquera','nerpio','ontur','ossa_de_montiel','paterna_del_madera','penascosa','penas_de_san_pedro','petrola','povedilla','pozo_canada','pozohondo','pozo_lorente','pozuelo','recueja_la','riopar','robledo','roda_la','salobre','san_pedro','socovos','tarazona_de_la_mancha','tobarra','valdeganga','vianos','villa_de_ves','villalgordo_del_jucar','villamalea','villapalacios','villarrobledo','villatoya','villavaliente','villaverde_de_guadalimar','viveros','yeste']
    diccmunxml={}
    for i in municipios:
        diccmunxml[i]=municipio(i)
    return diccmunxml

def obtenertemperaturasmun(munixml):
    r = requests.get(munixml)
    xml = r.text.encode('utf_8')
    root = ET.fromstring(xml)
    dicctemmun={}
    for dia in root.iter('dia'):
        fecha = str(format(dia.get('fecha')))
        t= dia.find('temperatura')
        tmax = t.find('maxima').text
        tmin = t.find('minima').text
        tempabs = int(format(tmin))+int(format(tmax))/2
        dicctemmun[fecha]=tempabs
    return dicctemmun

def tempabsmax():
    diccmunxml = formarxmls()
    auxdicc={}
    for i in diccmunxml:
        if i=="abengibre":
            abengibre=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['abengibre']=abengibre
        if i=="alatoz":
            alatoz=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['alatoz']=alatoz
        if i=="albacete":
            albacete=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['albacete']=albacete
        if i=="albatana":
            albatana=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['albatana']=albatana
        if i=="alborea":
            alborea=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['alborea']=alborea
        if i=="alcadozo":
            alcadozo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['alcadozo']=alcadozo
        if i=="alcala_del_jucar":
            alcala_del_jucar=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['alcala_del_jucar']=alcala_del_jucar
        if i=="alcaraz":
            alcaraz=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['alcaraz']=alcaraz
        if i=="almansa":
            almansa=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['almansa']=almansa
        if i=="alpera":
            alpera=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['alpera']=alpera
        if i=="ayna":
            ayna=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['ayna']=ayna
        if i=="balazote":
            balazote=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['balazote']=balazote
        if i=="ballestero_el":
            ballestero_el=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['ballestero_el']=ballestero_el
        if i=="balsa_de_ves":
            balsa_de_ves=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['balsa_de_ves']=balsa_de_ves
        if i=="barrax":
            barrax=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['barrax']=barrax
        if i=="bienservida":
            bienservida=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['bienservida']=bienservida
        if i=="bogarra":
            bogarra=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['bogarra']=bogarra
        if i=="bonete":
            bonete=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['bonete']=bonete
        if i=="bonillo_el":
            bonillo_el=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['bonillo_el']=bonillo_el
        if i=="carcelen":
            carcelen=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['carcelen']=carcelen
        if i=="casas_de_juan_nunez":
            casas_de_juan_nunez=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['casas_de_juan_nunez']=casas_de_juan_nunez
        if i=="casas_de_lazaro":
            casas_de_lazaro=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['casas_de_lazaro']=casas_de_lazaro
        if i=="casas_de_ves":
            casas_de_ves=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['casas_de_ves']=casas_de_ves
        if i=="casas_ibanez":
            casas_ibanez=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['casas_ibanez']=casas_ibanez
        if i=="caudete":
            caudete=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['caudete']=caudete
        if i=="cenizate":
            cenizate=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['cenizate']=cenizate
        if i=="chinchilla_de_monte_aragon":
            chinchilla_de_monte_aragon=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['chinchilla_de_monte_aragon']=chinchilla_de_monte_aragon
        if i=="corral_rubio":
            corral_rubio=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['corral_rubio']=corral_rubio
        if i=="cotillas":
            cotillas=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['cotillas']=cotillas
        if i=="elche_de_la_sierra":
            elche_de_la_sierra=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['elche_de_la_sierra']=elche_de_la_sierra
        if i=="ferez":
            ferez=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['ferez']=ferez
        if i=="fuensanta":
            fuensanta=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['fuensanta']=fuensanta
        if i=="fuente_alamo":
            fuente_alamo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['fuente_alamo']=fuente_alamo
        if i=="fuentealbilla":
            fuentealbilla=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['fuentealbilla']=fuentealbilla
        if i=="gineta_la":
            gineta_la=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['gineta_la']=gineta_la
        if i=="golosalvo":
            golosalvo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['golosalvo']=golosalvo
        if i=="hellin":
            hellin=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['hellin']=hellin
        if i=="herrera_la":
            herrera_la=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['herrera_la']=herrera_la
        if i=="higueruela":
            higueruela=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['higueruela']=higueruela
        if i=="hoya_gonzalo":
            hoya_gonzalo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['hoya_gonzalo']=hoya_gonzalo
        if i=="jorquera":
            jorquera=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['jorquera']=jorquera
        if i=="letur":
            letur=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['letur']=letur
        if i=="lezuza":
            lezuza=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['lezuza']=lezuza
        if i=="lietor":
            lietor=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['lietor']=lietor
        if i=="madrigueras":
            madrigueras=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['madrigueras']=madrigueras
        if i=="mahora":
            mahora=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['mahora']=mahora
        if i=="masegoso":
            masegoso=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['masegoso']=masegoso
        if i=="minaya":
            minaya=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['minaya']=minaya
        if i=="molinicos":
            molinicos=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['molinicos']=molinicos
        if i=="montalvos":
            montalvos=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['montalvos']=montalvos
        if i=="montealegre_del_castillo":
            montealegre_del_castillo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['montealegre_del_castillo']=montealegre_del_castillo
        if i=="motilleja":
            motilleja=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['motilleja']=motilleja
        if i=="munera":
            munera=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['munera']=munera
        if i=="navas_de_jorquera":
            navas_de_jorquera=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['navas_de_jorquera']=navas_de_jorquera
        if i=="nerpio":
            nerpio=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['nerpio']=nerpio
        if i=="ontur":
            ontur=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['ontur']=ontur
        if i=="ossa_de_montiel":
            ossa_de_montiel=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['ossa_de_montiel']=ossa_de_montiel
        if i=="paterna_del_madera":
            paterna_del_madera=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['paterna_del_madera']=paterna_del_madera
        if i=="penascosa":
            penascosa=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['penascosa']=penascosa
        if i=="penas_de_san_pedro":
            penas_de_san_pedro=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['penas_de_san_pedro']=penas_de_san_pedro
        if i=="petrola":
            petrola=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['petrola']=petrola
        if i=="povedilla":
            povedilla=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['povedilla']=povedilla
        if i=="pozo_canada":
            pozo_canada=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['pozo_canada']=pozo_canada
        if i=="pozohondo":
            pozohondo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['pozohondo']=pozohondo
        if i=="pozo_lorente":
            pozo_lorente=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['pozo_lorente']=pozo_lorente
        if i=="pozuelo":
            pozuelo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['pozuelo']=pozuelo
        if i=="recueja_la":
            recueja_la=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['recueja_la']=recueja_la
        if i=="riopar":
            riopar=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['riopar']=riopar
        if i=="robledo":
            robledo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['robledo']=robledo
        if i=="roda_la":
            roda_la=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['roda_la']=roda_la
        if i=="salobre":
            salobre=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['salobre']=salobre
        if i=="san_pedro":
            san_pedro=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['san_pedro']=san_pedro
        if i=="socovos":
            socovos=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['socovos']=socovos
        if i=="tarazona_de_la_mancha":
            tarazona_de_la_mancha=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['tarazona_de_la_mancha']=tarazona_de_la_mancha
        if i=="tobarra":
            tobarra=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['tobarra']=tobarra
        if i=="valdeganga":
            valdeganga=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['valdeganga']=valdeganga
        if i=="vianos":
            vianos=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['vianos']=vianos
        if i=="villa_de_ves":
            villa_de_ves=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villa_de_ves']=villa_de_ves
        if i=="villalgordo_del_jucar":
            villalgordo_del_jucar=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villalgordo_del_jucar']=villalgordo_del_jucar
        if i=="villamalea":
            villamalea=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villamalea']=villamalea
        if i=="villapalacios":
            villapalacios=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villapalacios']=villapalacios
        if i=="villarrobledo":
            villarrobledo=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villarrobledo']=villarrobledo
        if i=="villatoya":
            villatoya=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villatoya']=villatoya
        if i=="villavaliente":
            villavaliente=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villavaliente']=villavaliente
        if i=="villaverde_de_guadalimar":
            villaverde_de_guadalimar=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['villaverde_de_guadalimar']=villaverde_de_guadalimar
        if i=="viveros":
            viveros=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['viveros']=viveros
        if i=="yeste":
            yeste=obtenertemperaturasmun(diccmunxml[i])
            auxdicc['yeste']=yeste
    #Hacer un bucle con los municipios que llame a encontrarmayor(municipio) que coteje las mayores temperaturas
    # y gurde a que municipio pertenece
    auxtemp=0
    auxfecha=''
    auxmuni=[]
    for j in auxdicc:
        dicc = encontrarmayor(auxdicc[j])
        if dicc['temperatura'] > auxtemp:
            auxtemp = dicc['temperatura']
            auxfecha = dicc['fecha']
    for j in auxdicc:
        dicc = encontrarmayor(auxdicc[j])
        if dicc['temperatura'] == auxtemp:
            auxmuni.append(j)
    print auxmuni
    print auxtemp
    print auxfecha

    return auxmuni


def encontrarmayor(muni):
    aux=''
    temaux=0
    diatem={}
    for dia in muni:
        if muni[dia] > temaux:
            temaux = muni[dia]
            aux = dia
    diatem['fecha'] = aux
    diatem['temperatura'] = temaux
    # *** Tener en cuenta que puede haber misma temperatura en varios dias.
    return diatem


def municipio(m):
    return {
        'abengibre':'http://www.aemet.es/xml/municipios/localidad_02001.xml',
        'alatoz':'http://www.aemet.es/xml/municipios/localidad_02002.xml',
        'albacete':'http://www.aemet.es/xml/municipios/localidad_02003.xml',
        ''''albatana':'http://www.aemet.es/xml/municipios/localidad_02004.xml',
        'alborea':'http://www.aemet.es/xml/municipios/localidad_02005.xml',
        'alcadozo':'http://www.aemet.es/xml/municipios/localidad_02006.xml',
        'alcala_del_jucar':'http://www.aemet.es/xml/municipios/localidad_02007.xml',
        'alcaraz':'http://www.aemet.es/xml/municipios/localidad_02008.xml',
        'almansa':'http://www.aemet.es/xml/municipios/localidad_02009.xml',
        'alpera':'http://www.aemet.es/xml/municipios/localidad_02010.xml',
        'ayna':'http://www.aemet.es/xml/municipios/localidad_02011.xml',
        'balazote':'http://www.aemet.es/xml/municipios/localidad_02012.xml',
        'ballestero_el':'http://www.aemet.es/xml/municipios/localidad_02014.xml',
        'balsa_de_ves':'http://www.aemet.es/xml/municipios/localidad_02013.xml',
        'barrax':'http://www.aemet.es/xml/municipios/localidad_02015.xml',
        'bienservida':'http://www.aemet.es/xml/municipios/localidad_02016.xml',
        'bogarra':'http://www.aemet.es/xml/municipios/localidad_02017.xml',
        'bonete':'http://www.aemet.es/xml/municipios/localidad_02018.xml',
        'bonillo_el':'http://www.aemet.es/xml/municipios/localidad_02019.xml',
        'carcelen':'http://www.aemet.es/xml/municipios/localidad_02020.xml',
        'casas_de_juan_nunez':'http://www.aemet.es/xml/municipios/localidad_02021.xml',
        'casas_de_lazaro':'http://www.aemet.es/xml/municipios/localidad_02022.xml',
        'casas_de_ves':'http://www.aemet.es/xml/municipios/localidad_02023.xml',
        'casas_ibanez':'http://www.aemet.es/xml/municipios/localidad_02024.xml',
        'caudete':'http://www.aemet.es/xml/municipios/localidad_02025.xml',
        'cenizate':'http://www.aemet.es/xml/municipios/localidad_02026.xml',
        'chinchilla_de_monte_aragon':'http://www.aemet.es/xml/municipios/localidad_02029.xml',
        'corral_rubio':'http://www.aemet.es/xml/municipios/localidad_02027.xml',
        'cotillas':'http://www.aemet.es/xml/municipios/localidad_02028.xml',
        'elche_de_la_sierra':'http://www.aemet.es/xml/municipios/localidad_02030.xml',
        'ferez':'http://www.aemet.es/xml/municipios/localidad_02031.xml',
        'fuensanta':'http://www.aemet.es/xml/municipios/localidad_02032.xml',
        'fuente_alamo':'http://www.aemet.es/xml/municipios/localidad_02033.xml',
        'fuentealbilla':'http://www.aemet.es/xml/municipios/localidad_02034.xml',
        'gineta_la':'http://www.aemet.es/xml/municipios/localidad_02035.xml',
        'golosalvo':'http://www.aemet.es/xml/municipios/localidad_02036.xml',
        'hellin':'http://www.aemet.es/xml/municipios/localidad_02037.xml',
        'herrera_la':'http://www.aemet.es/xml/municipios/localidad_02038.xml',
        'higueruela':'http://www.aemet.es/xml/municipios/localidad_02039.xml',
        'hoya_gonzalo':'http://www.aemet.es/xml/municipios/localidad_02040.xml',
        'jorquera':'http://www.aemet.es/xml/municipios/localidad_02041.xml',
        'letur':'http://www.aemet.es/xml/municipios/localidad_02042.xml',
        'lezuza':'http://www.aemet.es/xml/municipios/localidad_02043.xml',
        'lietor':'http://www.aemet.es/xml/municipios/localidad_02044.xml',
        'madrigueras':'http://www.aemet.es/xml/municipios/localidad_02045.xml',
        'mahora':'http://www.aemet.es/xml/municipios/localidad_02046.xml',
        'masegoso':'http://www.aemet.es/xml/municipios/localidad_02047.xml',
        'minaya':'http://www.aemet.es/xml/municipios/localidad_02048.xml',
        'molinicos':'http://www.aemet.es/xml/municipios/localidad_02049.xml',
        'montalvos':'http://www.aemet.es/xml/municipios/localidad_02050.xml',
        'montealegre_del_castillo':'http://www.aemet.es/xml/municipios/localidad_02051.xml',
        'motilleja':'http://www.aemet.es/xml/municipios/localidad_02052.xml',
        'munera':'http://www.aemet.es/xml/municipios/localidad_02053.xml',
        'navas_de_jorquera':'http://www.aemet.es/xml/municipios/localidad_02054.xml',
        'nerpio':'http://www.aemet.es/xml/municipios/localidad_02055.xml',
        'ontur':'http://www.aemet.es/xml/municipios/localidad_02056.xml',
        'ossa_de_montiel':'http://www.aemet.es/xml/municipios/localidad_02057.xml',
        'paterna_del_madera':'http://www.aemet.es/xml/municipios/localidad_02058.xml',
        'penascosa':'http://www.aemet.es/xml/municipios/localidad_02059.xml',
        'penas_de_san_pedro':'http://www.aemet.es/xml/municipios/localidad_02060.xml',
        'petrola':'http://www.aemet.es/xml/municipios/localidad_02061.xml',
        'povedilla':'http://www.aemet.es/xml/municipios/localidad_02062.xml',
        'pozo_canada':'http://www.aemet.es/xml/municipios/localidad_02901.xml',
        'pozohondo':'http://www.aemet.es/xml/municipios/localidad_02063.xml',
        'pozo_lorente':'http://www.aemet.es/xml/municipios/localidad_02064.xml',
        'pozuelo':'http://www.aemet.es/xml/municipios/localidad_02065.xml',
        'recueja_la':'http://www.aemet.es/xml/municipios/localidad_02066.xml',
        'riopar':'http://www.aemet.es/xml/municipios/localidad_02067.xml',
        'robledo':'http://www.aemet.es/xml/municipios/localidad_02068.xml',
        'roda_la':'http://www.aemet.es/xml/municipios/localidad_02069.xml',
        'salobre':'http://www.aemet.es/xml/municipios/localidad_02070.xml',
        'san_pedro':'http://www.aemet.es/xml/municipios/localidad_02071.xml',
        'socovos':'http://www.aemet.es/xml/municipios/localidad_02072.xml',
        'tarazona_de_la_mancha':'http://www.aemet.es/xml/municipios/localidad_02073.xml',
        'tobarra':'http://www.aemet.es/xml/municipios/localidad_02074.xml',
        'valdeganga':'http://www.aemet.es/xml/municipios/localidad_02075.xml',
        'vianos':'http://www.aemet.es/xml/municipios/localidad_02076.xml',
        'villa_de_ves':'http://www.aemet.es/xml/municipios/localidad_02077.xml',
        'villalgordo_del_jucar':'http://www.aemet.es/xml/municipios/localidad_02078.xml',
        'villamalea':'http://www.aemet.es/xml/municipios/localidad_02079.xml',
        'villapalacios':'http://www.aemet.es/xml/municipios/localidad_02080.xml',
        'villarrobledo':'http://www.aemet.es/xml/municipios/localidad_02081.xml',
        'villatoya':'http://www.aemet.es/xml/municipios/localidad_02082.xml',
        'villavaliente':'http://www.aemet.es/xml/municipios/localidad_02083.xml',
        'villaverde_de_guadalimar':'http://www.aemet.es/xml/municipios/localidad_02084.xml','''
        'viveros':'http://www.aemet.es/xml/municipios/localidad_02085.xml',
        'yeste':'http://www.aemet.es/xml/municipios/localidad_02086.xml'

        }[m]

def obtenersensacionmun(munixml):
    r = requests.get(munixml)
    xml = r.text.encode('utf_8')
    root = ET.fromstring(xml)
    diccsenmax={}
    diccsenmin={}
    diccseis={}
    diccdoce={}
    diccdiezyocho={}
    diccveinticuatro={}
    for dia in root.iter('dia'):
        fecha = str(format(dia.get('fecha')))
        t= dia.find('sens_termica')
        tmax = str(format(t.find('maxima').text))
        tmin = str(format(t.find('minima').text))
        for name in dia.iter('dato'):
            hora = name.get('hora')
            print hora
            '''
            if hora == 06:
            seis = hora.find('06')
            doce = hora.find('12')
            dieziocho = hora.find('18')
            veinticuatro = hora.find('24')
            diccseis[fecha]= seis
            diccdoce[fecha]=  doce
            diccdiezyocho[fecha]= dieziocho
            diccveinticuatro[fecha]= veinticuatro'''
        diccsenmax[fecha]= tmax
        diccsenmin[fecha]= tmin
       # print diccseis, diccdoce, diccdiezyocho, diccveinticuatro
    return diccsenmin, diccsenmax, diccseis, diccdoce, diccdiezyocho, diccveinticuatro

def hacergrafica():
    muni = tempabsmax()
    diccmunxml = formarxmls()
    smax=[]
    smin=[]
    fechas=[]
    s06=[]
    s12=[]
    s18=[]
    s24=[]
    diccsenmin, diccsenmax, diccseis, diccdoce, diccdiezyocho, diccveinticuatro = obtenersensacionmun(diccmunxml[muni[0]])
    #Ya tengo las max y las minimas, hago lo mismo para las horas y tengo todos los diccionarios
    #Divido los diccionarios en listas de fechas y sensaciones termincas.
    #obtengo lista con fechas
    for j in diccsenmin.keys():
        fechas.append(j)
    #lista con sensaciones minimas
    for i in diccsenmax:
        smin.append(diccsenmax[i])
    #lista con sensaciones maximas
    for k in diccsenmin:
        smax.append(diccsenmin[k])
    #lista con sensaciones 06
    for seis in diccseis:
        s06.append(diccseis[seis])
    #lista con sensaciones 12
    for doce in diccdoce:
        s12.append(diccdoce[doce])
    #lista con sensaciones 18
    for diezyocho in diccdiezyocho:
        s18.append(diccdiezyocho[diezyocho])
    #lista con sensaciones 24
    for veinticuatro in diccveinticuatro:
        s24.append(diccveinticuatro[veinticuatro])

    '''plt.title(u'Sensación Termica en Municipio Max y Min', fontsize='x-large')
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
    plt.savefig('plot2.pdf')'''

hacergrafica()

