## EJERCICIO 2

from matplotlib.pyplot import imshow,show
from imageio import imread

img = imread('img/ants.png')
r = (122, 19, 300, 153)
color = (0,255,0)

def draw_rect(img,r,color):
    img[:, 19] = color
    img[19, :] = color
    imshow(img)
    return show()

draw_rect(img, r, color)