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
        wapi.SetCursorPos((int(self._Width/2),int(self._Height/2)))
        print("Executa o INIT")
        
    def SetPosAbsolut(self,Ax,Ay):
        wapi.SetCursorPos((Ax,Ay))
    
    def SetPosIncremental(self,Ix,Iy):
        mouse_Pos_x = wapi.GetCursorPos()[0]
        mouse_Pos_y = wapi.GetCursorPos()[1]
        wapi.SetCursorPos((mouse_Pos_x + Ix,mouse_Pos_y - Iy))
        
    def GetMousePosX(self):
        return wapi.GetCursorPos()[0]
        
    def GetMousePosY(self):
        return wapi.GetCursorPos()[1]
        
    def GetWidth(self):
        return wapi.GetSystemMetrics(0)   
    
    def GetHeight(self):
        return wapi.GetSystemMetrics(1)