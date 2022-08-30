# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:42:12 2021

@author: 陳忨詠
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def NLRK2(l,theta0,t0,tf,N):   
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
    
        thta=theta[i]+k22
        theta.append(thta)
        omg=omega[i]+k2
        omega.append(omg)        
        tt=tt+h
        xt.append(tt)
    return xt,theta
    
t,theta=NLRK2(0.1,179,0,10,10000) 
angle=[179]
for i in range(10000):
    degree=theta[i]*180/np.pi
    angle.append(degree)
plt.figure()
plt.title('theta-time(2ed Runge Kutta)')
plt.plot(t,angle)


def LFM(l,theta0,t0,tf,N):   
    h=(tf-t0)/N
    theta00=(theta0/180)*np.pi
    theta=[theta00]
    omega0=0
    omega=[]
    xt=[t0]
    theta0=0
    tt=0   
    kt0=omega0+(h/2)*-(9.81/l)*np.sin(theta[0])
    omega.append(kt0)
    
    for i in range(0,N):
        k11=theta[i]+h*omega[i]
        theta.append(k11)
        k1=omega[i]+h*-(9.81/l)*np.sin(theta[i+1])
        omega.append(k1)        
        tt=tt+h
        xt.append(tt)
    return xt,theta
    
t,theta=LFM(0.1,179,0,10,10000) 
angle=[179]
for i in range(10000):
    degree=theta[i]*180/np.pi
    angle.append(degree)
plt.figure()
plt.title('theta-time(leapfrog)')
plt.plot(t,angle)


def ENLFM(l,theta0,t0,tf,N):   
    h=(tf-t0)/N
    theta00=(theta0/180)*np.pi
    theta=[theta00]
    omega0=0
    omega=[]
    xt=[t0]
    Energy=[1*9.81*l*(1-np.cos((179/180)*np.pi))]  #質量設1公斤
    theta0=0
    tt=0   
    kt0=omega0+(h/2)*-(9.81/l)*np.sin(theta[0])
    omega.append(kt0)
    
    for i in range(0,N):
        k11=theta[i]+h*omega[i]
        theta.append(k11)
        k1=omega[i]+h*-(9.81/l)*np.sin(theta[i+1])
        omega.append(k1) 
        E=(0.5*1*(l*omega[i+1])**2)+1*9.81*l*(1-np.cos(theta[i+1]))
        Energy.append(E)
        tt=tt+h
        xt.append(tt)
    return xt,theta,Energy
    
t,theta,Energy=ENLFM(0.1,179,0,10,100000) 
angle=[179]
for i in range(100000):
    degree=theta[i]*180/np.pi
    angle.append(degree)

plt.figure()
plt.title('Energy-time(leapfrog)')
plt.plot(t,Energy)

#1(b) 首先從能量的週期有8個,剛好為此時段內角度週期(4)的兩倍,
#也就是能量的誤差為從起始到角度的半周期為一個週期,因角度在半周期
#時計算能量的條件與起始一樣,故能量誤差週期為角度週期的一半
#接著可以發現能量誤差在前半週期是從平衡點變大,是因為使用leapfrog
#方法使得該點位置所對應到的速度為下半步所對應到的數值,使的能量誤差
#不斷累積,且累積速度會愈來越慢,直到能量誤差週期的一半,這時的能量條件與
#初始條件一樣,但初始條件是沒有初速度的,在能量半周期的一開始因為當速度為零時
#其位置還沒達到平衡點,所以能量會比原本少,接著做一樣的循環到底

#2.(b)

def LFM(x0,t0,tf,h):   
    N=int((tf-t0)/h)
    x=[x0]
    v=[]
    xt=[t0]
    tt=0   
    v0=0+(h/2)*(0**2-1-5)
    v.append(v0)
    
    for i in range(0,N):
        xx=x[i]+h*v[i]
        x.append(xx)
        vv=v[i]+h*((v[i]**2)-x[i+1]-5)
        v.append(vv)        
        tt=tt+h
        xt.append(tt)
    return xt,x
    
t,x=LFM(1,0,50,0.001) 

plt.figure()
plt.title('x-time(leapfrog)')
plt.plot(t,x)


#3(a)(b)

