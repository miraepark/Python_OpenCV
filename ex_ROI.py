# -*- coding: utf-8 -*-
"""
ex_ROI.py
Created on Tue Feb 07 13:53:27 2017

@author: USER
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread('messi.jpg')
ball = im[280:336, 330:400]

im[180:236, 230:300]=ball

plt.imshow(im)
plt.show()
