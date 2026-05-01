from mensaje import*

PuertoSerie = abrirPort('COM3')

while True:
    import math
    import random
    print("1-Secuencia\n2-Raiz.Cuadrados")
    sec = receiveMensaje(PuertoSerie)
    sec = sec.split(":")

    if sec[0] == "1":
        op = int(sec[3]) * (math.sqrt(int(sec[1])/int(sec[2])))
        print("\n-----------------------------------------------")
        print(op)
        print("-----------------------------------------------\n")
        sendMensaje(PuertoSerie, str(op) + '\n')

    if sec[0] == "2":
        op = (int(sec[1])**2) + (int(sec[2])**2)
        print("\n-----------------------------------------------")
        print(op)
        print("-----------------------------------------------\n")
        sendMensaje(PuertoSerie, str(op) + '\n')

    if sec[0] == "3":
        l = []
        for i in range((int(sec[1])), (int(sec[3])) + 1):
            op = int(sec[3]) * math.sqrt((i) / int(sec[2]))
            l.append(int(op))
        sendMensaje(PuertoSerie, str(l) + '\n')
        print("\n-----------------------------------------------")
        print(l)
        print("-----------------------------------------------\n")
        conf = receiveMensaje(PuertoSerie)
        print("\n-----------------------------------------------")
        print(conf)
        print("-----------------------------------------------\n")

    if sec[0] == "4":
        l =[]
        l_ran = []
        for i in range (int(sec[1]), (int(sec[2]))+1):
            l.append(i)
            l_ran.append(i + random.randint(int(sec[1]), int(sec[2])))
        print(l)
        print("-------------------------------------------------")
        print(l_ran)
        sendMensaje(PuertoSerie, str(l) + '\n')
        sendMensaje(PuertoSerie, str(l_ran) + '\n')
        conf = receiveMensaje(PuertoSerie)
        print("-------------------------------------------------")
        print(conf)
        print("-------------------------------------------------")