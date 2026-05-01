from matplotlib.pyplot import imshow,show
from imageio import imread

img = imread('img/ants.png')

def get_mask(img, color):
    img = imread('img/ants.png')
    height, width, channels = img.shape
    r = (0,0,width,height)
    xi = r[0]
    yi = r[1]
    xf = r[2]
    yf = r[3]
    for x in range(xi, xf):
        for y in range(yi, yf):
            print(img[y, x])
            if tuple(img[y, x]) == color:
                img[y,x] = 0
            else:
                img[y,x] = 255
    imshow(img)
    return show()

#get_mask(img, (255,255,255))

