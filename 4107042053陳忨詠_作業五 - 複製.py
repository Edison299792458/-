# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 22:16:05 2019

@author: 陳忨詠
"""

import matplotlib.pyplot as plt   #引進繪圖模組
import numpy as np                #引進numpy module


x=2
v=0
m=2


k=8*np.pi**2  

xx=[]
tt=[]
t=0
T=3
dt=0.0001


while t<=T:
    x=x+v*dt
    a=-k*x/m
    v=v+a*dt
    xx.append(x)
    tt.append(t)
    t=t+dt
    
plt.plot(tt,xx)
plt.show()#畫出來吧!

xx1=[]
xx2=[]
tt1=[]
tt2=[]
x1=2
x2=2
v1=0
v2=0
t1=0
t2=0
T1=10


while t1<=T1:
    x1=x1+v1*dt
    a1=-k*x1/m-5*v1/m     #臨界阻尼算出來大概是25.1 欠阻尼只要選比25.1小即可
    v1=v1+a1*dt
    xx1.append(x1)
    
    tt1.append(t1)
    t1=t1+dt
    
plt.plot(tt1,xx1)


while t2<=T1:
    x2=x2+v2*dt
    a2=-k*x2/m-26*v2/m  #臨界阻尼算出來大概是25.1 阻尼只要選比25.1大即可
    v2=v2+a2*dt
    xx2.append(x2)
    
    tt2.append(t2)
    t2=t2+dt
    
plt.plot(tt2,xx2)
plt.show()#畫出來吧!



xx3=[]
xx4=[]
tt3=[]
tt4=[]
x3=0
x4=0
v3=0
v4=0
t3=0
t4=0
T1=10
A=100   #看助教例子震幅為3就設定A0=100





while t3<=T1:
    x3=x3+v3*dt
    a3=-k*x3/m-10*v3/m+A*np.cos(2*np.pi*t3)
    v3=v3+a3*dt
    xx3.append(x3)
    
    tt3.append(t3)
    t3=t3+dt
    
plt.plot(tt3,xx3)


while t4<=T1:
    x4=x4+v4*dt
    a4=-k*x4/m-10*v4/m+A*np.cos(2*np.pi*0.1*t4)
    v4=v4+a4*dt
    xx4.append(x4)
    
    tt4.append(t4)
    t4=t4+dt
    
plt.plot(tt4,xx4)






    