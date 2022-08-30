# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:52:26 2021

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt
def Euler(f,y0,t):
    y = np.zeros(len(t))
    y[0] = y0
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1] - t[n])
    return y
ff=lambda y,x:-y**3+np.sin(x)
tt=np.linspace(0,10,1000)
y0=0
y=Euler(ff,y0,tt)
plt.figure()
plt.plot(tt,y,'b.-')
plt.legend(['Euler'])

def rungeKutta2(x0, y0, x, h):
    list1=[]
    n = round((x - x0) / h)
    y = y0
    for i in range(1, n + 1):
        k1=h*ff(x0, y)
        k2=h*ff(x0 + 0.5 * h, y + 0.5 * k1)
        y=y+(1.0 / 6.0) * (k1 + 2 * k2)
        list1.append(y)
        x0=x0+h
    return list1
def rungeKutta4(x0, y0, x, h):
    list1=[]
    n = round((x - x0) / h)
    y = y0
    for i in range(1, n + 1):
        k1=h*ff(x0, y)
        k2=h*ff(x0 + 0.5 * h, y + 0.5 * k1)
        k3=h*ff(x0 + 0.5 * h, y + 0.5 * k2)
        k4=h*ff(x0 + h, y + k3)
        y=y+(1.0 / 6.0) * (k1+2*k2+2*k3+k4)
        list1.append(y)
        x0=x0+h
    return list1
x0 = 0; y0 = 0;
x = 10; h = 0.1;
tt1=np.linspace(0,10,100)
yy=rungeKutta2(x0, y0, x, h)
yyy=rungeKutta4(x0, y0, x, h)
plt.figure()
plt.plot(tt1,yy,'r.-',tt1,yyy,'y.-',tt,y,'b.-')
plt.legend(['rk2','rk4','Euler'])
plt.show()
