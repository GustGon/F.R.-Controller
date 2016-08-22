# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np

img = cv2.imread('Imagens\cidade_teste.jpg',cv2.IMREAD_COLOR)

cv2.line(img, (50,50), (150,150), (0,255,0),8)

cv2.imshow('CITY',img)
print(img.size)
cv2.waitKey(0)
cv2.destroyAllWindows()
