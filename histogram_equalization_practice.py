# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:21:58 2017

@author: USER
"""
## Histogram Equalization 
## 이미지의 히스토그램이 특정영역에 너무 집중되어 있으면 contrast가 낮아
## 좋은 이미지라고 할 수 없음 >> 따라서 전체영역에 골고루 분포가 되도록 하는 작업

"""
원리 : 이미지의 각 픽셀의 cumulative distribution function(cdf)값을 구하고
 Histogram Equalization 공식에 대입하여 0 ~ 255 사이의 값으로 변환 
 
 
"""
###Numpy를 이용하여 균일화 작업
#%%
import cv2
import numpy as np
from matplotlib import pyplot as plt
#%%
img=cv2.imread('wiki.jpg')


histogram=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histogram,color='r'), plt.xlim([0,256])
hist, bins = np.histogram(img.flatten(), 256,[0,256])

cdf = hist.cumsum()

# cdf의 값이 0인 경우는 mask처리를 하여 계산에서 제외
# mask처리가 되면 Numpy 계산에서 제외가 됨
# 아래는 cdf array에서 값이 0인 부분을 mask처리함
cdf_m = np.ma.masked_equal(cdf,0)

#History Equalization 공식
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

# Mask처리를 했던 부분을 다시 0으로 변환
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img1 = cdf[img]

plt.subplot(121),plt.imshow(img,'gray'),plt.title('Original')
plt.subplot(122),plt.imshow(img1,'gray'),plt.title('Equalization')

plt.show()

#%%
img2 = cv2.imread('wiki.jpg',0);

# OpenCV의 Equaliztion함수
img3 = cv2.equalizeHist(img2)
img2 = cv2.resize(img2,(400,400))
img3 = cv2.resize(img3,(400,400))

dst = np.hstack((img2, img3))
cv2.imshow('img2',dst)
cv2.waitKey()
cv2.destroyAllWindows()
