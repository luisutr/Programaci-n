for posi, elemento in enumerate(["a",2,"b",4,"Pedro", 14.6]):
    if type(elemento) == int:
        if elemento == 4:
            print(posi)

def ordenar(lista):
    result = []
    longitud = len(lista)
    while (len(result)!= longitud):
        min = 999
        posmin = 0
        for posicion,valor in enumerate(lista):
            if min>valor:
                min = valor
                posmin = posicion
        result.append(min)
        lista.pop(posmin)
    return result

#print(ordenar([5,6,2,4,8,1,3,8,4,5]))


#[[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]

matriz = [[1,2,3,4,5],
        [2,2,3,4,5],
        [3,2,3,4,5],
        [4,2,3,4,5]
        ]

print("Valor maximo de x: " + str(len(matriz[0])))
print("Valor maximo de y: " + str(len(matriz)))
print(matriz[3])
print(matriz[3][0])

'''
for y in range(len(matriz)):
    for x in range(len(matriz[0])):
        print((x,y),matriz[y][x])

'''

#################################### IMAGENES #######################################

from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show
"""
img = imread('https://e00-elmundo.uecdn.es/television/programacion-tv/img/v2/programas/24/618532.png')

height, width, channels = img.shape
print(height, width, channels)
# poner un color determinado en un pixel de la imagen
y, x = 100, 30
for y,x in zip(range(100,110), range(30, 40)):
    img[y,x] = (50,50,50, 255)

# poner al máximo la componente roja de una línea horizontal
img[:,x,0] = 255   # img[:,x]=(255,0,0,255)

# poner a cero la componente azul de un rectángulo
img[100:250,50:120,1] = 255
img[100:150,50:60] = (255,0,0,255)

print(img[210,150])

imshow(img)
show()


#Dar la vuelta a la imagen
figure()
imshow(img[::-1,:])   #img[Y,X]
show()
"""

def pintarectangulo(img, r):
    x1,y1,x2,y2 = r
    for y in range(int(y1), int(y2)):
        img[y, x1] = (0, 0, 0)
        img[y, x2] = (0, 0, 0)
    for x in range(x1, x2):
        img[y1, x] = (0, 0, 0)
        img[y2, x] = (0, 0, 0)

    imshow(img)
    show()


img = imread('img/ants.png')
'''
r = (100,0,300,160)
pintarectangulo(img, r,)
'''
def delimitarHormiga(img,r,fondo):
    x1,y1,x2,y2 = r
    a,b,c,d = 0,0,0,0
    for x in range(x1,x2):
        for y in range(y1,y2):
            if tuple(img[y,x]) != fondo:
                a = x+1
                break
    for y in range(y1,y2):
        for x in range(x1,x2):
            if tuple(img[y,x]) != (255,255,255):
                b = y+1
                break
    for x in range(x2, x1, -1):
        for y in range(y2, y1, -1):
            if tuple(img[y, x]) != fondo:
                c = x
                break
    for y in range(y2, y1, -1):
        for x in range(x2, x1, -1):
            if tuple(img[y, x]) != (255, 255, 255):
                d = y
                break
    return c,d,a,b

r = (100,0,300,160)
#print(delimitarHormiga(img, r, (255,255,255)))

#pintarectangulo(img, (122, 19, 300, 153))

def rellenarectangulo(img, r, color):
    y1,x1,y2,x2 = r
    r,g,b = color
    img[x1:x2, y1:y2, 0] = r
    img[x1:x2, y1:y2, 1] = g
    img[x1:x2, y1:y2, 2] = b
    imshow(img)
    show()

rellenarectangulo(img, (122, 19, 300, 153), (100,25,50))