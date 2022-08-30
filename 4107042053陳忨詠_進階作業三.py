# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:14:31 2019

@author: 陳忨詠
"""

import numpy as np      #引入numpy及sympy模組
import matplotlib.pyplot as plt   #引進繪圖模組

G=1
M=1
m=1



m=[1,1]

p1=[-1,0]  #(-1,0)的起始位置
p2=[1,0]   #(1,0)的起始位置
v1=[0,-0.5]#(-1,0)的起始速度
v2=[0,0.5]#(1,0)的起始速度

dt=0.001
t=0
T=10
times=0

def a(x1,y1,x2,y2):         #計算在不同位置的加速度
    dr=[p2[0]-p1[0],p2[1]-p1[1]]
   
    R=((dr[0])**2+(dr[1])**2)**0.5
    cos=dr[0]/R
    sin=dr[1]/R
    
    ac1=G*m[1]/R**2
    ax1=ac1*cos
    ay1=ac1*sin
    
    ac2=G*m[0]/R**2
    ax2=-ac2*cos
    ay2=-ac2*sin
    
    return [ax1,ay1,ax2,ay2]



xx1=[]   #設置list紀錄軌跡
yy1=[]
xx2=[]
yy2=[]
tt=[]

while t<T:             #利用疊代法計算位置
    xx1.append(p1[0])  
    yy1.append(p1[1])
    xx2.append(p2[0])
    yy2.append(p2[1])
    tt.append(t)
    
    
    A=a(x1,y1,x2,y2)
    v1[0]=v1[0]+A[0]*dt
    v1[1]=v1[1]+A[1]*dt
    v2[0]=v2[0]+A[2]*dt
    v2[1]=v2[1]+A[3]*dt
    
    p1[0]=p1[0]+v1[0]*dt
    p1[1]=p1[1]+v1[1]*dt
    p2[0]=p2[0]+v2[0]*dt
    p2[1]=p2[1]+v2[1]*dt
    
    
    t=t+dt
    
plt.plot(xx1,yy1,xx2,yy2)

    
    
    
    
    
    
m=[1,2]

p1=[-2,0]  #(-2,0)的起始位置
p2=[1,0]   #(1,0)的起始位置
v1=[0,-0.6666]#(-1,0)的起始速度
v2=[0,0.33333]#(1,0)的起始速度

dt=0.001
t=0
T=100
times=0

def a(x1,y1,x2,y2):         #計算在不同位置的加速度
    dr=[p2[0]-p1[0],p2[1]-p1[1]]
   
    R=((dr[0])**2+(dr[1])**2)**0.5
    cos=dr[0]/R
    sin=dr[1]/R
    
    ac1=G*m[1]/R**2
    ax1=ac1*cos
    ay1=ac1*sin
    
    ac2=G*m[0]/R**2
    ax2=-ac2*cos
    ay2=-ac2*sin
    
    return [ax1,ay1,ax2,ay2]



xx1=[]   #設置list紀錄軌跡
yy1=[]
xx2=[]
yy2=[]
tt=[]

while t<T:             #利用疊代法計算位置
    xx1.append(p1[0])  
    yy1.append(p1[1])
    xx2.append(p2[0])
    yy2.append(p2[1])
    tt.append(t)
    
    
    A=a(x1,y1,x2,y2)
    v1[0]=v1[0]+A[0]*dt
    v1[1]=v1[1]+A[1]*dt
    v2[0]=v2[0]+A[2]*dt
    v2[1]=v2[1]+A[3]*dt
    
    p1[0]=p1[0]+v1[0]*dt
    p1[1]=p1[1]+v1[1]*dt
    p2[0]=p2[0]+v2[0]*dt
    p2[1]=p2[1]+v2[1]*dt
    
    
    t=t+dt
    
plt.plot(xx1,yy1,xx2,yy2)
   










    
    