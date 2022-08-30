# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:22:20 2020

@author: 陳忨詠
"""

import numpy as np
from matplotlib import pyplot as plt, animation as ani

f=plt.figure(facecolor='white')





x=-4
y=0
vx=1
vy=0
k=1
m=1




xx=[]
yy=[]
t=0

dt=0.01


while x<=4 :
    x=x+vx*dt
    y=y+vy*dt
    r=((x)**2+(y-(-2)**2)**0.5
    cos=x/r
    sin=y+2/r
    a=1/r**2
    vx=vx+a*cos*dt
    vy=vy+a*sin*dt
    xx.append(x)
    yy.append(y)
    t=t+dt
    





def fun(fram):                        #定義動畫
    plt.clf()
    plt.xlim(-4,4)                #範圍
    plt.ylim(-5,5)
    plt.scatter(xx[fram],yy[fram],c='b')
    plt.scatter(0,-2,c='r')            #圓心

animate=ani.FuncAnimation(fig=f,func=fun,interval=0.1,frames=1000,repeat=False)  