def VM(x0,y0,vx0,vy0,t0,tf,h):   
    N=int(tf/h) 
    G=8.65*10**-13
    M=1.989*(10**30)
    XX=[x0]
    YY=[y0]
    VX=[]
    VY=[]
    VX1=[vx0]
    VY1=[vy0]
    xt=[t0]
    vxt0=vx0+0.5*h*(-G*M*XX[0]/abs((XX[0]**2+YY[0]**2)**1.5))
    VX.append(vxt0)
    vyt0=vy0+0.5*h*(-G*M*YY[0]/abs((XX[0]**2+YY[0]**2)**1.5))
    VY.append(vyt0)
    tt=0
    
    for i in range(0,N):
        xx=XX[i]+h*(VX[i])
        XX.append(xx)        
        yy=YY[i]+h*(VY[i])
        YY.append(yy)       
        kx=h*(-G*M*XX[i+1]/(abs(XX[i+1]**2+YY[i+1]**2)**1.5))
        vx1=VX[i]+0.5*kx
        VX1.append(vx1)
        vx2=VX[i]+kx
        VX.append(vx2)       
        ky=h*(-G*M*YY[i+1]/(abs(XX[i+1]**2+YY[i+1]**2)**1.5))
        vy1=VY[i]+0.5*ky
        VY1.append(vy1)
        vy2=VY[i]+ky
        VY.append(vy2)
        tt=tt+h
        xt.append(tt)
    return xt,XX,YY,VX,VX1,VY,VY1
    
t,x,y,vx,vx1,vy,vy1=VM(-(1.47*10**8),0,0,-1.09*10**5,0,8760,1)
plt.figure()
plt.title('earth-orbit')
plt.plot(x,y)

def EVM(x0,y0,vx0,vy0,t0,tf,h):   
    N=int(tf/h) 
    G=8.65*10**-13
    M=1.989*(10**30)
    m=5.9722*10**24
    PE=[]
    KE=[]
    TE=[]
    XX=[x0]
    YY=[y0]
    VX=[]
    VY=[]
    VX1=[vx0]
    VY1=[vy0]
    xt=[t0]
    vxt0=vx0+0.5*h*(-G*M*XX[0]/abs((XX[0]**2+YY[0]**2)**1.5))
    VX.append(vxt0)
    vyt0=vy0+0.5*h*(-G*M*YY[0]/abs((XX[0]**2+YY[0]**2)**1.5))
    VY.append(vyt0)
    PE0=-G*M*m/abs(XX[0]**2+YY[0]**2)**0.5    
    PE.append(PE0)
    KE0=0.5*m*(vx0**2+vy0**2)
    KE.append(KE0)
    TE0=PE0+KE0
    TE.append(TE0)
    tt=0
    
    for i in range(0,N):
        xx=XX[i]+h*(VX[i])
        XX.append(xx)        
        yy=YY[i]+h*(VY[i])
        YY.append(yy)       
        kx=h*(-G*M*XX[i+1]/(abs(XX[i+1]**2+YY[i+1]**2)**1.5))
        vx1=VX[i]+0.5*kx
        VX1.append(vx1)
        vx2=VX[i]+kx
        VX.append(vx2)       
        ky=h*(-G*M*YY[i+1]/(abs(XX[i+1]**2+YY[i+1]**2)**1.5))
        vy1=VY[i]+0.5*ky
        VY1.append(vy1)
        vy2=VY[i]+ky
        VY.append(vy2)
        PEE=-G*M*m/abs(XX[i+1]**2+YY[i+1]**2)**0.5
        PE.append(PEE)
        KEE=0.5*m*((vx1**2)+(vy1**2))
        KE.append(KEE)
        TEE=PEE+KEE
        TE.append(TEE)
        tt=tt+h
        xt.append(tt)
    return xt,PE,KE,TE
    
t,PE,KE,TE=EVM(-(1.47*10**8),0,0,-1.09*10**5,0,8760,1)
plt.figure()
plt.plot(t,KE, label='kinetic energy')
plt.plot(t,TE, label='total energy')
plt.plot(t,PE, label='potential energy')
plt.xlabel('time')
plt.ylabel('Energy')
plt.legend()
plt.show()
#3.(c)
#受萬有引力且不受外力影響的物體運動,可以預期其總能會是位能的一半,其圖表也大約看得出來
#假設我從外太空往-z軸方向看地球公轉是逆時針,則+z軸方向則是會順時針,且往+z軸方向會等價於
#往-z軸方向看的時間逆行運動,又物理客觀事實應相同且行星運動為周期性的,故一定會回到原點(當然用verlet的方法也是原因之一)


