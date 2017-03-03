# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:01:53 2017

@author: USER
contours line위 도형 그리기
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('convexHull.jpg')
img1=img.copy()
img2=img.copy()
img3=img.copy()
img4=img.copy()
img5=img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1] # 1이 손모양 주변의 contour

#%% Straight Rectangle
x, y, w, h = cv2.boundingRect(cnt)
img1 = cv2.rectangle(img1,(x,y),(x+w, y+h),(0,255,0), 3) # green
img5 = cv2.rectangle(img5,(x,y),(x+w, y+h),(0,255,0), 3) # green

plt.imshow(img1)

#%%Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img2 = cv2.drawContours(img2, [box], 0, (0,0,255), 3) # blue
img5 = cv2.drawContours(img5, [box], 0, (0,0,255), 3) # blue

plt.imshow(img2)

#%%Minimum Enclosing Circle
(x,y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img3 = cv2.circle(img3, center, radius,(255,255,0),3) # yellow
img5 = cv2.circle(img5, center, radius,(255,255,0),3) # yellow

plt.imshow(img3)

#%%Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
img4 = cv2.ellipse(img4, ellipse,(255,0,0),3) #red
img5 = cv2.ellipse(img5, ellipse,(255,0,0),3) #red

plt.imshow(img4)

#%%
titles=['Original','Straight Rectangle', 'Rotated Rectangle', 'Enclosing Circle', 'Ellipse', 'All']
images=[img,img1,img2,img3,img4,img5]

for i in xrange(6):
    plt.subplot(2,3,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

