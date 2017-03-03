# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 11:36:03 2017

@author: USER
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('dave.jpg',0)

laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

images=[img, laplacian, sobelX, sobelY]
titles=['Original','Laplacian','Sobel X', 'Sobel Y']

for i in xrange[4]:
    plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
    