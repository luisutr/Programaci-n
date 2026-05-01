import socket

IP = "127.0.0.1"
PORT = 5490

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))
    funciona = True
    while funciona ==True:
        mensaje_recibido = s.recv(4096).decode("utf-8")
        print(mensaje_recibido)

        orden = input("crear cuenta presina 1, consulatr cuenta presiona 2")
        if orden == "1":
            mensaje("crear Cliente1 123123X CC0987654321 700 3")
            send_bytes = str.encode(mensaje)
            s.send(send_bytes)
            #hemos enviado, espero respuesta e imprimo por pantalla
            mensaje_recibido = s.recv(4096).decode("utf-8")
            print(mensaje_recibido)
        if orden == "2":
            mensaje("consulta CC0987654321")
            send_bytes = str.encode(mensaje)
            s.send(send_bytes)
            # hemos enviado, espero respuesta e imprimo por pantalla
            mensaje_recibido = s.recv(4096).decode("utf-8")
            print(mensaje_recibido)
            mensaje = input("")

        if mensaje =="salir":
            funciona = False
            #s.close()

except OSError:
    print("Socket already used")
    # But first we need to disconnect
    send_message = input("escribe el mesajeee")
    while send_message!="salir":
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
print("Read from the server", s.recv(2048).decode("utf-8"))
s.send(str.encode("adios\n"))

