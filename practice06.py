# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 10:22:14 2017

@author: USER
"""



import cv2
import numpy as np
from matplotlib import pyplot as plt
##img=cv2.imread('j.png', 0)

img=cv2.imread('image3.jpg',0)
plt.imshow(img,cmap='gray')
plt.show()

kernel=np.ones((5,5),np.uint8)

##두껍게해서  작은 Object를 제거하는 효과
erosion=cv2.erode(img,kernel,iterations=1)
plt.imshow(erosion,cmap='gray')
plt.show()

##대상을 확장한 후 작은 구멍을 채우는 방법
dilation=cv2.dilate(img,kernel,iterations=1)
plt.imshow(dilation,cmap='gray')
plt.show()

## Erosion적용 후 Dilation 적용/ 작은 object나 돌기제거에 적합
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
plt.imshow(opening,cmap='gray')
plt.show()

## Dilation적용 후 Erosion 적용. 전체적인 윤곽 파악에 적합
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
plt.imshow(closing,cmap='gray')
plt.show()

## 이미지의 edge를 검출하는 방법
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.imshow(gradient,cmap='gray')
plt.show()

## “top hat”. Opeining과 원본 이미지의 차이
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
plt.imshow(tophat,cmap='gray')
plt.show()
##  “black hat”. Closing과 원본 이미지의 차이
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
plt.imshow(blackhat,cmap='gray')
plt.show()

##색 반전
_,t = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#plt.imshow(t) >> 임의로 색깔을 정해 대비한 상태로 나타냄(여기서는 노랑과 보라)
plt.imshow(t,cmap='gray')
plt.show()



