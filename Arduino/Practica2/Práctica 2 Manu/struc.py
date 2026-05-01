def setA(struct, a):
    struct[0] = a
def setB(struct, b):
    struct[1] = b
def setResult(struct, r):
    struct[2] = r
def Suma(struct):
    setResult(struct, sum(struct[0:2]))
def Resta(struct):
    setResult(struct, float(struct[0]-struct[1]))
def Multiplicar(struct):
    setResult(struct, float(struct[0]*struct[1]))
def dividir(struct):
    setResult(struct, float(struct[0]/struct[1]))
def getResult(struct):
    return struct[2]