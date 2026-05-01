from matplotlib.pyplot import imshow,show
from imageio import imread
import numpy as np

w = imread('weed2', 1)
imshow('image', w)
b, g, r = w
height = np.size(w, 0)
width = np.size(w, 1)
bw = np.zeros((height, width))

for i in range(1, height):
    for j in range(1, width):
        if (b[i, j] < g[i, j] and r[i, j] < g[i, j] and g[i, j] > 125):
            bw[i, j] = 1
imshow('Black and White image', bw)
kernel = np.ones((5, 5), np.uint8)
imshow('Eroded image', bw)
imshow('Final Image', bw)
show()