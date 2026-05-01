from matplotlib.pyplot import imshow,show
from imageio import *
from ejercicio1_2 import *

def draw_rect(img,r,color):
    xi=r[0]
    yi=r[1]
    xf=r[2]
    yf=r[3]
    img[yi:yf, xi] = color
    img[yi:yf, xf] = color
    img[yi, xi:xf] = color
    img[yf, xi:xf] = color
    return img

def autocrop(ruta):
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


autocrop('img/ants.png')

