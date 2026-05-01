from matplotlib.pyplot import imshow,show
from imageio import *

def maxcomp2 (imagen):
    imagen = imread(imagen)
    size_x = len(imagen[1, :])
    size_y = len(imagen[:, 1])
    for i in range(1,size_x):
        for j in range (1,size_y):
            if imagen[i, j, 0] != max(imagen[i, j]):
                imagen[i, j, 0] = 0
            if imagen[i, j, 1] != max(imagen[i, j]):
                imagen[i, j, 1] = 0
            if imagen[i, j, 2] != max(imagen[i, j]):
                imagen[i, j, 2] = 0
    imwrite('nueva.png', imagen)
    imshow(imagen)
    return show()

maxcomp2('img/ants.png')

def maxcomp():
    img = imread('img/ants.png')
    #Dimension de la imagen
    height, width, channels = img.shape
    #Buscamnos el color mas repetido (fondo)
    x1, y1, x2, y2 = 0,0,width,height
    #PINTAMOS LA NEUVA IMAGEN
    for x in range(x1, x2):
        for y in range(y1, y2):
            componentemaxima = max(img[y, x])
            if img[y, x, 0] != componentemaxima:
                img[y, x, 0]= 0
            if img[y, x, 1] != componentemaxima:
                img[y, x, 1]= 0
            if img[y, x, 2] != componentemaxima:
                img[y, x, 2]= 0
    # lo guardo en una imagen por si hiciera falta
    imwrite('img/ants2.png', img)
    imshow(img)
    return show()



def raiz_cubica_precision(numero, precision):
    cifras_despues_de_la_coma = len(str(int(1/precision))) - 1
    return round(raiz_cubica(numero), cifras_despues_de_la_coma)

def raiz_cubica(numero):
    return numero**(1. / 3.)


def root_n(x, n, epsilon):
    yk = 1;
    while abs(yk ** n - x) > epsilon:
        yk = -((yk ** n - x) / (n * yk ** (n - 1))) + yk
    return yk
