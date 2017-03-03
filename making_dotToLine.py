# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:20:13 2017

@author: USER
"""

import cv2
import numpy as np
import math

#초기값 지정
ix, iy=-1,-1

#%%
def draw_dotToLine(event, x, y, flags, param):
    global ix,iy
    
    if event==cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
        
    elif event==cv2.EVENT_LBUTTONUP:
        cv2.line(img,(ix,iy),(x,y),(255,255,255),10)

#%%
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('Dot_To_Line')
cv2.setMouseCallback('Dot_To_Line',draw_dotToLine)

while(1):
    cv2.imshow('Dot_To_Line',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:     #ESC키
        break

cv2.destroyAllWindows()
