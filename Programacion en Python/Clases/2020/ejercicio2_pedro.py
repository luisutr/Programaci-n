# EJERCICIO 2. DIBUJAR UN RECTANGULO EN UNA IMAGEN.
from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show

def draw_rect(img, r, color):
    for y in range(19,153):
        img[y,122] = color
        img[y,300] = color
    for x in range(122,300):
        img[19,x] = color
        img[153,x] = color
    imshow(img)
    return show()

img = imread('img/ants.png')

draw_rect(img, (122, 19, 300, 153), (0, 255, 0) )