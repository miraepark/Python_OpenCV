# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 10:16:20 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE=[255,0,0]

img1=cv2.imread('spaceimage.jpg')

replicate=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('original')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')

plt.show()
