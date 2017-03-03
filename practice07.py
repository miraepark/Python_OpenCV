# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 17:16:09 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

Image = cv2.imread('spaceimage.jpg')


kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

erosion = cv2.erode(Image,kernel,iterations = 1)
dilation = cv2.dilate(Image,kernel,iterations = 1)
opening = cv2.morphologyEx(Image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(Image, cv2.MORPH_CLOSE,kernel)
gradient = cv2.morphologyEx(Image, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(Image, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(Image, cv2.MORPH_BLACKHAT, kernel)

images =[Image, erosion, opening, dilation, closing, gradient, tophat, blackhat]
titles =['Image','Erosion','Opening','Dilation','Closing', 'Gradient', 'Tophat','Blackhot']

for i in xrange(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
