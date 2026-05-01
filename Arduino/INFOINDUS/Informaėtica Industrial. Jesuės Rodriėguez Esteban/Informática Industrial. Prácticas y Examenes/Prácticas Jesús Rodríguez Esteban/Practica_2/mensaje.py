import serial

def abrirPort(p):
    return serial.Serial(
port = p,
baudrate = 115200,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
bytesize = serial.EIGHTBITS
)
def sendMensaje(ps,s):  #función que empleamos para enviar el mensaje
    ps.write( s.encode("utf-8") ) #codificacion que soporta acentos y ñ entre otros

def receiveMensaje(ps):  #función que emplemos para recivir el mensaje y almacenarlo en la variable r
    r = ps.readline()
    return r.decode()[0:-1]
