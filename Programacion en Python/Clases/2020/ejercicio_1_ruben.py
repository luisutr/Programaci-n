from imageio import imread, imwrite

def get_bb(img, retang, color):
    yi, xi, yf, xf = retang
    x1, y1, x2, y2 = 0, 0, 0, 0
    for x in range(xi, xf):
        if x1 == 0:
            for y in range(yi, yf):
                if img[x, y, 0] != color[0] and img[x, y, 1] != color[1] and img[x, y, 2] != color[2]:
                    x1 = x
    for y in range (yi, yf):
        if y1 == 0:
            for x in range(xi, xf):
                if img[x, y, 0] != color[0] and img[x, y, 1] != color[1] and img[x, y, 2] != color[2]:
                    y1 = y
    for x in reversed(range(xi, xf)):
        if x2 ==  0:
            for y in reversed(range(yi, yf)):
                if img[x, y, 0] != color[0] and img[x, y, 1] != color[1] and img[x, y, 2] != color[2]:
                    x2 = x+1
    for y in reversed(range(yi, yf)):
        if y2 == 0:
            for x in reversed(range(xi, xf)):
                if img[x, y, 0] != color[0] and img[x, y, 1] != color[1] and img[x, y, 2] != color[2]:
                    y2 = y+1
    return ((y1,x1,y2,x2))

img = imread('img/ants.png')
r = (100,0,300,160)
print(get_bb(img, r, (255, 255, 255)))

