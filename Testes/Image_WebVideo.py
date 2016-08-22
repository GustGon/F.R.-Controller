# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np
import time
#cam = 'http://192.168.0.83:4747/mjpegfeed'
cam = 'http://192.168.0.83:8080/shot.jpg'
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.imshow('Video',frame)

    if cv2.waitKey(0) & 0xFF == ord('c'):
        break
    time.slep(1)
    
cap.release()
cv2.destroyAllWindows()