# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
def triWave(L,thick,ratio):
    global w,h
    
    thick=input("thick : ")
    L=input("L : ")
    ratio=input("ratio : ")
    
    w=L+100+thick
    h=(L*ratio*2)+thick+50
    print w,h
    
img = np.zeros((h, w), np.uint8)    

#%%+x,y 좌표 계산 함수
x1, y1 = 30, h/2
x2, y2 = x1+(ratio*L/3), y1+(ratio*L)
#x2=x1+L/3, x3=x1+2L/3으로 할 경우에는 보기 힘듬(원하는 코드가 안나와서 ratio 곱함)
x3, y3 = x1+(ratio*2L/3), y1-(ratio*L)
x4, y4 = x1+L, y1
print (x1,y1), (x2,y2), (x3,y3), (x4,y4)

pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img, [pts], False, 255, thick)

plt.imshow(img)
plt.show()
#%%original source
thick=5
h=50
w=100
img=np.zeros((h,w),np.uint8)

x1,y1=10,5
x2,y2=20,30
x3,y3=70,20
x4,y4=50,10

pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img, [pts], False, 255, thick)

plt.imshow(img)
