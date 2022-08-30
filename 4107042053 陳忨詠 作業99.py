# -*- coding: utf-8 -*-
"""
Created on Sun May  9 21:01:02 2021

@author: 陳忨詠
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation


#1.
def liRK4(t0,tf,N,x0,y0,z0):
    h=(tf-t0)/N
    x=[x0]
    y=[y0]
    z=[z0]
    r0=[x,y,z]
    xt=[t0]  
    xx=0
    tt=0
    for i in range(0,N):
        k1=h*np.array([10*(y[i]-x[i]),28*x[i]-y[i]-x[i]*z[i],x[i]*y[i]-(8/3)*z[i]],float)
        k2=h*np.array([10*((y[i]+0.5*k1[1])-(x[i]+0.5*k1[0])),28*(x[i]+0.5*k1[0])-(y[i]+0.5*k1[1])-(x[i]+0.5*k1[0])*(z[i]+0.5*k1[2]),(x[i]+0.5*k1[0])*(y[i]+0.5*k1[1])-(8/3)*(z[i]+0.5*k1[2])],float)
        k3=h*np.array([10*((y[i]+0.5*k2[1])-(x[i]+0.5*k2[0])),28*(x[i]+0.5*k2[0])-(y[i]+0.5*k2[1])-(x[i]+0.5*k2[0])*(z[i]+0.5*k2[2]),(x[i]+0.5*k2[0])*(y[i]+0.5*k2[1])-(8/3)*(z[i]+0.5*k2[2])],float)
        k4=h*np.array([10*((y[i]+k3[1])-(x[i]+k3[0])),28*(x[i]+k3[0])-(y[i]+k3[1])-(x[i]+k3[0])*(z[i]+k3[2]),(x[i]+k3[0])*(y[i]+k3[1])-(8/3)*(z[i]+k3[2])])
        xx=x[i]+(1/6)*(k1[0]+2*k2[0]+2*k3[0]+k4[0])
        yy=y[i]+(1/6)*(k1[1]+2*k2[1]+2*k3[1]+k4[1])
        zz=z[i]+(1/6)*(k1[2]+2*k2[2]+2*k3[2]+k4[2])
        tt=tt+h
        xt.append(tt)
        x.append(xx)
        y.append(yy)
        z.append(zz)
    return xt,x,y,z

t,x,y,z=liRK4(0,50,2500,0,1,0)
plt.figure()
plt.title('y-t')
plt.plot(t,y)
plt.figure()
plt.title('x-z')
plt.plot(x,z)

#2.
def NLRK4(l,theta0,t0,tf,N):   
    h=(tf-t0)/N
    theta00=(theta0/180)*np.pi
    theta=[theta00]
    omega0=0
    omega=[omega0]
    xt=[t0]
    theta0=0
    tt=0   
    for i in range(0,N):
        k11=h*omega[i]
        k1=h*-(9.81/l)*np.sin(theta[i])
        
        k22=h*(omega[i]+0.5*k1)
        k2=h*-(9.81/l)*np.sin(theta[i]+0.5*k11)
    
        k33=h*(omega[i]+0.5*k2)
        k3=h*-(9.81/l)*np.sin(theta[i]+0.5*k22)
        
        k44=h*(omega[i]+k3)
        k4=h*-(9.81/l)*np.sin(theta[i]+k33)
        
        thta=theta[i]+(1/6)*(k11+2*k22+2*k33+k44)
        theta.append(thta)
        omg=omega[i]+(1/6)*(k1+2*k2+2*k3+k4)
        omega.append(omg)        
        tt=tt+h
        xt.append(tt)
    return xt,theta
    
t,theta=NLRK4(0.1,179,0,15,1000) 
angle=[179]
for i in range(1000):
    degree=theta[i]*180/np.pi
    angle.append(degree)
plt.figure()
plt.title('theta-time')
plt.plot(t,angle)

xdata = 0.1*np.sin(theta)
ydata =-0.1*np.cos(theta)

fig, ax = plt.subplots()
ax.grid()
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    ax.set_xlim(-0.2, 0.2)
    ax.set_ylim(-0.2, 0.2)
    time_text.set_text('')
    return line, time_text

def update(i):
    newx = [0, xdata[i]]
    newy = [0, ydata[i]]
    line.set_data(newx, newy)
    time_text.set_text(time_template %(0.1*i))
    return line, time_text

ani = animation.FuncAnimation(fig, update, range(1, len(xdata)), init_func=init, interval=50)
plt.show()

 
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
plt.figure()
plt.title('orbit')
plt.plot(a[0],a[1])
plt.plot(list1 ,list2 , 'ro')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()











