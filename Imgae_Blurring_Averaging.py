# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 09:07:38 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#imgframe이 empty임
img=cv2.imread('opencv_logo.png',1)
#blur=cv2.blur(img,(5,5))

kernel=np.ones((5,5),np.float32)/25
dst=cv2.filter2D(img,-1,kernel)

blur2=cv2.blur(img,(5,5))

plt.subplot(121),plt.imshow(img2), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur2), plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.show()
