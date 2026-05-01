from matplotlib.pyplot import imshow,show
from imageio import imread

img = imread('ants.png')
def rgb_to_grayscale(img):
    height, width, channels = img.shape
    for x in range(height):
        for y in range(width):
            #0.299 R + 0.587 G + 0.114 B
            R,G, B = img[x,y]
            I = R*0.299+G*0.587+B*0.144
            img[x, y, 0] = I
            img[x, y, 1] = I
            img[x, y, 2] = I
    imshow(img)
    return show()

def filtro_binario(img, umbral):
    height, width, channels = img.shape
    for x in range(height):
        for y in range(width):
            if tuple(img[x, y]) <= umbral:
                img[x, y] = [255,255,255]
            else:
                img[x, y] = [0,0,0]
    imshow(img)
    return show()

print(filtro_binario(img, (127,127,127)))