import socket

HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096
videofile = "video.mp4"

bytes = open(videofile, "rb")

print (len(bytes))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send(bytes(chr(1), "utf-8"))

client.close()
