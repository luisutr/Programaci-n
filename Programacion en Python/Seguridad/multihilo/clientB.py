# Python TCP Client B
import socket 

host = socket.gethostname() 
port = 12345
BUFFER_SIZE = 1024
MESSAGE = input("tcpClientB: Enter message/ Enter exit:")
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE.encode('utf-8'))
    data = tcpClientB.recv(BUFFER_SIZE)
    print(" Client received data:", data)
    MESSAGE = input("tcpClientB: Enter message to continue/ Enter exit:")

tcpClientB.close() 