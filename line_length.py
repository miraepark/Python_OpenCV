# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np
import math

#초기값 지정
ix, iy=-1,-1

#%% [[1-3]] 선 바로 밑에 띄우기
def draw_line(event, x, y, flags, param):
    global ix, iy
    

    if event==cv2.EVENT_LBUTTONDOWN:
        #그리기 시작
        ix, iy=x,y
        
    elif event==cv2.EVENT_LBUTTONUP: #왼쪽버튼 클릭시
         cv2.line(img,(ix,iy),(x,y),(255,255,255),10)
         line_length=math.sqrt(math.pow((ix-x),2)+math.pow((iy-y),2))

         
         value_str=str(line_length)
         print line_length
         cv2.putText(img,value_str,(ix+30,iy+30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),1)
         
        
         
         #cv2.putText(img,'Check Line Length in IPython console',(10,500),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)

#%%
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('MakingLine')
cv2.setMouseCallback('MakingLine',draw_line)

## 선 여러개 그리
while(1):
    cv2.imshow('MakingLine',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:     #ESC키
        break
    
cv2.destroyAllWindows()
