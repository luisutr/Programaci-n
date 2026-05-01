# TRATAMIENTO DE IMAGENES BASICO.
# EJERCICIO 1. OBTENER LAS CAJAS DELIMITADORAS.
from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show


def get_bb(img, rectang, color):
    yi, xi, yf, xf = rectang
    for x in range(xi, xf):
        for y in range(yi, yf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                x1 = x + 1
    for y in range(yi, yf):
        for x in range(xi, xf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                y1 = y + 1
    for x in reversed(range(xi, xf)):
        for y in range(yi, yf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                x2 = x
    for y in reversed(range(yi, yf)):
        for x in range(xi, xf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                y2 = y

    return ((y2, x2, y1, x1))

def draw_rect(img,r,color):
    xi=r[0]
    yi=r[1]
    xf=r[2]
    yf=r[3]
    img[yi:yf, xi] = color
    img[yi:yf, xf] = color
    img[yi, xi:xf] = color
    img[yf, xi:xf] = color
    imshow(img)
    return show()


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
    #img[0:160, 100:300] =  (205,255,255, 200)

    imshow(img)
    return show()

def find_bb(img, hormigas):
    color = (-50, -50, 50)
    ctrazo = (0, 0, 250)
    for r in hormigas:
        r = get_bb(img, r, (255,255,255))
        img = draw_rect4(img, r, ctrazo)
        img = hl_rect4(img, r, color)
    imshow(img)
    return show()

def draw_rect4(img,r,color):
    xi=r[0]
    yi=r[1]
    xf=r[2]
    yf=r[3]
    img[yi:yf, xi] = color
    img[yi:yf, xf] = color
    img[yi, xi:xf] = color
    img[yf, xi:xf] = color
    return img

def hl_rect4(img,r,color3):
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
    return img