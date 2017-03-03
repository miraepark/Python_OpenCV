# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
L=input("L : ")
ratio=input("ratio : ")
thick=input("thick : ")
"""
    
#%%
def triWave(L, ratio, thick = 1):
    global w,h

    w=L+100+thick
    h=(L*ratio*2)+thick+50
    print w,h
    
    img = np.zeros((h, w), np.uint8)    

    x1, y1 = 30, h/2
    x2, y2 = x1+L/3, y1+(ratio*L)
    x3, y3 = x1+(2*L)/3, y1-(ratio*L)
    x4, y4 = x1+L, y1
    print (x1,y1), (x2,y2), (x3,y3), (x4,y4)

    pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], np.int32)
    pts = pts.reshape((-1,1,2))
    img = cv2.polylines(img, [pts], False, 255, thick)
    
    plt.imshow(img)
    plt.show()

    return img

I = triWave(200, 0.2, 3)
