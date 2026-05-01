def main():
    C,Dimension = 0,0
    Sistema = []
    Sistema, Dimension = PideDatos(Dimension,Sistema)
    print("\n\n\nEl SISTEMA introducido es el siguiente: \n\n")
    EscribeDatos(Dimension,Sistema);
    Sistema = ResuelveGauss(Dimension,Sistema);
    print("\n\n\nLas soluciones son:\n");
    for C in range(Dimension):
        print("\n X%d=%f\n",C,Sistema[C][Dimension+1])

def PideDatos(Dim, Sist):
    A,B = 0,0
    print("\n\n ||RESUELVE SISTEMAS LINEALES DETERMINADOS POR GAUSS||")
    Dim=input("\n\n\n Introduce el numero de incognitas:(menor que 100)")
    print("\n\n PASE A INTRODUCIR CADA COMPONENTE DEL SISTEMA (A|B):")
    print("\n\n MATRIZ A:\n")
    for A in range(Dim):
        fila = []
        for B in range(Dim):
            fila.append(input("\n Termino:"+str(A)+", "+str(B)))
        Sist.append(fila)
    for A in range(len(Sist)):
        print(Sist[A])
    return Sist, Dim


def EscribeDatos(Dim, Sist):
    for A in range(len(Sist)):
        x = Sist[A]
        for B in x:
            print B,
        print

"""
def ResuelveGauss(Dim, Sist):
    NoCero,Col,C1,C2,A = 0,0,0,0,0
    Pivote,V1 = 0.0, 0.0
    for Col in range(Dim):
        NoCero=0;A=Col;
        while(NoCero==0):
           if((Sist[A][Col]>0.0000001) or ((Sist[A][Col]<-0.0000001))):
                NoCero=1
           else:
                A+=1
        Pivote=Sist[A][Col]
        for C1 in range(Dim):
            V1=Sist[A][C1]
            Sist[A][C1]=Sist[Col][C1]
            Sist[Col][C1]=V1/Pivote
        for C2 in range(Col+1,Dim):
            V1=Sist[C2][Col]
            for C1 in range(Col,Dim+1):
                Sist[C2][C1]=Sist[C2][C1]-V1*Sist[Col][C1]
    for Col in reversed(range(Dim)):
        for C1 in reversed(range(Col-1)):
            Sist[C1][Dim+1]=Sist[C1][Dim+1]-Sist[C1][Col]*Sist[Col][Dim+1]
            Sist[C1][Col]=0
    return Sist


main()
"""

#matriz=[[9.0,8.0,7.0],[6.0,5.0,4.0],[3.0,2.0,1.0]]


#Uso auxiliares, porque si opero directamente con la fila, se modifica la matriz sin querer.
#las asignaciones de variables a la matriz indexan a esta y si modifico esa variable se modifica la matriz.
def dividirlista(fila,elemento):
    aux=[]
    for i in fila:
        aux.append(i/elemento)
    return aux
def multiplicarlista(fila,elemento):
    aux=[]
    for i in fila:
        aux.append(i*elemento)
    return aux
def restar(fila,fila2):
    aux=[]
    for i in range(len(fila)):
        aux.append(fila[i]-fila2[i])
    return aux

def escribe(matriz,fila,posicion):
        matriz[posicion]=fila

#Elimino la fila y me la llevo al final de la matriz
#Asi el elemento posterior ocupa su lugar
def cambiarfilas(matriz,posicion):
    matriz.append(matriz[posicion])
    matriz.pop(posicion)
    pivotear(matriz,posicion)

#Si la fila vale como pivote, es decir, el elemento que necesita para operar no es 0
#Divide toda la fila por el elemento de la misma fila, con el que operara para que se quede con valor 1
def pivotear(matriz,posicion):
    pivote=[]
    for i in range(len(matriz[posicion])):
        elem=matriz[posicion][i]
        if i == posicion and elem==0:
            cambiarfilas(matriz,posicion)#si la fila tiene 0 y no puedo usarla como pivote, la cambio.
        pivote.append(matriz[posicion][i])
    pivote=dividirlista(pivote,pivote[posicion])
    return pivote

def rango_matriz(matriz):
    resultado=gaussjordan(matriz)
    rango = 0
    for i in range(len(resultado)):
        fila=resultado[i]
        bandera=0
        for j in range(len(fila)):
            if fila[j] != 0:
                bandera = 1
        if bandera == 1:
            rango +=1
    print rango


def gaussjordan(matriz):
    for i in range(len(matriz)-1):
        fila = matriz[i+1]
        elementos = i+1
        for posicion in range(elementos):
            pivote=pivotear(matriz,posicion)
            matriz[posicion]=pivote
            fila=restar(fila, multiplicarlista(pivote,fila[posicion]))
            matriz[i+1]=fila
    print matriz
    return matriz

rango_matriz([[1,0,0], [0,1,0], [0,0,1]])
#3

rango_matriz([[1,1,1], [1,0,1], [1,2,3]])
#2

