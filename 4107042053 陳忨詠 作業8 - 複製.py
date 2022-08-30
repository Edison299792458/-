# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:16:22 2021

@author: 陳忨詠
"""

import numpy as np
import matplotlib.pyplot as plt

#(1)
def Euler(t0,tf,N,x0):
    h=(tf-t0)/N
    xt=[t0]
    xy=[x0]
    xx=0
    tt=0
    for i in range(0,N):             
        xx=xy[i]+h*(-1*((xy[i])**3)+np.sin(xt[i]))
        tt=tt+h
        xt.append(tt)
        xy.append(xx)
    return xt,xy
        
x,y=Euler(0,10,1000,0)
plt.figure()
plt.title('Euler method')
plt.plot(x,y,'b.-')


def RK2(t0,tf,N,x0):
    h=(tf-t0)/N
    xt=[t0]
    xy=[x0]
    xx=0
    tt=0
    for i in range(0,N):
        k1=h*(-1*((xy[i])**3)+np.sin(xt[i]))
        k2=h*(-1*((xy[i]+0.5*k1)**3)+np.sin(xt[i]+0.5*h))
        xx=xy[i]+k2
        tt=tt+h
        xt.append(tt)
        xy.append(xx)
    return xt,xy
    
x1,y1=RK2(0,10,100,0)
plt.figure()
plt.title('2ed Runge Kutta')
plt.plot(x1,y1,'g.-')
    

def RK4(t0,tf,N,x0):
    h=(tf-t0)/N
    xt=[t0]
    xy=[x0]
    xx=0
    tt=0
    for i in range(0,N):
        k1=h*(-1*((xy[i])**3)+np.sin(xt[i]))
        k2=h*(-1*((xy[i]+0.5*k1)**3)+np.sin(xt[i]+0.5*h))
        k3=h*(-1*((xy[i]+0.5*k2)**3)+np.sin(xt[i]+0.5*h))
        k4=h*(-1*((xy[i]+k3)**3)+np.sin(xt[i]+h))
        xx=xy[i]+(1/6)*(k1+2*k2+2*k3+k4)
        tt=tt+h
        xt.append(tt)
        xy.append(xx)
    return xt,xy
    
x1,y1=RK4(0,10,40,0)  #測試結果大約為40次
plt.figure()
plt.title('4th Runge Kutta')
plt.plot(x1,y1,'r.-')





#(2)(a)
#方波生成
def Vin(N):
    h=10/N
    tt=[0]
    vv=[1]
    xt=0
    for i in range(0,N):
        xt=tt[i]+h
        xtt=round(2*xt)
        if (xtt% 2)==0:
            vv.append(1)
        else:
            vv.append(-1)
        tt.append(xt)        
    return tt,vv
x3,y3=Vin(1000) #此時的h為0.01

def Vout(N,RC):
    h=10/N
    h=h*2
    t,vi=Vin(N)
    vout=[0]
    newt=[0]
    nn=int(N/2)
    for i in range(0,nn):
        
        k1=h*((vi[2*i]-vout[i])/RC)
        k2=h*((vi[(2*i)+1]-(vout[i]+(0.5*k1)))/RC)
        k3=h*((vi[(2*i)+1]-(vout[i]+(0.5*k2)))/RC)
        k4=h*((vi[(2*i)+2]-(vout[i]+k3))/RC)
        vo=vout[i]+(1/6)*(k1+2*k2+2*k3+k4)
        vout.append(vo)
        pt=t[2*i]
        newt.append(pt)
    return newt,vout

#  h=0.02    
t4,vout=Vout(1000,0.01)
plt.figure()
plt.title('RC=0.01')
plt.plot(t4,vout,'b.-')


t5,vout=Vout(1000,0.1)
plt.figure()
plt.title('RC=0.1')
plt.plot(t5,vout,'b.-')


t4,vout=Vout(1000,1)
plt.figure()
plt.title('RC=1')
plt.plot(t4,vout,'b.-')


#(2)(b) 
#方波的傅立葉轉換之頻譜從低到高皆有
#低通濾波器是讓截止頻率以上之頻率之頻譜區域減少或去掉其振幅
#其中決定截止頻率為1/RC，所以當RC越小其濾波效果越差
#反之則越好，所以RC之大小可以看成是濾波效果的程度好壞。

#(3)

def iRK4(u0,uf,N,x0):
    m=10/(N)
    uff=(uf-m)   
    h=((uff/(1-uff))-(u0/(1-u0)))/N
    xt=[u0]
    xy=[x0]
    xx=1
    tt=0
    for i in range(0,N):
        a=(1-xt[i])*(xy[i])
        b=xt[i]
        k1=h*(1/(a**2+b**2))
        
        a1=(1-xt[i]-0.5*h)*(xy[i]+0.5*k1)
        b1=xt[i]+0.5*h
        k2=h*(1/(a1**2+b1**2))
        
        a2=(1-xt[i]-0.5*h)*(xy[i]+0.5*k2)
        b2=xt[i]+0.5*h
        k3=h*(1/(a2**2+b2**2))
        
        a3=(1-xt[i]-h)*(xy[i]+k3)
        b3=xt[i]+0.5*h
        k4=h*(1/(a3**2+b3**2))
        
        xx=xy[i]+(1/6)*(k1+2*k2+2*k3+k4)
        tt=tt+h
        xt.append(tt)
        xy.append(xx)
    return xt,xy

x4,y4=iRK4(0,1,500,1)
plt.figure()
plt.title('solution over an infinite range')
plt.plot(x4,y4,'b.-')
    















