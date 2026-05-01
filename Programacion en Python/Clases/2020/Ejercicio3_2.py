from matplotlib.pyplot import imshow,show
from imageio import imread
from math import *
color3 = (-50,50,50)
r = (122, 19, 300, 153)
img = imread('img/ants.png')

def colorea_highlight(img, x,y,capa,color):
    # MIro si en la componente rojo se pasa o no llega
    if (img[x, y, capa] + color[capa]) < 0:
        img[x, y, capa] = 0
    elif (img[x, y, capa] + color[capa]) > 255:
        img[x, y, capa] = 255
    else:
        img[x, y, capa] = img[x, y, capa] + color[capa]

def hl_rect(img,r,color3):
    xi,yi,xf,yf = r
    for y in range(xi, xf):
        for x in range(yi, yf):
            colorea_highlight(img, x,y,0,color3)
            colorea_highlight(img, x, y, 1, color3)
            colorea_highlight(img,x,y,2,color3)
    imshow(img)
    return show()

hl_rect(img,r,color3)


