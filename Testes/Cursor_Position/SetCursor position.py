import win32api
import time
import math

for i in range(500):
   x = int(500+math.sin(math.pi*i/100)*500)
   y = int(500+math.cos(i)*100)
   win32api.SetCursorPos((x,y))
