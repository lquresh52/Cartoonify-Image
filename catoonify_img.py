# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:37:50 2020

@author: IAQMH
"""
import cv2

import os

def cartoonify(img_rgb):    
    numBilateralFilters = 4
    img_color = img_rgb
    #cv2.imshow("Quresh_img.png",img_color)

    for _ in range(numBilateralFilters):
          img_color = cv2.bilateralFilter(img_color, 15, 30, 20)
          cv2.imshow('in for',img_color)
          cv2.waitKey(1000)
    
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    img_blur = cv2.medianBlur(img_gray, 7)

    cv2.imshow('Blur img',img_blur)
    cv2.waitKey(1000)
    img_edge = cv2.adaptiveThreshold(img_blur, 235,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)

    cv2.imshow('Img edge',img_edge)
    cv2.waitKey(1000)
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

    return cv2.bitwise_and(img_color, img_edge)

real_inputs = []
cartoon_outputs = []

img_rgb = cv2.imread("hunaid.jpeg")
# img_rgb = cv2.resize(img_rgb, (600, 500))
cv2.imshow('Img', img_rgb)
cv2.waitKey(1000)

output = cartoonify(img_rgb)

real_inputs.append(img_rgb)

cartoon_outputs.append(output)

cv2.imshow('Final Output',output)
cv2.waitKey(1000)
cv2.imwrite('hunaid_cartoon.jpg',output)