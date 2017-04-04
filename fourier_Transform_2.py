# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 09:16:56 2017

@author: USER
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('messi.jpg')
f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
magnitude_spectrum=20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('InputImage'), plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
plt.show()
#%%

