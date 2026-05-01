# -*- coding: utf-8 -*-
import pandas as pd
import codecs

dic_cursos = {1: "GESTIÓN Y ARCHIVOS DE DOCUMENTOS ELECTRÓNICOS. TRAMITACIÓN ELECTRÓNICA DE EXPEDIENTES", 2: "CONTRATACIÓN PÚBLICA ELECTRÓNICA: LA E-CONTRATACIÓN", 3: "REDES SOCIALES. ESPECIAL ATENCIÓN A LOS SISTEMAS DE PROTECCIÓN DE DATOS", 4: "DESARROLLO Y EJECUCIÓN PRESUPUESTARIA EN LAS ENTIDADES LOCALES", 5: "INVERSIONES FINANCIERAMENTE SOSTENIBLES", 6: "ELABORACIÓN Y APLICACIÓN PRÁCTICA DE LAS BASES DE EJECUCIÓN DEL PRESUPUESTO. MARCO NORMATIVO", 7: "ELABORACIÓN, SEGUIMIENTO Y MODIFICACIÓN DE LOS PLANES ECONÓMICO FINANCIEROS EN LAS EELL", 9: "LIDERAZGO Y HABILIDADES DIRECTIVAS", 10: "URGENCIAS SANITARIAS PARA PRIMEROS INTERVINIENTES", 11: "REANIMACIÓN CARDIO PULMONAR BÁSICA CON DESA", 12: "INTERVENCIÓN EN ACCIDENTES DE TRÁFICO CON CISTERNAS", 13: "BUSQUEDA DE PERSONAS DESAPARECIDAS CON PERROS DE RASTRO", 14: "INTERVENCIÓN CON RIESGO BIOLÓGICO EN SERVICIOS DE EMERGENCIAS", 15: "TALA,  PODA Y ACTUACIONES DE PREVENCIÓN DE RIESGOS CON PLATAFORMA ELEVADORA", 16: "INTERVENCIÓN EN ACCIDENTES DE TRÁFICO   ", 17: "INTERVENCIÓN POLICIAL EN CASOS DE VÍCTIMAS DE DELITOS VIOLENTOS,  DE GÉNERO Y SEXUALES", 18: "INTERVENCIÓN POLICIAL EN CASOS DE RESPONSABILIDAD PENAL DE MENORES", 20: "ACTUACIONES POLICIALES EN MATERIA DE CONTAMINACIÓN ACÚSTICA", 21: "COMUNICACIÓN NO VIOLENTA", 22: "ASERTIVIDAD Y EMPATÍA. CLAVES EN NUESTRAS RELACIONES SOCIALES", 23: "MANEJO DE SITUACIONES DE RIESGO FÍSICO O PSICOLOGICO EN LA ATT A USUARIOS DE SERVICIOS PUBLICOS", 24: "ATENCIÓN A LA CIUDADANÍA ANTE SITUACIONES DE PÁNICO COLECTIVO", 25: "ACTUALIZACIÓN EN INTERVENCIÓN SOCIAL ANTE CASOS DE VIOLENCIA DE GÉNERO Y FAMILIAR", 26: "PREVENCIÓN Y ACTUACIÓN ANTE LAS NUEVAS ADICCIONES ( RRSS,  VIDEO JUEGOS,  JUEGOS DE AZAR…)", 27: "PREVENCIÓN DE LA DELINCUENCIA JUVENIL", 28: "RIESGOS PSICOSOCIALES DERIVADOS DEL TRABAJO CON USUARIOS EN RIESGOS O SITUACIÓN DE EXCLUSIÓN SOCIAL", 29: "INTERVENCIÓN CON FAMILIAS MULTIPROBLEMATICAS EN SITUACIÓN DE EXCLUSION SOCIAL", 30: "TÉCNICAS DE ASESORAMIENTO INNOVADOR PARA EL DESARROLLO DE  ECOSISTEMAS EMPRENDEDORES", 31: "ARABE PARA LA ATENCIÓN AL PÚBLICO. INICIACIÓN", 32: "INGLÉS PARA LA ATENCIÓN AL PÚBLICO – NIVEL B1", 33: "ATENCIÓN ELECTRÓNICA AL CIUDADANO", 34: "LEY 39/2015 DE PROCEDIMIENTO ADMINISTRATIVO LOCAL. ASPECTOS PRÁCTICOS", 35: "LEY 40/2015 DE RÉGIMEN JURÍDICO DEL SECTOR PÚBLICO. ASPECTOS PRÁCTICOS", 36: "CONTRATO DE OBRA,  SERVICIOS Y SUMINISTROS. ASPECTOS PRÁCTICOS DE SU TRAMITACIÓN", 38: "LOS CONTRATOS DE GESTIÓN DE SERVICIOS PÚBLICOS EN LA LEY 9/2017. ASPECTOS PRÁCTICOS", 39: "LA NUEVA LEY ORGÁNICA DE PROTECCIÓN DE DATOS. ESPECIALIDADES Y ASPECTOS PRÁCTICOS DE SU APLICACIÓN", 40: "EL CONTRATO MENOR. TIPOS,  PROCEDIMIENTO,  TRAMITACIÓN Y EJEMPLOS PRÁCTICOS", 41: "PREPARACIÓN DE LOS CONTRATOS Y PROCEDIMIENTOS DE CONTRATACIÓN", 42: "NNTT Y COMMUNITY MANAGER EN EL AMBITO LOCAL", 43: "PAQUETE OFFICE", 44: "OFIMÁTICA Y E-ADMINISTRACIÓN", 45: "VIOLENCIAS DE GÉNERO EN REDES SOCIALES: ACTUACIONES EN MATERIA DE PREVENCIÓN", 46: "MOBBING,  BULLYNG,  ACOSO SEXUAL,  CIBERACOSO: LAS DIFERENTES FORMAS DEL ACOSO Y SU REPERCUSIÓN", 47: "IMPLANTACIÓN DE SISTEMAS DE GESTIÓN DE LA SEGURIDAD Y SALUD EN EL TRABAJO. NORMA ISO 45001", 48: "ELABORACIÓN DE PLANES DE AUTOPROTECCIÓN", 49: "CONTENIDO Y APLICACIÓN PRÁCTICA DE LA RPT Y LA PLANTILLA DE PLAZAS COMO INSTRUMENTOS BÁSICOS DE LA LEGALIDAD Y LA GESTIÓN DE LOS RRHH", 50: "TRANSPARENCIA,  ADMINISTRACIÓN ELECTRÓNICA Y PROTECCIÓN DE DATOS. NOVEDADES TRAS LA LOPD 2018", 51: "ESTRATEGIAS LOCALES CONTRA EL CAMBIO CLIMÁTICO. REDUCCIÓN DE LA HUELLA DE CARBONO A NIVEL LOCAL", 52: "CONTROL DE CALIDAD DE LAS AGUAS", 53: "IMPLEMENTACIÓN DE LA AGENDA URBANA EN LOS MUNICIPIOS", 54: "NUEVA LEY DE EVALUACIÓN AMBIENTAL. 9 /18", 55: "RESPONSABILIDAD Y ACTUACIÓN INSPECTORA DE LAS CCLL EN MATERIA DE INFRACCIONES Y DELITOS MEDIOAMBIENTALES", 56: "IMPLANTACIÓN Y GESTIÓN DE ECOPARQUES Y PUNTOS LIMPIOS", 57: "ANÁLISIS DE PROBLEMAS Y TOMA DE DECISIONES", 58: "ASPECTOS GENERALES DE LA AGENDA 2030 Y ODS", 59: "GESTIÓN DE PROYECTOS EUROPEOS Y BÚSQUEDAS DE SUBVENCIONES", 61: "HERRAMIENTA PARA LA IMPLEMENTACIÓN Y MEJORA DE POLÍTICAS DE INFANCIA", 62: "RECICLAJE PROFESIONAL PARA AUXILIARES DE AYUDA A DOMICILIO"}
salida = codecs.open("encuestas.html", "w+")

