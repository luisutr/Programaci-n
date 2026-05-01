import socket
# El cliente debe tener las mismas especificaciones del servidor
host = "127.0.0.1"
port = 12345
BUFFER_SIZE = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    # Convertimos str a bytes
    while (2 >= 1):
        MESSAGE = input("Escribe mensaje: ")  # Datos que queremos enviar
        socket_tcp.send(MESSAGE.encode('utf-8'))
        data = socket_tcp.recv(BUFFER_SIZE)
        print(data)
