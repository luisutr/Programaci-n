# TRATAMIENTO DE IMAGENES BASICO.
# EJERCICIO 1. OBTENER LAS CAJAS DELIMITADORAS.
from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show


def get_bb(img, rectang, color):
    yi, xi, yf, xf = rectang
    red,green, blue = color
    for x in range(xi, xf):
        for y in range(yi, yf):
            if img[x, y, 0] != red and img[x, y, 1] != green and img[x, y, 2] != blue:
                x1 = x + 1
    for y in range(yi, yf):
        for x in range(xi, xf):
            if img[x, y, 0] != red and img[x, y, 1] != green and img[x, y, 2] != blue:
                y1 = y + 1
    for x in reversed(range(xi, xf)):
        for y in range(yi, yf):
            if img[x, y, 0] != red and img[x, y, 1] != green and img[x, y, 2] != blue:
                x2 = x
    for y in reversed(range(yi, yf)):
        for x in range(xi, xf):
            if img[x, y, 0] != red and img[x, y, 1] != green and img[x, y, 2] != blue:
                y2 = y

    return (y2, x2, y1, x1)

def encuentray2(xi,yi,xf,yf, img, color):
    for y in reversed(range(yi, yf)):
            for x in reversed(range(xi, xf)):
                if tuple(img[x, y]) != color:
                    return  y+1

def draw_rect(img,r,color):
    xi=r[0]
    yi=r[1]
    xf=r[2]
    yf=r[3]
    img[yi:yf, xi] = color
    img[yi:yf, xf] = color
    img[yi, xi:xf] = color
    img[yf, xi:xf] = color
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
    return show()

def find_bb(img, hormigas):
    # OJO estamos cambiando la imagen para obligar a coger la de ants.png
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

def autocrop(ruta):
    # OJO estamos cambiando la imagen para obligar a coger la de ants.png
    img = imread('img/ants.png')
    #Dimension de la imagen
    height, width, channels = img.shape
    #Buscamnos el color mas repetido (fondo)
    colordefondo = colormasrepido(img, (0,0,width,height))
    # con dimension y el color mas repetido, busco las dos coordenadas  que me delimitan las hormigas
    r = get_bb(img, (0,0,width,height), colordefondo)
    xi, yi, xf, yf = r
    # me creo una iumagen nueva con el recuadro de ocupan todas las hormigas ajustadas
    crop_lena = img[xi:xf, yi:yf]
    # lo guardo en una imagen por si hiciera falta
    imwrite('img/ants2.png', crop_lena)
    imshow(crop_lena)
    return show()
def colormasrepido(img, r):
    x1, y1, x2, y2 = r
    dicc_color = {}
    '''
    recorro todos los pixel y voy contando y voy creando un diccionario 
    si el color no existe lo creo y le asigo el valor 1 
    si color ecxiste incremento en 1 su valor 
    
    luego saco el maxo del diccionario y que me devuelva el color mas repetido
    '''
    for x in range(x1, x2):
        for y in range(y1, y2):
            if tuple(img[y,x]) in dicc_color.keys():
                dicc_color[tuple(img[y,x])] = dicc_color[tuple(img[y,x])]+1
            else:
                dicc_color[tuple(img[y, x])]=1
    return max(dicc_color)
    
def get_mask(img, color):
    # OJO estamos cambiando la imagen para obligar a coger la de ants.png
    img = imread('img/ants.png')
    height, width, channels = img.shape
    r = (0,0,width,height)
    xi = r[0]
    yi = r[1]
    xf = r[2]
    yf = r[3]
    for x in range(xi, xf):
        for y in range(yi, yf):
            if tuple(img[y, x]) == color:
                img[y,x] = 0
            else:
                img[y,x] = 255
    imshow(img)
    return show()