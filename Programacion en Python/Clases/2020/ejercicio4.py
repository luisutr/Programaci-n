from matplotlib.pyplot import imshow,show
from imageio import imread
from ejercicio1_2 import *
from Ejercicio2 import *
from Ejercicio3 import *
hormigas = [
    (100,0,300,160),
    (310,0,500,180),
    (450,150,600,340),
    (0,150,170,300),
    (50,300,200,500),
    (400,340,600,490),
    (200,400,400,589)
    ]

img = imread('img/ants.png')
'''
    me creo unas variaciones del ejercicio 2 y 3 que pinten en la imagen pero que no la devuelvan
    recorro lista de hormigas
    por cada hormiga llamo a mis variaciones de los ejervcicios 2 y 3 para que por cada rectangulo pinten en la imagen
    el recuadro y lo rellenen con el colo dicho

    Una vez he recorrido todas las hormigas
    puedop hacer el return

    '''
def find_bb(img, hormigas):
    img = imread('img/ants.png')
    color = (-50, -50, 50)
    ctrazo = (0, 0, 250)
    rhormigas = []
    for r in hormigas:
        r = get_bb(img, r, (255,255,255))
        rhormigas.append(r)
    for hormiga in rhormigas:
        draw_rect(img, hormiga, ctrazo)
        hl_rect(img, hormiga, color)
    imshow(img)
    return show()

find_bb(img, hormigas)