# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:09:06 2017

@author: USER
Line 그리기 

cv2.rectangle(img,(ix,iy),(x,y),(255,255,0),-1) #하늘색
             (이미지, 시작좌표, 종료좌표, BGR컬러, 선두)

(제곱값 구하기)
a^n  = a ** n
a^n = math.pow(a, n)

(루트값 구하기)
\sqrt x = x ** 0.5
\sqrt x = math.sqrt(x)

(두 점간의 거리 구하기)
math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2, y1),2))

(어떤 변수s를 다른 자료형으로 변환)
n = float(s) / n = str(s) / n = int(s) / n = long(s)
>>활용
ine_length=math.sqrt(math.pow((ix-x),2)+math.pow((iy-y),2))
value_str=str(line_length)

"""
#%%
import cv2
import numpy as np
import math

#초기값 지정
ix, iy=-1,-1

#%%[[1-1]] line 생성, console창에 띄우기
def draw_line(event, x, y, flags, param):
    global ix, iy

    if event==cv2.EVENT_LBUTTONDOWN:
        #그리기 시작
        ix, iy=x,y
        
    elif event==cv2.EVENT_LBUTTONUP: #왼쪽버튼 클릭시
         cv2.line(img,(ix,iy),(x,y),(255,255,255),10)
         line_length=math.sqrt(math.pow((ix-x),2)+math.pow((iy-y),2))

         print line_length
     
#%% [[1-2]] cv2창, console 두개 모두에 값 띄우기
## 아직 해결 못한 사항 : 글씨 위에 
#글씨가 겹쳐져서 사실상 안보임

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
         cv2.putText(img,value_str,(150,500),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
         
         
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
