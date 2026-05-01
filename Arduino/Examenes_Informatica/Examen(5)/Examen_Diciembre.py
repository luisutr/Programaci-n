from mensaje import*

PuertoSerie = abrirPort('COM3')

while True:
    print("1-Incremento\n2-Decremento\n3-Lista\n4-Lista.D")
    sec = receiveMensaje(PuertoSerie)
    sec = sec.split(":")
    if sec[0] == "1":
        incre = int(sec[1]) + 1
        sendMensaje(PuertoSerie, str(incre) + '\n')
        print(incre)

    if sec[0] == "2":
        decre = int(sec[1]) - 1
        sendMensaje(PuertoSerie, str(decre) + '\n')
        print(decre)

    if sec[0] == "3":
        lista = []
        for i in range(int(sec[1]), int(sec[2])+1):
            lista.append(i)
        lista = ",".join(str(e) for e in lista)
        sendMensaje(PuertoSerie, lista + '\n')
        print(lista)
        conf = receiveMensaje(PuertoSerie)
        print(conf)

    if sec[0] == "4":
        lista = []
        lista_d = []
        N = 0
        for i in range(int(sec[1]), int(sec[2])+1):
            N += 1
            lista.append(i)
            lista_d.append(i/int(sec[3]))
        sendMensaje(PuertoSerie, str(N) + '\n')
        lista_c = lista + lista_d
        lista_d = ':'.join(str(e) for e in lista_d)
        print(lista_d)
        sendMensaje(PuertoSerie, lista_d + '\n')
        lista_c = ':'.join(str(j) for j in lista_c)
        print(lista_c)
        sendMensaje(PuertoSerie, lista_c + '\n')
        conf = receiveMensaje(PuertoSerie)
        print(conf)
