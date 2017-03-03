# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 13:29:44 2017

@author: USER
"""

import cv2

img=cv2.imread('image7.jpg')
cv2.imshow('imageshowing',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('savingtest2.jpg',img)
    cv2.destroyAllWindows()
    