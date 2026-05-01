## EJERCICIO 2

from matplotlib.pyplot import imshow,show
from imageio import imread

img = imread('img/ants.png')
r = (100,0,300,160)
color = (0,255,0)

def draw_rect(img,r,color):
    x1=r[0]
    x2=r[2]
    y1=r[1]
    y2=r[3]
    cv2.rectangle(img,(x1,y1),(x2,y2),(color),2)
    imshow(img)
    return show()