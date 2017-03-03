# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt 
import numpy as np

import cv2

#imae의 경로
#path = 'C:\Users\USER\Desktop\SampleData\\'
#경로안의 파일명을 읽어들여 사진 불러오기
#변수명=cv2.imread('이미지파일명.확장자',0(흑백)/1...2....3... > 그림 색상정보)
img = cv2.imread('image5.JPG',0)

"""
#ipython console창에 띄우기(그래프 같이나)
plt.imshow(img)
plt.show()
"""

#B라는 창에 윈도우 표준크기 또는 크기를 가로500/세로700로 나타냄
cv2.imshow('ImageShowing', img[:,:,0])
cv2.namedWindow('ImageShowing', cv2.WINDOW_NORMAL)
cv2.waitKey(0)
cv2.imwrite('savingtest1.jpg',img)
