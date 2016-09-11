# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:40:31 2016

@author: Gustavo
"""

import win32api as wapi

class Mouse:
    def __init__(self):
        self._Width = wapi.GetSystemMetrics(0)
        self._Height = wapi.GetSystemMetrics(1)
        wapi.SetCursorPos((self.Width/2,self.Height/2))
        print('Executa o INIT')
        
    def SetPosAbsolut(Ax,Ay):
        wapi.SetCursorPos((Ax,Ay))
    
    def SetPosIncremental(Ix,Iy):
        mouse_Pos_x = wapi.GetCursorPos()[0]
        mouse_Pos_y = wapi.GetCursorPos()[1]
        wapi.SetCursorPos((mouse_Pos_x - Ix,mouse_Pos_y - Iy))
        
    def GetMousePos():
        return wapi.GetCursorPos()
        
    def GetWidth():
        return wapi.GetSystemMetrics(0)   
    
    def GetHeight():
        return wapi.GetSystemMetrics(1)