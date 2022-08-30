# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:39:41 2021

@author: User
"""
#python3
import numpy as np
import matplotlib.pyplot as plt 
M = 1.98*10**30
G=66374.2
def ff(v0):
    vx=v0[0]
    vy=v0[1]
    fxx=f1(vx)
    fyy=f2(vy)
    return np.array([fxx,fyy],float)
def f(r0):
    x=r0[0]
    y=r0[1]
    fxxx=fx(x,y)
    fyyy=fy(x,y)
    return np.array([fxxx,fyyy],float)
f1=lambda x:x
def fx(x,y): #x acceleration
     return -G*M*x/((x**2+y**2)**(3/2))
f2=lambda y:y
def fy(x,y): #y acceleration
     return -G*M*y/((x**2+y**2)**(3/2))

def rkx(r0,v0,t,h):
    xx=[r0[0]]
    vx=[v0[0]]
    yy=[r0[1]]
    vy=[v0[1]]
    N=int(t/h)

    for i in range(0,N): 
        k1y = h*ff(v0)
        k1v = h*f(r0)

        k2y = h*ff(v0+0.5*k1v)
        k2v = h*f(r0+0.5*k1y)

        k3y = h*ff(v0+0.5*k2v)
        k3v = h*f(r0+0.5*k2y)

        k4y = h*ff(v0+k3v)
        k4v = h*f(r0+k3y)

        r0 = r0 + (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        v0 = v0 + (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        xx.append(r0[0])
        yy.append(r0[1])
        vx.append(v0[0])
        vy.append(v0[1])
    return np.array([xx,yy]),np.array([vx,vy])
r0=[4*10**12,0]
v0=[0,15768000000]
a,b=rkx(r0,v0,165,165/200000)
t=0#c,d,e 跑不出來
t1=165
h=165/200000

def time_step(r0, v0,t, h):
    def runge_kutta_step(r0,v0, t, h):
        k1y = h*ff(v0)
        k1v = h*f(r0)

        k2y = h*ff(v0+0.5*k1v)
        k2v = h*f(r0+0.5*k1y)

        k3y = h*ff(v0+0.5*k2v)
        k3v = h*f(r0+0.5*k2y)

        k4y = h*ff(v0+k3v)
        k4v = h*f(r0+k3y)
        a=(k1y + 2 * k2y + 2 * k3y + k4y) / 6
        b=(k1v + 2 * k2v + 2 * k3v + k4v) / 6
        c=np.hstack((a,b))
        return c

    delta_step_1 = runge_kutta_step(r0,v0, t, h)
    delta_step_2 = runge_kutta_step(r0 + delta_step_1[0:2],v0+delta_step_1[2:4], t + h, h)
    delta_r1 = delta_step_1 + delta_step_2

    delta_r2 = runge_kutta_step(r0,v0, t, 2*h)

    delta_x1 = delta_r1[0]
    delta_x2 = delta_r2[0]
    delta_y1 = delta_r1[1]
    delta_y2 = delta_r2[1]
    error = (((delta_x1 - delta_x2) **2 + (delta_y1 - delta_y2) **2)**0.5) / 30

    rho = h*1000 / error
    factor = np.power(rho, 1 / 4)

    if  rho >= 1:
        t = t + 2 * h
        if factor > 2:
            h *= 2
        else:
            h *= factor
        delta_r1[0] += (delta_x1 - delta_x2) / 15
        delta_r1[1] += (delta_y1 - delta_y2) / 15
        return delta_r1, h, t
    else:
        return time_step(r0,v0, t, factor * h)
delta=1000
h=165/150000
tt=[]
xx=[]
yy=[]
list1=[]
list2=[]
while(t < t1):
    tt.append(t)
    xx.append(r0[0])
    yy.append(r0[1])
    delta_r, h, t = time_step(r0,v0, t, h)
    r0 += delta_r[0:2]
    v0 += delta_r[2:4]
for i in range(0,1586,30):
    list1.append(xx[i])
    list2.append(yy[i])
plt.plot(a[0],a[1])
plt.plot(list1 ,list2 , 'ro')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()