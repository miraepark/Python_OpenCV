#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread('detecttest_1.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#%%Rotated Rectangle
cnt=contours[1]
    
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], -1, (0,0,255), 2) # blue

cnt=contours[2]
    
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], -1, (0,0,255), 2) # blue


cnt=contours[3]
    
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], -1, (0,0,255), 2) # blue

cnt=contours[4]
    
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], -1, (0,0,255), 2) # blue
        
    
plt.imshow(img)

