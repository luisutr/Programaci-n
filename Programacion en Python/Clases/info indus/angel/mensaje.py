import serial

def abrirPort(p):
    return serial.Serial(
port = p,
baudrate = 115200,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
bytesize = serial.EIGHTBITS
)
def sendMensaje(ps,s):
    ps.write( s.encode("utf-8") )
def receiveMensaje(ps):
    r = ps.readline()
    return r.decode()[0:-1]
