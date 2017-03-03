
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 10:36:01 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('opencv-logo.png',1)

kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)

plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122), plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])

plt.show()


##img2=노란색 이미지

