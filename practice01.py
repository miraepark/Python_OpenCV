# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 14:31:59 2017

@author: USER
"""

"""
p.31~
import cv2
import numpy as np

#mouse callback function

def draw_circle(event, x, y, flags, param):
    if event ==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF==27:
        break

cv2.destroyAllWindows()
"""

import cv2
import numpy as np

drawing=False  #true if mouse is pressed
mode=True  #if True, draw rectangel. press 'm' to toggle to curve
ix, iy=-1,-1

#mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    
    if event==cv2.EVENT_LBUTTONDOWN:
        #그리기 시작
        drawing =True
        ix, iy=x,y
        
    elif event==cv2.EVENT_RBUTTONUP: #오른쪽버튼클릭
        drawing=True
        if mode==True:
            cv2.rectangle(img, (ix,iy),(x,y),(0,255,0),-1) #초록색
        else : 
            cv2.circle(img,(x,y),50,(0,0,255),-1) #빨간색 계속생김(이동할때 따라다님)
                
    elif event==cv2.EVENT_RBUTTONDBLCLK:    #오른쪽버튼 더블클릭
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)   #파란색
        else:
            cv2.circle(img,(x,y),100,(0,255,255),-1) #노란색
            
    elif event==cv2.EVENT_LBUTTONUP: #왼쪽버튼 클릭시
        drawing=True
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,255,0),-1) #하늘색
        else:
            cv2.circle(img,(x,y),10,(255,0,255),-1) #분홍색

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('circle and rectangle')
cv2.setMouseCallback('circle and rectangle',draw_circle)

while(1):
    cv2.imshow('circle and rectangle',img)
    k=cv2.waitKey(1) & 0xFF
    if k==ord('m'):
        mode=not mode
    elif k==27:     #ESC키
        break
    
cv2.destroyAllWindows()

            
                
                    
        

