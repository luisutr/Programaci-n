__author__ = 'Luis'
# 0 1 2 3 4 5 0
# 1 2 3 4 5 1
# 2 3 4 5 2
# 3 4 5 3
# 4 5 4
# 5 5
# 6

#-*-coding:cp1252-*-
def piramidenumeros(numero):
    numcol=0
    while numcol<=numero:
        fila=numcol

        while (fila<numero):
            print fila,
            fila=fila+1

        print numcol,
        numcol=numcol+1
        print "\t"

piramidenumeros(6)

def piramide2(num):
    for i in range(num+1):
        for j in range(i,num):
            print j,
        print i

piramide2(6)