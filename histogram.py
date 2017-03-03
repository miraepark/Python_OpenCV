# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:50:53 2017

@author: USER
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1=cv2.imread('landscape2.jpg')


#calcHist(이미지, 채널, 마스크, 히스트사이즈, 범위, 히스트,accumulate)
##accumulate가 0,255 / 0,256
hist=cv2.calcHist([img1],[0],None,[255],[0,256])
comparehist=cv2.calcHist([img1],[0],None,[255],[0,255])

comparehist1=cv2.calcHist([img1],[1],None,[255],[0,256])
comparehist2=cv2.calcHist([img1],[2],None,[255],[0,256])

plt.figure()
plt.plot(hist)              #파란색
plt.plot(comparehist)        #노란색
plt.plot(comparehist1)        #초록색
plt.plot(comparehist2)          #빨간
