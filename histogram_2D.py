# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:47:56 2017

@author: USER

2D Histogram 분석
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('histogramimg.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
# X축은 Saturation, Y축은 Hue값
#HSV모델에서 H가 100이면 하늘색/ H값이 25이면 노란색
plt.imshow(hist) #, interpolation='nearest')
plt.show()
