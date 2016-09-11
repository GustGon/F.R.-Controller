# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:40:31 2016

@author: Gustavo
"""

import win32api as wapi
        

print ("Width =", wapi.GetSystemMetrics(0))
print ("Height =", wapi.GetSystemMetrics(1))
mouse.SetCursorPos((800,50))
