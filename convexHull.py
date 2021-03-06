# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:07:46 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('detecttest.png')
img1 = img.copy()
img2=img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1] # 1이 손모양 주변의 contour
rect=cv2.minAreaRect(cnt)
box=cv2.boxPoints(rect)
box=np.int0(box)

hull = cv2.convexHull(cnt)

cv2.drawContours(img1, contours, -1 ,(0,255,0), 3)
cv2.drawContours(img2, [box], -1 ,(0,255,0), 2)

titles = ['[Original]','[Convex Hull]','[rotated rectangle]']
images = [img, img1,img2]

for i in xrange(3):
    plt.subplot(2,2,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
