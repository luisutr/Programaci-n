matriz = [[i] * 3 for i in xrange(3)]

def print_r(matriz):
    for fila in matriz:
        print fila


def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in xrange(rows)] for i in xrange(cols)]


#print "Original"
#print_r(matriz)
#print "TRANSPUESTA"
#print_r(transpuesta(matriz))

def transpuesta2(m):
    transp=[]
    for numcol in range(len(m[0])):
        fila=[]
        for numfil in range(len(m)):
            fila.append(m[numfil][numcol])
        transp.append(fila)
    return transp
#print transpuesta([[1,2,3],[4,5,6],[7,8,9]])
print transpuesta2([[1,2,3],[4,5,6],[7,8,9]])

import string
def find_missing_letter(chars):
    listabc=[]
    if chars[0].islower():
        minus = True
        abc = (string.ascii_letters)
    else:
        abc = (string.ascii_letters).upper()
    for i in abc:
        listabc.append(i)
    for j in listabc:
        if j not in chars:
            return j
    return -1

print find_missing_letter(['O','Q','R','S'])