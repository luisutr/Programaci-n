from matplotlib.pyplot import imshow,show
from imageio import imread
color3 = (-50,50,50)
r = (100,0,300,160)
img = imread('img/ants.png')
def hl_rect(img,r,color3):
    c1= color3[0]
    c2= color3[1]
    c3= color3[2]
    a=img[0:160,100:300,0]
    print(a)
    b=img[0:160,100:300,1]
    c=img[0:160,100:300,2]
    for x in range(0,161):
        for y in range(100,301):
            if img[x,y,0] < 50:
                img[x,y,0]=50+c1
            else:
                img[x, y, 0] = img[x, y, 0] + c1
    #img[0:160,100:300,1]= (b + c2)
    for x in range(0,161):
        for y in range(100,301):
            if img[x,y,1] > 205:
                img[x,y,1]=205+c2
            else:
                img[x, y, 1] = img[x, y, 1] + c2
    #img[0:160,100:300,2]= (c + c3)
    for x in range(0,161):
        for y in range(100,301):
            if img[x,y,2] > 205:
                img[x,y,2]=205+c3
            else:
                img[x, y, 2] = img[x, y, 2] + c3
    imshow(img)
    return show()

hl_rect(img,r,color3)
