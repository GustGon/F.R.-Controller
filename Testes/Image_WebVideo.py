# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_frontalface_default.xml')
left_eye_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_righteye_2splits.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_nariz.xml')

cap = cv2.VideoCapture(0)
x_maior = 0
x_menor = 1200
y_maior = 0
y_menor = 1200


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(frame,1.5,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y),(x + w,y + h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_frame = frame[y:y+h, x:x+w]
#        nariz = nose_cascade.detectMultiScale(frame,1.3,6)
 #       for (nx,ny,nw,nh) in nariz:
  #          cv2.rectangle(frame, (nx,ny),(nx + nw,ny + nh),(0,0,255),2)
        olho = eye_cascade.detectMultiScale(frame,1.3,6)
        if(olho[0][0] != 0):
            x_atual = olho[0][0]
            y_atual = olho[0][1]
            if(x_atual > x_maior):
                x_maior = x_atual
            elif(x_atual < x_menor):
                x_menor = x_atual
            if(y_atual > y_maior):
                y_maior = y_atual
            elif(y_atual < y_menor):
                y_menor = y_atual
       # for (ex,ey,ew,eh) in olho:
        #    cv2.rectangle(frame, (ex,ey),(ex + ew,ey + eh),(0,255,0),2)
        print(x_maior,x_menor,y_maior,y_menor )

    # Display the resulting frame
    
    cv2.imshow('F.R. Controler',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#cam = 'http://192.168.0.83:4747/mjpegfeed'
#cam = 'http://192.168.0.83:8080/shot.jpg'