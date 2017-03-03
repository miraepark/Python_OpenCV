# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 10:13:23 2017

@author: USER
"""
"""
import cv2
import numpy as np

img=cv2.imread('messi5.jpg')

res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

#OR

height,width=img.shape[:2]
res=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
"""

import cv2
import numpy as np

img=cv2.imread('messi5.jpg',0)
rows,cols=img.shape

N=np.float32([[1,0,100],[0,1,50]])
dst2=cv2.warpAffine(img,N,(cols,rows))

cv2.imshow('img',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()


M=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
