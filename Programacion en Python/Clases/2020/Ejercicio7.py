from matplotlib.pyplot import *
from imageio import imread

def strelnueva(cadena, radio):
    img = imread('img/geometria.png')
    if cadena == "diamond":
        img = dibujarombo(img, radio)
    if cadena == "square":
        print()
    if cadena == "octagon":
        print()
    imshow(img)
    return show()

def cuadrado(img, radio):
    xi,yi,xf,yf= 0,0,100,100
    for y in range(xi, xf):
        for x in range(yi, yf):
            img[y,x] = 0,0,0
    return img

def dibujarombo(img, lado):
    xi, yi, xf, yf = 0, 0, 100, 100
    # primera mitad del rombo
    cont = 0
    for x in reversed(range(50)):
        y = cont
        img[y, x] = 0, 0, 0
        cont +=1
    cont = 0
    for x in range(51, 101):
        y = cont
        img[y, x] = 0, 0, 0
        cont +=1

    return img


strelnueva("diamond", 10)