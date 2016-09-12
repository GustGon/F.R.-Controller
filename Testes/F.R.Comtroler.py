# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
from Mouse import *

face_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_mouth.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_nariz.xml')


cap = cv2.VideoCapture(0)
Ms = Mouse



def main():
    IMPRECISAO = 5
    LIMITE = 20
    x_anterior = 0
    y_anterior = 0
    delta_x = 0
    delta_y = 0
    x_inicial = 0
    y_inicial = 0
    try:
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = face_cascade.detectMultiScale(frame,1.5,5)
            for (x,y,w,h) in face:
                cv2.rectangle(frame, (x,y),(x + w,y + h),(255,0,0),2)
                #roi_gray = gray[y:y+h, x:x+w]
                #roi_frame = frame[y:y+h, x:x+w]
                
                olho = eye_cascade.detectMultiScale(frame,1.3,6)
                for (x,y,w,h) in olho:
                    cv2.rectangle(frame, (x,y),(x + w,y + h),(255,0,0),2)
                    if(x_inicial == 0 and y_inicial == 0):
                        x_inicial = x
                        y_inicial = y
                    x_atual = x
                    y_atual = y
                    delta_x = x_inicial - x_atual 
                    delta_y = y_inicial - y_atual 
                    x_anterior = x_atual
                    y_anterior = y_atual
                    
                print('''
                Inicial x = {0}
                Inicial y = {1}
                Delta x = {2}
                Delta y = {3} 
                x atual = {4}
                y atual = {5}
                '''.format(x_inicial,y_inicial,delta_x,delta_y,x_atual,y_atual))
                
                if (delta_x > 0):
                    if(delta_x - IMPRECISAO < delta_x < delta_x + LIMITE):
                        x_pos = int(Ms.GetHeight()*0.05*delta_x)
                elif(delta_x < 0):
                   if(delta_x - IMPRECISAO > delta_x > delta_x + LIMITE):
                        x_pos = int(Ms.GetHeight()*0.05*delta_x)
                   
                if (delta_y > 0):
                    if(delta_y - IMPRECISAO < delta_y < delta_y + LIMITE):
                        y_pos = int(Ms.GetHeight()*0.05*delta_y)
                elif(delta_y < 0):
                   if(delta_y - IMPRECISAO > delta_y > delta_y + LIMITE):
                        y_pos = int(Ms.GetHeight()*0.05*delta_y)
                   
                   Ms.SetPosIncremental(x_pos,0)
                if(delta_y != 0):
                    y_pos = int(Ms.Mouse.GetWidth()*0.05)
                    Ms.SetPosIncremental(0,y_pos)
                
           
            # Display the resulting frame
            
            cv2.imshow('F.R. Controler',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    
    except IndexError:
         # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        
    
if __name__ == '__main__':
    main()
    
    