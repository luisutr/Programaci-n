# TRATAMIENTO DE IMAGENES BASICO.
# EJERCICIO 1. OBTENER LAS CAJAS DELIMITADORAS.
from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show

img = imread('img/ants.png')
rectang = (100,0,300,160)
def get_bb(img, rectang, color):
    xi, yi, xf, yf = rectang
    red,green, blue = color
    for x in range(xi, xf):
        for y in range(yi, yf):
            if img[y, x, 0] != red and img[y, x, 1] != green and img[y, x, 2] != blue:
                x1 = x + 1
    for y in range(yi, yf):
        for x in range(xi, xf):
            if img[y, x, 0] != red and img[y, x, 1] != green and img[y, x, 2] != blue:
                y1 = y + 1
    for x in reversed(range(xi, xf)):
        for y in range(yi, yf):
            if img[y, x, 0] != red and img[y, x, 1] != green and img[y, x, 2] != blue:
                x2 = x
    for y in reversed(range(yi, yf)):
        for x in range(xi, xf):
            if img[y, x, 0] != red and img[y, x, 1] != green and img[y, x, 2] != blue:
                y2 = y

    return (x2, y2, x1, y1)

print(get_bb(img, rectang, (255, 255, 255)))