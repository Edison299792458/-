# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:04:24 2020

@author: 陳忨詠
"""

import matplotlib.pyplot as plt   #引進繪圖模組
import numpy as np                #引進numpy module


a=1
b=0.5



xx=[]
tt=[]
t=0
T=50
dt=0.0001


while t<=T:
    r=a+b*t
    x=r*np.cos(t)
    y=r*np.sin(t)
    xx.append(x)
    tt.append(y)
    t=t+dt
    
    
plt.plot(xx,tt)
plt.show()#畫出來吧!



