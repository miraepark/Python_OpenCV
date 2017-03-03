# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 09:50:29 2017

@author: USER
"""

import cv2
from matplotlib import pyplot as plt 

img=cv2.imread('image.jpg',1)


##matplotlib은 RGB,OpenCV는 BGR사용하므로 바꿔줘야 원본색상 나타
b,g,r=cv2.split(img)
img2=cv2.merge([r,g,b])

plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()