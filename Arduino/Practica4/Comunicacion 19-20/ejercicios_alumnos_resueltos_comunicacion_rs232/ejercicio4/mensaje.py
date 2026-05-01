import serial

def abrirPort(p, port):
    return serial.Serial(
        port=p,
        baudrate=port,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

def sendMensaje(ps,s, fin='\n'):
    ps.write((s+fin).encode('utf-8'))

def receiveMensaje(ps):
    r = 'chg_'
    while r[0:4]=='chg_': # para e
        r = ps.readline().decode()[0:-2]
    return r

def cerrarPort(ps):
    ps.close()


