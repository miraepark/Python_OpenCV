# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 09:19:28 2017

@author: USER
"""

import cv2
img=cv2.imread('image.jpg',1)
img2=cv2.imread('image.jpg',0)
img3=cv2.imread('image.jpg',-1)
#cv2.imshow(윈도우창 title, cv2.imread()의 return)
cv2.imshow('image',img)
cv2.imshow('image2',img2)
cv2.imshow('image3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()



