import socket
import bancolista
PORT = 5490
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5 #maximo de conversaciones que puedes escuchar
# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
mibanco = bancolista.Banco()
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)
    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        mensaje_recibido = serversocket.recv(4096).decode("utf-8")
        print(mensaje_recibido)
        resultado = mibanco.ejecutar_orden(mensaje_recibido)
        send_message = resultado
        send_bytes = str.encode(send_message)
        clientsocket.send(send_bytes)

        if mensaje_recibido == "salir":
            clientsocket.close()

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
