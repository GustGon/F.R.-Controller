# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
from Mouse import *

face_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_mouth.xml')
eye_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('C:\Gustavo\Git\F.R.-Controller\haarcascades\haarcascade_nariz.xml')


cap = cv2.VideoCapture(0)
Ms = Mouse()
#_blMarcar = False

class F_R_Controler(object):
    _blMarcar = False

    def comecar(self):
        self._blMarcar = True
        print(self._blMarcar)

    def parar(self):
        self._blMarcar = False
        print(self._blMarcar)
 
    def main(self): 
        IMPRECISAO = 10
        SENSIBILIDADE = 20
        T_RESPOSTA = 3
        delta_x = 0
        delta_y = 0
        x_inicial = 0
        y_inicial = 0
        x_atual = 0
        y_atual = 0
        olho_medio_x = 0
        olho_medio_y = 0
        i = 0

        try:
            while(True):
                ret, frame = cap.read()
                face = face_cascade.detectMultiScale(frame,1.5,5)
                for (x,y,w,h) in face:
                    
                    cv2.rectangle(frame, (x,y),(x + w,y + h),(255,0,0),2)
                    olho = eye_cascade.detectMultiScale(frame,1.3,6)  
                    if(len(olho)):
                        olho_direito_x = olho[0][0]
                        olho_direito_y = olho[0][1]
                    if(len(olho) > 1):
                        olho_esquerdo_x = olho[1][0]
                        olho_esquerdo_y = olho[1][1]
                    if(olho_direito_x and olho_esquerdo_x and olho_direito_y and olho_esquerdo_y):
                        olho_medio_x = (olho_direito_x + olho_esquerdo_x)/2
                        olho_medio_y = (olho_direito_y + olho_esquerdo_y)/2
                        x_atual = olho_medio_x
                        y_atual = olho_medio_y
                        delta_x = x_inicial - x_atual
                        delta_y = y_inicial - y_atual
                        olho_esquerdo_x = olho_esquerdo_y = olho_direito_x = olho_direito_y = 0
                    if(x_inicial == 0 and y_inicial == 0 and self._blMarcar == True):
                        x_inicial = olho_medio_x
                        y_inicial = olho_medio_y
                    elif(self._blMarcar == False):
                        x_inicial = y_inicial = 0
                    for (ex,ey,ew,eh) in olho:
                        cv2.rectangle(frame, (ex,ey),(ex + ew,ey + eh),(0,0,255),2)
                print('''
                Inicial x = {0}
                Inicial y = {1}
                Delta x = {2}
                Delta y = {3} 
                x atual = {4}
                y atual = {5}
                '''.format(x_inicial + IMPRECISAO,y_inicial + IMPRECISAO,delta_x,
                           delta_y,x_atual,y_atual))

                if(self._blMarcar == True):
                    
                    if((olho_esquerdo_x and olho_esquerdo_y) and (not olho_direito_x and not olho_direito_y)):
                            Ms.LeftClick()
                            
                    elif((olho_direito_x and olho_direito_y) and (not olho_esquerdo_x and not olho_esquerdo_y)):
                        if(i > T_RESPOSTA):
                            Ms.LeftClick()
                            i = 0
                        else:
                            i += 1
                            
                    if(delta_x > IMPRECISAO):
                        Ms.SetPosIncremental(SENSIBILIDADE,0)
                        
                    elif(delta_x < -IMPRECISAO):
                        Ms.SetPosIncremental(-SENSIBILIDADE,0)
                        
                    if(delta_y > IMPRECISAO):
                        Ms.SetPosIncremental(0,SENSIBILIDADE)
                        
                    elif(delta_y < -IMPRECISAO):
                        Ms.SetPosIncremental(0,-SENSIBILIDADE)
                        
                    
                cv2.imshow('F.R. Controler',frame)
                if cv2.waitKey(33) == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        
        except:
            cap.release()
            cv2.destroyAllWindows()
