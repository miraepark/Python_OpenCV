#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('detecttest_1.png')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in range(1,len(contours)):
    cnt=contours[i]
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], -1, (0,0,255), 2) # blue
    # i를 텍스트 넘버로 하면 될 듯 합니다.
    text=repr(i)
    width,height=box[i-1]
    cv2.putText(img,text,(width-20,height-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

plt.imshow(img)

