from mensaje import*

PuertoSerie = abrirPort('COM3')

while True:
    print("1-Secuencia\n2-Raiz.Cuadrados")
    sec = receiveMensaje(PuertoSerie)
    sec = sec.split(":")
    if sec[0] == "1":
        rang = []
        for i in range(int(sec[2]), (int(sec[3]))+1, int(sec[4])):
            rang.append(i)
        rang = ','.join(str(e)for e in rang)
        print("\n-----------------------------------------------")
        print(rang)
        print("-----------------------------------------------\n")
        sendMensaje(PuertoSerie, rang + '\n')

    if sec[0] == "2":
        N = (int(sec[1])) + 2
        lfloats = []
        sum3 = 0
        for i in range(2, N):
            lfloats.append(float(sec[i]))
        print(lfloats)
        cuadrados = 0
        import math
        for j in lfloats:
            cuadrados += (j**2)
        resultado = round(math.sqrt(cuadrados),3)
        print("\n-----------------------------------------------")
        print(resultado)
        print("-----------------------------------------------\n")
        sendMensaje(PuertoSerie, str(resultado) + '\n')

    if sec[0] == "3":
        l = []
        for i in sec[2]:
            l.append(i)
        l_ord = sorted(l)
        str_v = ""
        for j in l_ord:
            str_v += j
        print("\n-----------------------------------------------")
        print(str_v)
        print("-----------------------------------------------\n")
        sendMensaje(PuertoSerie, str_v + '\n')
        conf = receiveMensaje(PuertoSerie)
        print("\n-----------------------------------------------")
        print(conf)
        print("-----------------------------------------------\n")

    if sec[0] == "4":
        rangos = []
        operac = []
        for i in range((int(sec[2])), (int(sec[3]))):
            rangos.append(i)
            ope = 2 * i * ((i + 1) ** 2)
            operac.append(ope)
        nu = rangos + operac
        nu = ','.join(str(e) for e in nu)
        ######### NO ESTA BIEN PLANTEADO EL ENUNCIADO NO SE LO QUE HAY QUE HACER#########


