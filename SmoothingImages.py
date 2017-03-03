# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 10:36:01 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img2=cv2.imread('opencv-logo.png',1)

b, g, r= cv2.split(img2)
img = cv2.merge((r, g, b))

kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)

blur=cv2.blur(img,(5,5))

gblur=cv2.GaussianBlur(img,(5,5),0)

median=cv2.medianBlur(img,5)

bblur=cv2.bilateralFilter(img,9,75,75)

plt.subplot(2,3,1),plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,2),plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3),plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,4),plt.imshow(gblur), plt.title('GaussianBlurred')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5),plt.imshow(median), plt.title('medianBlurred')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,6),plt.imshow(bblur), plt.title('bilateralFilter')
plt.xticks([]), plt.yticks([])

plt.show()


##img2=노란색 이미지

