from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show

img = imread('img/ants.png')
r = (100,0,300,160)

def encuentrapuntosupcolor(a,b,c,d, img, color):
    rojo,verde,azul = color
    for x in range(a, b):
        for y in range(c, d):
            if img[x,y,0] != rojo and img[x,y,1] != verde and img[x,y,2] != azul:
                return x
def ecuentrapuntinfcolor(a,b,c,d, img, color):
    rojo, verde, azul = color
    for x in reversed(range(a, b)):
        for y in range(c, d):
            if img[x,y,0] !=rojo and img[x,y,1] != verde and img[x,y,2] != azul:
                return x
def get_bb(img, rectang, color):
    xi, yi, xf, yf = rectang
    #ENCUENTRO PUNTO SUPERIOR
    #recorro desde el punto incial x1,y1 las x  hasta encontrar hormiga
    x1 = encuentrapuntosupcolor(xi, xf, yi, yf, img, color)
      # recorro desde el punto incial x1,y1 las y  hasta encontrar hormiga
    y1 = encuentrapuntosupcolor(yi, yf, xi, xf, img, color)
    # ENCUENTRO PUNTO INFERIOR
    # recorro desde el punto incial x2,y2 las x hacia la izquierda hasta encontrar hormiga
    x2 = ecuentrapuntinfcolor(xi, xf,yi,yf, img, color)
    # recorro desde el punto incial x1,y1 las y hacia arriba hasta encontrar hormiga
    y2 = ecuentrapuntinfcolor(yi,yf,xi,xf, img, color)
    print(x1, y1, x2, y2)
    img[y1:y2, x1] = (0,0,0)
    img[y1:y2, x2] = (0,0,0)
    img[y1, x1:x2] = (0,0,0)
    img[y2, x1:x2] = (0,0,0)
    imshow(img)
    return show()


print(get_bb(img, r, (255, 255, 255)))

