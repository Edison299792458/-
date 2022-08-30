# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:04:24 2020

@author: 陳忨詠
"""

import matplotlib.pyplot as plt   #引進繪圖模組
import numpy as np                #引進numpy module


a=1
b=0.5



xx=[]   #設定list為x軸
tt=[]   #設定list為y軸
t=0     #角度從0到50
T=50
dt=0.0001  #設置迴圈讓角度從0每次加0.0001到50弧度


while t<=T:
    r=a+b*t          #阿基米德螺旋公式
    x=r*np.cos(t)    #x軸座標
    y=r*np.sin(t)    #Y軸座標
    xx.append(x)
    tt.append(y)
    t=t+dt
    
    
plt.plot(xx,tt)
plt.show()#畫出來吧!



