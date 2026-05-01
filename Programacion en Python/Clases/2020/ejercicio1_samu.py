from imageio import imread, imwrite
from matplotlib.pyplot import imshow, figure, show


def get_bb(img, rectang, color):
    yi, xi, yf, xf = rectang
    x1 = 0
    y1 = 0
    x = xi
    y = yi
    while x < xf and x1 == 0:
        x += 1
        for y in range(yi, yf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                x1 = x
    while y < yf and y1 == 0:
        y += 1
        for x in range(xi, xf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                y1 = y

    x2 = 0
    y2 = 0
    x = xf
    while x > xi and x2 == 0:
        x -= 1
        for y in range(yi, yf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                x2 = x
    y = yf
    while y >= yi and y2 == 0:
        y -= 1
        for x in range(xi, xf):
            if img[x, y, 0] != 255 and img[x, y, 1] != 255 and img[x, y, 2] != 255:
                y2 = y

    return (y2, x2, y1, x1)


img = imread('img/ants.png')
r = (100, 0, 300, 160)
print(get_bb(img, r, (255, 255, 255)))

#(122, 19, 300, 153)