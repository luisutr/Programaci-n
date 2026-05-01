from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show

def get_bb(img, rectang, color):
    yi, xi, yf, xf = rectang
    x1,y1,x2,y2 = 0,0,0,0
    #ENCUENTRO PUNTO SUPERIOR
    #recorro desde el punto incial x1,y1 las x  hasta encontrar hormiga
    for x in range(xi, xf):
        if x1 == 0:
            for y in range(yi, yf):
                if tuple(img[x, y]) != color:
                    x1= x
      # recorro desde el punto incial x1,y1 las y  hasta encontrar hormiga
    for y in range(yi, yf):
        if y1 == 0:
            for x in range(xi, xf):
                if tuple(img[x, y])  != color:
                    y1 = y
    # ENCUENTRO PUNTO INFERIOR
    # recorro desde el punto incial x2,y2 las x hacia la izquierda hasta encontrar hormiga
    for x in reversed(range(xi, xf)):
        if x2 == 0:
            for y in reversed(range(yi, yf)):
                if tuple(img[x, y])  != color:
                    x2 = x+1
    # recorro desde el punto incial x1,y1 las y hacia arriba hasta encontrar hormiga
    y2 = encuentray2(xi,yi,xf,yf, img, color)

    return ((y1, x1, y2, x2))

def encuentray2(xi,yi,xf,yf, img, color):
    for y in reversed(range(yi, yf)):
            for x in reversed(range(xi, xf)):
                if tuple(img[x, y]) != color:
                    return  y+1

img = imread('img/ants.png')
rectang = (100,0,300,160)
print(get_bb(img, rectang, (255, 255, 255)))

