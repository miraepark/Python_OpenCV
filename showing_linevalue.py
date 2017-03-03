# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:36:22 2017

@author: USER
"""

import cv2
import math
import numpy as np

img=np.zeros((512,512,3),np.uint8)
ix=100
iy=100
x=400
y=100
        

cv2.line(img,(ix,iy),(x,y),(255,255,255),5)

line_length=math.sqrt(math.pow((ix-x),2)+math.pow((iy-y),2))
#### float변수(line_length)를 str변수(value_str)로 변경해보기
value_str=str(line_length)
cv2.putText(img,value_str,(10,500),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

cv2.imshow('TakingLineValue',img)
cv2.waitKey(0)
cv2.destroyAllWindows()