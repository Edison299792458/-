# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:32:23 2020

@author: 陳忨詠
"""

import numpy as np
from matplotlib import pyplot as plt, animation as ani

f=plt.figure(facecolor='white')



x=-4     #設定題目所給的參數
y=0
vx=1
vy=0
k=1
m=1




xx=[]   #設定x軸軌跡的list
yy=[]   #設定y軸軌跡的list
t=0

dt=0.1


while x<=4 :     
    x=x+vx*dt           #用迴圈得到正電荷的的軌跡
    y=y+vy*dt
    r=((x)**2+(y+2)**2)**0.5
    cos=x/r
    sin=y+2/r
    a=1/r**2
    vx=vx+a*cos*dt
    vy=vy+a*sin*dt
    xx.append(x)
    yy.append(y)
    t=t+dt
    



x2=-4                  #設定負電荷的參數
y2=0
vx2=1
vy2=0
k=1
m=1




xx2=[]       #設定負電荷x軸軌跡的list
yy2=[]       #設定鄭電荷y軸軌跡的list
t=0

dt=0.1


while x2<=4 :         #用迴圈得到負電荷的的軌跡
    x2=x2+vx2*dt
    y2=y2+vy2*dt
    r=((x2)**2+(y2+2)**2)**0.5
    cos=x2/r
    sin=y2+2/r
    a=-1/r**2
    vx2=vx2+a*cos*dt
    vy2=vy2+a*sin*dt
    xx2.append(x2)
    yy2.append(y2)
    t=t+dt



def fun(fram):                        #定義動畫
    plt.clf()
    plt.xlim(-4,4)                #範圍
    plt.ylim(-5,5)
    plt.scatter(xx[fram],yy[fram],c='r')
    plt.scatter(xx2[fram],yy2[fram],c='b')
    plt.scatter(0,-2,c='r')            #固定的電荷所在的位置

animate=ani.FuncAnimation(fig=f,func=fun,interval=1,frames=100,repeat=False)  

