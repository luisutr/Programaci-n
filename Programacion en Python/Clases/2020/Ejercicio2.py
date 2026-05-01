## EJERCICIO 2

from matplotlib.pyplot import imshow,show
from imageio import imread

img = imread('img/ants.png')

def draw_rect(img,r,color):
    xi=r[0]
    yi=r[1]
    xf=r[2]
    yf=r[3]
    #xi,yi,xf,yf = r
    #rojo, verde, azull = color
    img[yi:yf, xi] = color
    #img[yi:yf, xi, 0] = rojo
    #img[yi:yf, xi, 1] = verde
    #img[yi:yf, xi, 2] = azul
    img[yi:yf, xf] = color
    img[yi, xi:xf] = color
    img[yf, xi:xf] = color
    #imshow(img)
    #return show()
    return img

#draw_rect(img, (4, 161, 161, 285), (0,255,0))
## pytest test_lab2.py::test_draw_rect

