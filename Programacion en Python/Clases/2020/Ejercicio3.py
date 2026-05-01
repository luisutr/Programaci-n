from matplotlib.pyplot import imshow,show
from imageio import imread
from math import *
img = imread('img/ants.png')

def hl_rect(img,r,color3):
    rojo= color3[0]
    verde= color3[1]
    azul= color3[2]
    xi = r[0]
    yi = r[1]
    xf = r[2]
    yf = r[3]
    for y in range(xi, xf):
        for x in range(yi, yf):
            # MIro si en la componente rojo se pasa o no llega
            if (img[x, y, 0] + rojo) < 0:
                img[x, y, 0] = 0
            elif (img[x, y, 0] + rojo) > 255:
                img[x, y, 0] = 255
            else:
                img[x, y, 0] = img[x, y, 0] + rojo
            # MIro si en la componente verde se pasa o no llega
            if (img[x, y, 1] + verde) < 0:
                img[x, y, 1] = 0
            elif (img[x, y, 1] + verde) > 255:
                img[x, y, 1] = 255
            else:
                img[x, y, 1] = img[x, y, 1] + verde
            # MIro si en la componente azul se pasa o no llega
            if (img[x, y, 2] + azul) < 0:
                img[x, y, 2] = 0
            elif (img[x, y, 2] + azul) > 255:
                img[x, y, 2] = 255
            else:
                img[x, y, 2] = img[x, y, 2] + azul
    imshow(img)
    return show()
    return img

hl_rect(img,(4, 161, 161, 285),(-50,50,50))


