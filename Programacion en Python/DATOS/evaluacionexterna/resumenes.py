# -*- coding: utf-8 -*-
import pandas as pd
import codecs

dicc_areas = {1:"ADMON ELECTRONICA",2:"ADMON ELECTRONICA",
3:"ADMON ELECTRONICA",
4:"ECNCO-PRESUP",
5:"ECNCO-PRESUP",
6:"ECNCO-PRESUP",
7:"ECNCO-PRESUP",
9:"INNOV Y CREATIVIAD EN LAS ORGANIZACIONES",
10:"ESPECIFICOS DET COLECTIVOS",
11:"ESPECIFICOS DET COLECTIVOS",
12:"ESPECIFICOS DET COLECTIVOS",
13:"ESPECIFICOS DET COLECTIVOS",
14:"ESPECIFICOS DET COLECTIVOS",
15:"ESPECIFICOS DET COLECTIVOS",
16:"ESPECIFICOS DET COLECTIVOS",
17:"ESPECIFICOS DET COLECTIVOS",
18:"ESPECIFICOS DET COLECTIVOS",
20:"ESPECIFICOS DET COLECTIVOS",
21:"ESPECIFICOS DET COLECTIVOS",
22:"ESPECIFICOS DET COLECTIVOS",
23:"ESPECIFICOS DET COLECTIVOS",
24:"ESPECIFICOS DET COLECTIVOS",
25:"ESPECIFICOS DET COLECTIVOS",
26:"ESPECIFICOS DET COLECTIVOS",
27:"ESPECIFICOS DET COLECTIVOS",
28:"ESPECIFICOS DET COLECTIVOS",
29:"ESPECIFICOS DET COLECTIVOS",
30:"ESPECIFICOS DET COLECTIVOS",
31:"IDIOMAS",
32:"IDIOMAS",
33:"INFF Y ATT AL PUB",
34:"JURIDICO PROCEDIMENTAL",
35:"JURIDICO PROCEDIMENTAL",
36:"JURIDICO PROCEDIMENTAL",
38:"JURIDICO PROCEDIMENTAL",
39:"JURIDICO PROCEDIMENTAL",
40:"JURIDICO PROCEDIMENTAL",
41:"JURIDICO PROCEDIMENTAL",
42:"NUEVAS TECNOLOGIAS",
43:"NUEVAS TECNOLOGIAS",
44:"NUEVAS TECNOLOGIAS",
45:"POLITICAS DE IGUALDAD",
46:"POLITICAS DE IGUALDAD",
47:"PREV RIESG LAB. SEG LABORAL",
48:"PREV RIESG LAB. SEG LABORAL",
49:"RECURSOS HUMANOS",
50:"ADMON ELECTRONICA",
51:"URBANISMO Y MEDIO AMBIENTE",
52:"URBANISMO Y MEDIO AMBIENTE",
53:"URBANISMO Y MEDIO AMBIENTE",
54:"URBANISMO Y MEDIO AMBIENTE",
55:"URBANISMO Y MEDIO AMBIENTE",
56:"URBANISMO Y MEDIO AMBIENTE",
57:"DIRECCIÓN Y GERENCIA PUBLICA",
58:"DIRECCIÓN Y GERENCIA PUBLICA",
59:"UNION EUROPEA",
61:"AREA ESPECÍFICOS DETERMINADOS COLECTIVOS.",
62:"AREA ESPECÍFICOS DETERMINADOS COLECTIVOS."}
dic_cursos = {1: "GESTIÓN Y ARCHIVOS DE DOCUMENTOS ELECTRÓNICOS. TRAMITACIÓN ELECTRÓNICA DE EXPEDIENTES", 2: "CONTRATACIÓN PÚBLICA ELECTRÓNICA: LA E-CONTRATACIÓN", 3: "REDES SOCIALES. ESPECIAL ATENCIÓN A LOS SISTEMAS DE PROTECCIÓN DE DATOS", 4: "DESARROLLO Y EJECUCIÓN PRESUPUESTARIA EN LAS ENTIDADES LOCALES", 5: "INVERSIONES FINANCIERAMENTE SOSTENIBLES", 6: "ELABORACIÓN Y APLICACIÓN PRÁCTICA DE LAS BASES DE EJECUCIÓN DEL PRESUPUESTO. MARCO NORMATIVO", 7: "ELABORACIÓN, SEGUIMIENTO Y MODIFICACIÓN DE LOS PLANES ECONÓMICO FINANCIEROS EN LAS EELL", 9: "LIDERAZGO Y HABILIDADES DIRECTIVAS", 10: "URGENCIAS SANITARIAS PARA PRIMEROS INTERVINIENTES", 11: "REANIMACIÓN CARDIO PULMONAR BÁSICA CON DESA", 12: "INTERVENCIÓN EN ACCIDENTES DE TRÁFICO CON CISTERNAS", 13: "BUSQUEDA DE PERSONAS DESAPARECIDAS CON PERROS DE RASTRO", 14: "INTERVENCIÓN CON RIESGO BIOLÓGICO EN SERVICIOS DE EMERGENCIAS", 15: "TALA,  PODA Y ACTUACIONES DE PREVENCIÓN DE RIESGOS CON PLATAFORMA ELEVADORA", 16: "INTERVENCIÓN EN ACCIDENTES DE TRÁFICO   ", 17: "INTERVENCIÓN POLICIAL EN CASOS DE VÍCTIMAS DE DELITOS VIOLENTOS,  DE GÉNERO Y SEXUALES", 18: "INTERVENCIÓN POLICIAL EN CASOS DE RESPONSABILIDAD PENAL DE MENORES", 20: "ACTUACIONES POLICIALES EN MATERIA DE CONTAMINACIÓN ACÚSTICA", 21: "COMUNICACIÓN NO VIOLENTA", 22: "ASERTIVIDAD Y EMPATÍA. CLAVES EN NUESTRAS RELACIONES SOCIALES", 23: "MANEJO DE SITUACIONES DE RIESGO FÍSICO O PSICOLOGICO EN LA ATT A USUARIOS DE SERVICIOS PUBLICOS", 24: "ATENCIÓN A LA CIUDADANÍA ANTE SITUACIONES DE PÁNICO COLECTIVO", 25: "ACTUALIZACIÓN EN INTERVENCIÓN SOCIAL ANTE CASOS DE VIOLENCIA DE GÉNERO Y FAMILIAR", 26: "PREVENCIÓN Y ACTUACIÓN ANTE LAS NUEVAS ADICCIONES ( RRSS,  VIDEO JUEGOS,  JUEGOS DE AZAR…)", 27: "PREVENCIÓN DE LA DELINCUENCIA JUVENIL", 28: "RIESGOS PSICOSOCIALES DERIVADOS DEL TRABAJO CON USUARIOS EN RIESGOS O SITUACIÓN DE EXCLUSIÓN SOCIAL", 29: "INTERVENCIÓN CON FAMILIAS MULTIPROBLEMATICAS EN SITUACIÓN DE EXCLUSION SOCIAL", 30: "TÉCNICAS DE ASESORAMIENTO INNOVADOR PARA EL DESARROLLO DE  ECOSISTEMAS EMPRENDEDORES", 31: "ARABE PARA LA ATENCIÓN AL PÚBLICO. INICIACIÓN", 32: "INGLÉS PARA LA ATENCIÓN AL PÚBLICO – NIVEL B1", 33: "ATENCIÓN ELECTRÓNICA AL CIUDADANO", 34: "LEY 39/2015 DE PROCEDIMIENTO ADMINISTRATIVO LOCAL. ASPECTOS PRÁCTICOS", 35: "LEY 40/2015 DE RÉGIMEN JURÍDICO DEL SECTOR PÚBLICO. ASPECTOS PRÁCTICOS", 36: "CONTRATO DE OBRA,  SERVICIOS Y SUMINISTROS. ASPECTOS PRÁCTICOS DE SU TRAMITACIÓN", 38: "LOS CONTRATOS DE GESTIÓN DE SERVICIOS PÚBLICOS EN LA LEY 9/2017. ASPECTOS PRÁCTICOS", 39: "LA NUEVA LEY ORGÁNICA DE PROTECCIÓN DE DATOS. ESPECIALIDADES Y ASPECTOS PRÁCTICOS DE SU APLICACIÓN", 40: "EL CONTRATO MENOR. TIPOS,  PROCEDIMIENTO,  TRAMITACIÓN Y EJEMPLOS PRÁCTICOS", 41: "PREPARACIÓN DE LOS CONTRATOS Y PROCEDIMIENTOS DE CONTRATACIÓN", 42: "NNTT Y COMMUNITY MANAGER EN EL AMBITO LOCAL", 43: "PAQUETE OFFICE", 44: "OFIMÁTICA Y E-ADMINISTRACIÓN", 45: "VIOLENCIAS DE GÉNERO EN REDES SOCIALES: ACTUACIONES EN MATERIA DE PREVENCIÓN", 46: "MOBBING,  BULLYNG,  ACOSO SEXUAL,  CIBERACOSO: LAS DIFERENTES FORMAS DEL ACOSO Y SU REPERCUSIÓN", 47: "IMPLANTACIÓN DE SISTEMAS DE GESTIÓN DE LA SEGURIDAD Y SALUD EN EL TRABAJO. NORMA ISO 45001", 48: "ELABORACIÓN DE PLANES DE AUTOPROTECCIÓN", 49: "CONTENIDO Y APLICACIÓN PRÁCTICA DE LA RPT Y LA PLANTILLA DE PLAZAS COMO INSTRUMENTOS BÁSICOS DE LA LEGALIDAD Y LA GESTIÓN DE LOS RRHH", 50: "TRANSPARENCIA,  ADMINISTRACIÓN ELECTRÓNICA Y PROTECCIÓN DE DATOS. NOVEDADES TRAS LA LOPD 2018", 51: "ESTRATEGIAS LOCALES CONTRA EL CAMBIO CLIMÁTICO. REDUCCIÓN DE LA HUELLA DE CARBONO A NIVEL LOCAL", 52: "CONTROL DE CALIDAD DE LAS AGUAS", 53: "IMPLEMENTACIÓN DE LA AGENDA URBANA EN LOS MUNICIPIOS", 54: "NUEVA LEY DE EVALUACIÓN AMBIENTAL. 9 /18", 55: "RESPONSABILIDAD Y ACTUACIÓN INSPECTORA DE LAS CCLL EN MATERIA DE INFRACCIONES Y DELITOS MEDIOAMBIENTALES", 56: "IMPLANTACIÓN Y GESTIÓN DE ECOPARQUES Y PUNTOS LIMPIOS", 57: "ANÁLISIS DE PROBLEMAS Y TOMA DE DECISIONES", 58: "ASPECTOS GENERALES DE LA AGENDA 2030 Y ODS", 59: "GESTIÓN DE PROYECTOS EUROPEOS Y BÚSQUEDAS DE SUBVENCIONES", 61: "HERRAMIENTA PARA LA IMPLEMENTACIÓN Y MEJORA DE POLÍTICAS DE INFANCIA", 62: "RECICLAJE PROFESIONAL PARA AUXILIARES DE AYUDA A DOMICILIO"}
salidaonline = codecs.open("resumenonline.csv", "w+")
salidapresencial = codecs.open("resumenpresencial.csv", "w+")
salidaonline.write("cd;nombre;area;profesor;plataforma;duracion ;productividad;metodologia ;practicas ;general"+'\n')
salidapresencial.write("cd;nombre;area;formador;material;duracion;productividad;dinamico;practicas;recomendaria "'\n')
salidapromedioonline = codecs.open("promedioonline.csv", "w+")
salidapromediopresencial = codecs.open("promediopresencial.csv", "w+")
salidapromedioonline.write("profesor;plataforma;duracion ;productividad;metodologia ;practicas ;general"+'\n')
salidapromediopresencial.write("formador;material;duracion;productividad;dinamico;practicas;recomendaria "'\n')
#cd;profesor;material;duracion ;productividad;metodologia ;practicas ;general
def encuesta():
    cuestionaris46 = 0
    cuestionarios14 = 0
    media_edad = 0
    media_informa = 0
    media_orientados = 0
    media_espectativas = 0
    media_mejorara = 0
    media_organizacion = 0
    media_duración = 0
    media_material = 0
    media_plataforma = 0
    media_errores = 0
    media_servicios = 0
    media_metodologia = 0
    media_hipervinculos = 0
    media_temario = 0
    media_presentacion = 0
    media_Practicas = 0
    media_ayudado = 0
    media_profesor = 0
    media_apoyo = 0
    media_seguimientom = 0
    media_foro = 0
    media_seguimientob = 0
    media_aprendido = 0
    media_Plan = 0

    media_informaP = 0
    media_orientadosP = 0
    media_organizacionP = 0
    media_espectativasP = 0
    media_mejoraraP = 0
    media_duraciónP = 0
    media_materialP = 0
    media_plataformaP = 0
    media_erroresP = 0
    media_serviciosP = 0
    media_metodologiaP = 0
    media_temarioP = 0
    media_presentacionP = 0
    with open('./ENCUESTA/myoutput.txt') as f:
        for linea in f:
            # con el nombre del curso voy a la excel con los otros datos y escribo los datos del curso en salida
            codigo = int((linea[-7:-5]).strip())
            nombre = dic_cursos[codigo]
            area = dicc_areas[codigo]
            print(codigo, nombre)
            #Abro el archivo, saco la información de la encuesta y lo voy escribiendo en salida
            df = pd.read_csv("./ENCUESTA/"+linea[:-1], encoding = "ISO-8859-1", sep=';', decimal=',')
            columnas = ["Orden","Pregunta", "Respuesta","Valor"]
            df_seleccionados = df[columnas]
            #cuestionarios de 46 preguntas
            if len(df_seleccionados) == 46:
                cuestionaris46 += 1
                edad = df_seleccionados["Valor"][6]
                media_edad += float(edad)
                #for i in range(13,len(df_seleccionados)):
                #20,21, 41, 42, 43	mejorara mi trabajo
                mejorara = (df_seleccionados["Valor"][18] + df_seleccionados["Valor"][19]+ df_seleccionados["Valor"][39]+ df_seleccionados["Valor"][40]+ df_seleccionados["Valor"][41]) / 5
                media_mejorara += float(mejorara)
                #24	duración
                duración = df_seleccionados["Valor"][22]
                media_duración += float(duración)
                #26	Buen material didactico
                material = df_seleccionados["Valor"][24]
                media_material += float(material)
                # 23	plataforma
                plataforma = df_seleccionados["Valor"][21]
                media_plataforma += float(plataforma)
                #28	metodología correcta
                metodologia = df_seleccionados["Valor"][26]
                media_metodologia += float(metodologia)
                # 31	Practicas
                Practicas = df_seleccionados["Valor"][29]
                media_Practicas += float(Practicas)
                #34	han ayudado las practicas
                ayudado = df_seleccionados["Valor"][32]
                media_ayudado += float(ayudado)
                # 33	profesor preparado
                profesor = df_seleccionados["Valor"][31]
                media_profesor += float(profesor)
                #35,36	apoyo del tutor
                apoyo = (df_seleccionados["Valor"][33] + df_seleccionados["Valor"][34]) / 2
                media_apoyo += float(apoyo)
                #38	seguimiento  bien
                seguimientob = df_seleccionados["Valor"][36]
                media_seguimientob += float(seguimientob)
                # 40	cuanto a aprendido
                aprendido = df_seleccionados["Valor"][38]
                media_aprendido += float(aprendido)
                #44	Plan formativo
                Plan = df_seleccionados["Valor"][42]
                media_Plan += float(Plan)
                #cd;nombre;area;profesor;material;duracion ;productividad;metodologia ;practicas ;general
                salidaonline.write(str(codigo)+";"+str(nombre)+";"+str(area)+";"+str(round(profesor, 2))+";"+str(round(plataforma, 2))+";"+str(round(duración, 2))+";"+str(round(mejorara, 2))+";"+str(round(metodologia, 2))+";"+str(round(Practicas, 2))+";"+str(round(Plan, 2))+'\n')

            if len(df_seleccionados) == 14:
                '''
                               0  La organización del curso ha sido la adecuada, cumplimiento de fechas/horarios, entrega de material.  
                               1  El número de alumnos del grupo ha sido el adecuado para el desarrollo del curso
                               2  Los contenidos del curso se han ajustado a tus expectativas
                               3  Ha habido una combinación adecuada de teoría y práctica
                               4  La duración del curso ha sido adecuada
                               5  El horario ha favorecido la asistencia al curso
                               6  El Formador ha demostrado conocer los temas tratados en profundidad
                               7  El formador ha dinamizado el grupo, generando un clima que ha favorecido al aprendizaje.
                               8  Los materiales y documentación utilizados han sido comprensibles y adecuados
                               9  El Equipamiento y medios técnicos (pizarra, proyector...)
                               10  El Aula e instalaciones (espacio, luminosidad, ventilación....)
                               11  El curso le ha permitido adquirir nuevas habilidades/capacidades  que pueda aplicar al puesto de trabajo?
                               12  Recomendaría este curso a otros compañeros

                                '''
                cuestionarios14 += 1
                informaP = df_seleccionados["Valor"][0]
                orientadosP = df_seleccionados["Valor"][1]
                organizacionP = df_seleccionados["Valor"][2]
                espectativasP = df_seleccionados["Valor"][3]
                mejoraraP = df_seleccionados["Valor"][4]
                duraciónP = df_seleccionados["Valor"][5]
                materialP = df_seleccionados["Valor"][6]
                plataformaP = df_seleccionados["Valor"][7]
                erroresP = df_seleccionados["Valor"][8]
                serviciosP = df_seleccionados["Valor"][9]
                metodologiaP = df_seleccionados["Valor"][10]
                temarioP = df_seleccionados["Valor"][11]
                presentacionP = df_seleccionados["Valor"][12]
                salidapresencial.write(str(codigo)+";"+str(nombre)+";"+str(area)+";"+";"+str(round(materialP, 2))+";"+str(round(erroresP, 2))+";"+str(round(mejoraraP, 2))+";"+str(round(temarioP, 2))+";"+str(round(plataformaP, 2))+";"+str(round(espectativasP, 2))+";"+str(round(presentacionP, 2))+'\n')
                #cd;formador;material;duracion;productividad;dinamico;practicas;recomendaria
                media_informaP += float(informaP)
                media_orientadosP += float(orientadosP)
                media_organizacionP += float(organizacionP)
                media_espectativasP += float(espectativasP)
                media_mejoraraP += float(mejoraraP)
                media_duraciónP += float(duraciónP)
                media_materialP += float(materialP)
                media_plataformaP += float(plataformaP)
                media_erroresP += float(erroresP)
                media_serviciosP += float(serviciosP)
                media_metodologiaP += float(metodologiaP)
                media_temarioP += float(temarioP)
                media_presentacionP += float(presentacionP)
        '''VALORES PROMEDIOS DEL PLAN FORMATIVO ONLINE
        media_edad = media_edad/cuestionaris46
        salida.write("<ul>")
        salida.write("<li><b>Edad: </b>" + str(media_edad / cuestionaris46) + "</li>")
        '''
        salidapromedioonline.write(str(round(media_profesor/cuestionaris46, 2))+";"+str(round(media_plataforma/cuestionaris46, 2))+";"+str(round(media_duración/cuestionaris46, 2))+";"+str(round(media_mejorara/cuestionaris46, 2))+";"+str(round(media_metodologia/cuestionaris46, 2))+";"+str(round(media_Practicas/cuestionaris46, 2))+";"+str(round(media_Plan//cuestionaris46, 2))+'\n')
        '''
        #************************************************************************
        VALORES PROMEDIOS DEL PLAN FORMATIVO PRESENCIAL
        '''
        salidapromediopresencial.write(str(round(media_materialP/cuestionarios14, 2)) + ";" + str(
            round(media_erroresP/cuestionarios14, 2)) + ";" + str(round(media_mejoraraP/cuestionarios14, 2)) + ";" + str(round(media_temarioP/cuestionarios14, 2)) + ";" + str(
            round(media_plataformaP/cuestionarios14, 2)) + ";" + str(round(media_espectativasP/cuestionarios14, 2)) + ";" + str(round(media_presentacionP/cuestionarios14, 2)) + '\n')
encuesta()