def cursos(codigo):
    print(type(codigo),codigo)
    df = pd.read_excel('cursos.xlsx', sheet_name='Hoja1')
    columnas = ["CD", "NOMBRE", "AREA", "MODALIDAD", "PLAZAS", "HORAS", "EDICIONES"]
    '''CD	NOMBRE	AREA	MODALIDAD	PLAZAS	HORAS	EDICIONES'''
    df_seleccionados = df[columnas]
    for i in range(len(df_seleccionados)):
        '''
        Codigo del curso
        Nombre
        Plazas
        Horas
        Modalidad
        Número de ediciones
        Area 
        '''
        cd = str(df_seleccionados["CD"][i]).split(".")
        cd = int(cd[0])
        if(cd) == codigo:
            print(df_seleccionados["NOMBRE"][i])
            salida.write("***")
            salida.write("<h3>"+str(df_seleccionados["NOMBRE"][i]) + "</h3>")
            salida.write("<ul><li>")
            salida.write("<b>Código del curso: </b>"+str(df_seleccionados["CD"][i]))
            salida.write("</li>")
            salida.write("<li class='MsoNormal''>")
            salida.write("<b>Nombre del curso: </b>" + str(df_seleccionados["NOMBRE"][i]))
            salida.write("</li>")
            salida.write("<li class='MsoNormal'>")
            salida.write("<b>Horas del curso: </b>"+str(int(df_seleccionados["HORAS"][i])))
            salida.write("</li>")
            salida.write("<li class='MsoNormal'>")
            salida.write("<b>Modalidad: </b>" + str(df_seleccionados["MODALIDAD"][i]))
            salida.write("</li>")
            salida.write("<li class='MsoNormal'>")
            salida.write("<b>Área: </b>" + str(df_seleccionados["AREA"][i]))
            salida.write("</li></ul>")

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
            print(codigo, nombre)
            cursos(codigo)
            salida.write("<h4>" + "DATOS DE LAS ENCUESTAS" + "</h4>")
            salida.write("<table border='0' cellspacing='2' style='width:40%'><tbody>")
            #Abro el archivo, saco la información de la encuesta y lo voy escribiendo en salida
            df = pd.read_csv("./ENCUESTA/"+linea[:-1], encoding = "ISO-8859-1", sep=';', decimal=',')
            columnas = ["Orden","Pregunta", "Respuesta","Valor"]
            df_seleccionados = df[columnas]
            #cuestionarios de 46 preguntas
            if len(df_seleccionados) == 46:
                cuestionaris46 += 1
                edad = df_seleccionados["Valor"][6]
                media_edad += float(edad)
                # for i in range(13,len(df_seleccionados)):
                # 14, 15	Se informa correctamente de los cursos
                informa = (df_seleccionados["Valor"][12] + df_seleccionados["Valor"][13]) / 2
                salida.write("<tr><td>")
                salida.write(
                    "Se informa correctamente del plan formativo: </td><td>" + str(round(informa, 3)) + "</td>")
                salida.write("</tr>")
                media_informa += float(informa)
                # 17	Cursos orientados a necesidades
                orientados = df_seleccionados["Valor"][15]
                salida.write("<tr><td>")
                salida.write("Cursos orientados a necesidades:</td><td>" + str(round(orientados, 3)) + "</td>")
                salida.write("</tr>")
                media_orientados += float(orientados)
                # 18	organización de los cursos
                organizacion = df_seleccionados["Valor"][16]
                salida.write("<tr><td>")
                salida.write("Organización del curso:</td><td>" + str(round(organizacion, 3)) + "</td>")
                salida.write("</tr>")
                media_organizacion += float(organizacion)
                # 19, 22	espectativas satisfechas
                espectativas = (df_seleccionados["Valor"][17] + df_seleccionados["Valor"][20]) / 2
                salida.write("<tr><td>")
                salida.write("El curso ha cubierto las espectativas:</td><td>" + str(round(espectativas, 3)) + "</td>")
                salida.write("</tr>")
                media_espectativas += float(espectativas)
                # 20,21, 41, 42, 43	mejorara mi trabajo
                mejorara = (df_seleccionados["Valor"][18] + df_seleccionados["Valor"][19] + df_seleccionados["Valor"][
                    39] + df_seleccionados["Valor"][40] + df_seleccionados["Valor"][41]) / 5
                salida.write("<tr><td>")
                salida.write("Mejora la realización del trabajo:</td><td>" + str(round(mejorara, 3)) + "</td>")
                salida.write("</tr>")
                media_mejorara += float(mejorara)
                # 24	duración
                duración = df_seleccionados["Valor"][22]
                salida.write("<tr><td>")
                salida.write("La duración del curso es adecuada:</td><td>" + str(round(duración, 3)) + "</td>")
                salida.write("</tr>")
                media_duración += float(duración)
                # 26	Buen material didactico
                material = df_seleccionados["Valor"][24]
                salida.write("<tr><td>")
                salida.write("Cómo se valora el material didáctico:</td><td>" + str(round(material, 3)) + "</td>")
                salida.write("</tr>")
                media_material += float(material)
                # 23	plataforma
                plataforma = df_seleccionados["Valor"][21]
                salida.write("<tr><td>")
                salida.write("Como se valora la plataforma e-learning:</td><td>" + str(round(plataforma, 3)) + "</td>")
                salida.write("</tr>")
                media_plataforma += float(plataforma)
                # 25	errores en la plataforma
                errores = df_seleccionados["Valor"][23]
                salida.write("<tr><td>")
                salida.write(
                    "Considera que la plataforma se puede mejorar:</td><td>" + str(round(errores, 3)) + "</td>")
                salida.write("</tr>")
                media_errores += float(errores)
                # 27	servicios de la pltaforma
                servicios = df_seleccionados["Valor"][25]
                salida.write("<tr><td>")
                salida.write(
                    "La plataforma dispone de los servicios necesarios:</td><td>" + str(round(servicios, 3)) + "</td>")
                salida.write("</tr>")
                media_servicios += float(servicios)
                # 28	metodología correcta
                metodologia = df_seleccionados["Valor"][26]
                salida.write("<tr><td>")
                salida.write("La metodología es correcta:</td><td>" + str(round(metodologia, 3)) + "</td>")
                salida.write("</tr>")
                media_metodologia += float(metodologia)
                # 29	correspondencia de temario
                temario = df_seleccionados["Valor"][27]
                salida.write("<tr><td>")
                salida.write(
                    "Correspondencia del temario con lo informado:</td><td>" + str(round(temario, 3)) + "</td>")
                salida.write("</tr>")
                media_temario += float(temario)
                # 30	organización y presentacion de cursos
                presentacion = df_seleccionados["Valor"][28]
                salida.write("<tr><td>")
                salida.write("Organización y presentación del cursos:</td><td>" + str(round(presentacion, 3)) + "</td>")
                salida.write("</tr>")
                media_presentacion += float(presentacion)
                # 32	hipervinculos bien
                hipervinculos = df_seleccionados["Valor"][30]
                salida.write("<tr><td>")
                salida.write(
                    "Los hipervínculos expuestos estaban activos:</td><td>" + str(round(hipervinculos, 3)) + "</td>")
                salida.write("</tr>")
                media_hipervinculos += float(hipervinculos)
                # 31	Practicas
                Practicas = df_seleccionados["Valor"][29]
                salida.write("<tr><td>")
                salida.write("Suficientes ejercicios prácticos:</td><td>" + str(round(Practicas, 3)) + "</td>")
                salida.write("</tr>")
                media_Practicas += float(Practicas)
                # 34	han ayudado las practicas
                ayudado = df_seleccionados["Valor"][32]
                salida.write("<tr><td>")
                salida.write("Han ayudado los ejercicios prácticos:</td><td>" + str(round(ayudado, 3)) + "</td>")
                salida.write("</tr>")
                media_ayudado += float(ayudado)
                # 33	profesor preparado
                profesor = df_seleccionados["Valor"][31]
                salida.write("<tr><td>")
                salida.write("Cualificación del profesor:</td><td>" + str(round(profesor, 3)) + "</td>")
                salida.write("</tr>")
                media_profesor += float(profesor)
                # 35,36	apoyo del tutor
                apoyo = (df_seleccionados["Valor"][33] + df_seleccionados["Valor"][34]) / 2
                salida.write("<tr><td>")
                salida.write("Se recibe apoyo del tutor:</td><td>" + str(round(apoyo, 3)) + "</td>")
                salida.write("</tr>")
                media_apoyo += float(apoyo)
                # 37	foro
                foro = df_seleccionados["Valor"][35]
                salida.write("<tr><td>")
                salida.write("Se han usado los foros y han sido de ayuda:</td><td>" + str(round(foro, 3)) + "</td>")
                salida.write("</tr>")
                media_foro += float(foro)
                # 38	seguimiento  bien
                seguimientob = df_seleccionados["Valor"][36]
                salida.write("<tr><td>")
                salida.write("Se ha ralizado un seguimiento correcto:</td><td>" + str(round(seguimientob, 3)) + "</td>")
                salida.write("</tr>")
                media_seguimientob += float(seguimientob)
                # 39	seguimiento mal
                seguimientom = df_seleccionados["Valor"][37]
                salida.write("<tr><td>")
                salida.write("Existen deficiencias en el seguimiento:</td><td>" + str(round(seguimientom, 3)) + "</td>")
                salida.write("</tr>")
                media_seguimientom += float(seguimientom)
                # 40	cuanto a aprendido
                aprendido = df_seleccionados["Valor"][38]
                salida.write("<tr><td>")
                salida.write("Valor del aprendizaje:</td><td>" + str(round(aprendido, 3)) + "</td>")
                salida.write("</tr>")
                media_aprendido += float(aprendido)
                # 44	Plan formativo
                Plan = df_seleccionados["Valor"][42]
                salida.write("<tr><td>")
                salida.write("Valoración general del plan formativo:</td><td>" + str(round(Plan, 3)) + "</td>")
                salida.write("</tr>")
                media_Plan += float(Plan)
            if len(df_seleccionados) == 14:
                cuestionarios14 += 1
                '''
                 La organización del curso ha sido la adecuada, cumplimiento de fechas/horarios, entrega de material.  
                 El número de alumnos del grupo ha sido el adecuado para el desarrollo del curso
                 Los contenidos del curso se han ajustado a tus expectativas
                 Ha habido una combinación adecuada de teoría y práctica
                 La duración del curso ha sido adecuada
                 El horario ha favorecido la asistencia al curso
                 El Formador ha demostrado conocer los temas tratados en profundidad
                 El formador ha dinamizado el grupo, generando un clima que ha favorecido al aprendizaje.
                 Los materiales y documentación utilizados han sido comprensibles y adecuados
                 El Equipamiento y medios técnicos (pizarra, proyector...)
                 El Aula e instalaciones (espacio, luminosidad, ventilación....)
                 El curso le ha permitido adquirir nuevas habilidades/capacidades  que pueda aplicar al puesto de trabajo?
                 Recomendaría este curso a otros compañeros

                '''
                informaP = df_seleccionados["Valor"][0]
                salida.write("<tr><td>")
                salida.write(
                    "La organización del curso ha sido la adecuada:</td><td>" + str(round(informaP, 3)) + "</td>")
                salida.write("</tr>")

                orientadosP = df_seleccionados["Valor"][1]
                salida.write("<tr><td>")
                salida.write("El número de alumnos del grupo ha sido el adecuado:</td><td>" + str(
                    round(orientadosP, 3)) + "</td>")
                salida.write("</tr>")

                organizacionP = df_seleccionados["Valor"][2]
                salida.write("<tr><td>")
                salida.write(
                    "Contenidos del curso ajustado a expectativas:</td><td>" + str(round(organizacionP, 3)) + "</td>")
                salida.write("</tr>")

                espectativasP = df_seleccionados["Valor"][3]
                salida.write("<tr><td>")
                salida.write(
                    "Combinación adecuada de teoría y práctica:</td><td>" + str(round(espectativasP, 3)) + "</td>")
                salida.write("</tr>")

                mejoraraP = df_seleccionados["Valor"][4]
                salida.write("<tr><td>")
                salida.write("Duración del curso adecuada:</td><td>" + str(round(mejoraraP, 3)) + "</td>")
                salida.write("</tr>")

                duraciónP = df_seleccionados["Valor"][5]
                salida.write("<tr><td>")
                salida.write("Horario del curso adecuado:</td><td>" + str(round(duraciónP, 3)) + "</td>")
                salida.write("</tr>")

                materialP = df_seleccionados["Valor"][6]
                salida.write("<tr><td>")
                salida.write("Formador cualificado:</td><td>" + str(round(materialP, 3)) + "</td>")
                salida.write("</tr>")

                plataformaP = df_seleccionados["Valor"][7]
                salida.write("<tr><td>")
                salida.write(
                    "El formador ha favorecido al aprendizaje:</td><td>" + str(round(plataformaP, 3)) + "</td>")
                salida.write("</tr>")

                erroresP = df_seleccionados["Valor"][8]
                salida.write("<tr><td>")
                salida.write(" Los materiales y documentación:</td><td>" + str(round(erroresP, 3)) + "</td>")
                salida.write("</tr>")

                serviciosP = df_seleccionados["Valor"][9]
                salida.write("<tr><td>")
                salida.write("Equipamiento y medios técnicos:</td><td>" + str(round(serviciosP, 3)) + "</td>")
                salida.write("</tr>")

                metodologiaP = df_seleccionados["Valor"][10]
                salida.write("<tr><td>")
                salida.write("Aula e instalaciones:</td><td>" + str(round(metodologiaP, 3)) + "</td>")
                salida.write("</tr>")

                temarioP = df_seleccionados["Valor"][11]
                salida.write("<tr><td>")
                salida.write("Mejora la realización del trabajo:</td><td>" + str(round(temarioP, 3)) + "</td>")
                salida.write("</tr>")

                presentacionP = df_seleccionados["Valor"][12]
                salida.write("<tr><td>")
                salida.write(" Recomendaría este curso:</td><td>" + str(round(presentacionP, 3)) + "</td>")
                salida.write("</tr>")

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

            salida.write("</tbody></table>")
        salida.write("<h3>" + "VALORES PROMEDIOS DEL PLAN FORMATIVO ONLINE" + "</h3>")
        media_edad = media_edad/cuestionaris46
        salida.write("<table border='0' cellspacing='2' style='width:40%'><tbody>")
        salida.write("<tr><td><b>Edad: </b></td><td>" + str(round(media_edad / cuestionaris46))+ "</td></tr>")
        salida.write("<tr><td><b>Se informa correctamente del plan de formación: </b>" + str(round(
            media_informa / cuestionaris46))+ "</td></tr>")
        salida.write("<tr><td><b>Cursos orientados a necesidades: </b>" + str(round(media_orientados / cuestionaris46),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>El curso ha cubierto las espectativas: </b>" + str(round(media_espectativas / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Mejora la realización del trabajo: </b>" + str(round(media_mejorara / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Organización del curso: </b>" + str(round(media_organizacion / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>La duración del curso es adecuada: </b>" + str(round(media_duración / cuestionaris46),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>Cómo se valora el material didáctico: </b>" + str(round(media_material / cuestionaris46),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>Como se valora la plataforma e-learning: </b>" + str(round(media_plataforma / cuestionaris46),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>Considera que la plataforma se puede mejorar: </b>" + str(round(media_errores / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>La plataforma dispone de los servicios necesarios: </b>" + str(round(
            media_servicios / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>La metodología es correcta: </b>" + str(round(media_metodologia / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Correspondencia del temario con lo esperado: </b>" + str(round(
            media_hipervinculos / cuestionaris46),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>Organización y presentación del curso: </b>" + str(round(media_temario / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Los hipervínculos expuestos estaban activos: </b>" + str(round(
            media_presentacion / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Suficientes ejercicios prácticos: </b>" + str(round(media_Practicas / cuestionaris46),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>Han ayudado los ejercicios prácticos: </b>" + str(round(media_ayudado / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Cualificación del profesor: </b>" + str(round(media_profesor / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Se recibe apoyo del tutor: </b>" + str(round(media_apoyo / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Se han usado los foros y han sido de ayuda: </b>" + str(round(
            media_seguimientom / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Se ha ralizado un seguimiento correcto: </b>" + str(round(media_foro / cuestionaris46),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>Existen deficiencias en el seguimiento: </b>" + str(round(media_seguimientob / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Valor del aprendizaje: </b>" + str(round(media_aprendido / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Valoración general del plan formativo: </b>" + str(round(media_Plan / cuestionaris46),3)+ "</td></tr>")
        salida.write("<tr><td><b>Media de edad: </b>" + str(round(media_edad / cuestionaris46),3)+ "</td></tr>")
        salida.write("</tbody></table>")
        #************************************************************************
        salida.write("<h3>" + "VALORES PROMEDIOS DEL PLAN FORMATIVO PRESENCIAL" + "</h3>")
        salida.write("<table border='0' cellspacing='2' style='width:40%'><tbody>")
        salida.write("<tr><td><b>La organización</b> del curso ha sido la adecuada: " + str(round(media_informaP/cuestionarios14),3)+ "</td></tr>")
        salida.write(
            "<tr><td><b>El número de alumnos</b> del grupo ha sido el adecuado: " + str(round(media_orientadosP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Contenidos del curso ajustado a expectativas</b>: " + str(round(media_organizacionP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Combinación adecuada de teoría y práctica</b>: " + str(round(media_espectativasP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Duración del curso adecuada</b>: " + str(round(media_mejoraraP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Horario del curso adecuado</b>: " + str(round(media_duraciónP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Formador cualificado</b>: " + str(round(media_materialP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>El formador ha favorecido al aprendizaje</b>: " + str(round(media_plataformaP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<li>Los materiales y documentación</b>: " + str(round(media_erroresP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Equipamiento y medios técnicos</b>: " + str(round(media_serviciosP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Aula e instalaciones</b>: " + str(round(media_metodologiaP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b>Mejora la realización del trabajo</b>: " + str(round(media_temarioP/cuestionarios14),3)+ "</td></tr>")
        salida.write("<tr><td><b> Recomendaría este curso</b>: " + str(round(media_presentacionP/cuestionarios14),3)+ "</td></tr>")
        salida.write("</tbody></table>")
encuesta()