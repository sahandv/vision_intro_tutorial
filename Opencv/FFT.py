#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:58:25 2019

@author: github.com/sahandv
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read images
img = cv2.imread('1.jpg',0)
img2 = cv2.imread('2.jpg',0)

img3 = cv2.imread('3.jpg',0)
img4 = cv2.imread('4.jpg',0)

img5 = cv2.imread('5.jpg',0)
img6 = cv2.imread('6.jpg',0)

#Transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

f2 = np.fft.fft2(img2)
fshift2 = np.fft.fftshift(f2)
magnitude_spectrum2 = 20*np.log(np.abs(fshift2))

f3 = np.fft.fft2(img3)
fshift3 = np.fft.fftshift(f3)
magnitude_spectrum3 = 20*np.log(np.abs(fshift3))

f4 = np.fft.fft2(img4)
fshift4 = np.fft.fftshift(f4)
magnitude_spectrum4 = 20*np.log(np.abs(fshift4))

f5 = np.fft.fft2(img5)
fshift5 = np.fft.fftshift(f5)
magnitude_spectrum5 = 20*np.log(np.abs(fshift5))

f6 = np.fft.fft2(img6)
fshift6 = np.fft.fftshift(f6)
magnitude_spectrum6 = 20*np.log(np.abs(fshift6))


#Plot
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img2, cmap = 'gray')
plt.subplot(224),plt.imshow(magnitude_spectrum2, cmap = 'gray')
plt.show()


plt.subplot(221),plt.imshow(img3, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum3, cmap = 'gray')
plt.title('Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img4, cmap = 'gray')
plt.subplot(224),plt.imshow(magnitude_spectrum4, cmap = 'gray')
plt.show()


plt.subplot(221),plt.imshow(img5, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum5, cmap = 'gray')
plt.title('Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img6, cmap = 'gray')
plt.subplot(224),plt.imshow(magnitude_spectrum6, cmap = 'gray')
plt.show()

