# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:05:24 2020

@author: 陳忨詠
"""

import matplotlib.pyplot as plt

L=0.0405
dl=0.001
k=1
q=1

x=np.array([-0.0405+0.001*i for i in range(82)])   #x座標的範圍 (-0.0405~0.0405包含頭尾，共82個值)
y=np.array([-0.0405+0.001*i for i in range(82)])   #y座標的範圍

V=np.array([[0.0 for i in range(82)] for j in range(82)])  #(共82*82個值是一個二維的array)


for i in range(82):
    for j in range(82):
        if i==0 and j==0 :           #不能除以0
            V[i][j]=0
        else:    
            r=((x[j])**2+(y[i])**2)**0.5    #到原點之距離
            V[i][j]=k*q/r   #電位
            
plt.subplot(4, 4, 1)       
plt.imshow(V,origin='lower',vmin=-80,vmax=80,extent=[-L,L,-L,L]) #vmin,vmax可限制最大最小值,extent控制x,y座標軸,origin用以調整座標軸原點
plt.colorbar() #叫出色條colorbar


plt.subplot(4,4,3) 
cont=plt.contour(x,y,V,100) #最後一個數字為等高線密度設定
plt.clabel(cont) #加上數字標記等高線



k=1
q=1
q1=-1

x=np.array([-0.0405+0.001*i for i in range(82)])   #x座標的範圍 (-0.0405~0.0405包含頭尾，共82個值)
y=np.array([-0.0405+0.001*i for i in range(82)])   #y座標的範圍

V=np.array([[0.0 for i in range(82)] for j in range(82)])  #(共82*82個值是一個二維的array)


for i in range(82):
    for j in range(82):
        if i==0.01 and j==0 and i==-0.01 and j==0:       #不能除以0
            V[i][j]=0
        else:    
            r=((x[j]+0.01)**2+(y[i])**2)**0.5
            r1=((x[j]-0.01)**2+(y[i])**2)**0.5
            V[i][j]=k*q/r+k*q1/r1    #電位可現性疊加
            
plt.subplot(4, 4, 5)       
plt.imshow(V,origin='lower',vmin=-80,vmax=80,extent=[-L,L,-L,L]) #vmin,vmax可限制最大最小值,extent控制x,y座標軸,origin用以調整座標軸原點
plt.colorbar() #叫出色條colorbar


plt.subplot(4,4, 7) 
cont=plt.contour(x,y,V,100) #最後一個數字為等高線密度設定
plt.clabel(cont) #加上數字標記等高線




k=1
q=1
q2=1

x=np.array([-0.0405+0.001*i for i in range(82)])   #x座標的範圍 (-0.0405~0.0405包含頭尾，共82個值)
y=np.array([-0.0405+0.001*i for i in range(82)])   #y座標的範圍

V=np.array([[0.0 for i in range(82)] for j in range(82)])  #(共82*82個值是一個二維的array)


for i in range(82):
    for j in range(82):
        if i==0.01 and j==0 and i==-0.01 and j==0:         #不能除以0
            V[i][j]=0
        else:    
            r=((x[j]+0.01)**2+(y[i])**2)**0.5
            r2=((x[j]-0.01)**2+(y[i])**2)**0.5
            V[i][j]=k*q/r+k*q2/r2
            
plt.subplot(4, 4, 9)       
plt.imshow(V,origin='lower',vmin=-80,vmax=80,extent=[-L,L,-L,L]) #vmin,vmax可限制最大最小值,extent控制x,y座標軸,origin用以調整座標軸原點
plt.colorbar() #叫出色條colorbar


plt.subplot(4, 4, 11) 
cont=plt.contour(x,y,V,100) #最後一個數字為等高線密度設定
plt.clabel(cont) #加上數字標記等高線





k=1
q0=1
q2=1
q3=-1
q4=-1

x=np.array([-0.0405+0.001*i for i in range(82)])   #x座標的範圍 (-0.0405~0.0405包含頭尾，共82個值)
y=np.array([-0.0405+0.001*i for i in range(82)])   #y座標的範圍

V=np.array([[0.0 for i in range(82)] for j in range(82)])  #(共82*82個值是一個二維的array)


for i in range(82):
    for j in range(82):
        if i==0.01 and j==0.01 and i==-0.01 and j==-0.01 and i==-0.01 and j==0.01 and i==0.01 and j==-0.01: #不能除以0
            V[i][j]=0
        else:    
            r0=((x[j]+0.01)**2+(y[i]+0.01)**2)**0.5
            r2=((x[j]-0.01)**2+(y[i]-0.01)**2)**0.5
            r3=((x[j]+0.01)**2+(y[i]-0.01)**2)**0.5
            r4=((x[j]-0.01)**2+(y[i]+0.01)**2)**0.5
            V[i][j]=k*q0/r0+k*q2/r2+k*q3/r3+k*q4/r4
            
plt.subplot(4, 4, 13)       
plt.imshow(V,origin='lower',vmin=-80,vmax=80,extent=[-L,L,-L,L]) #vmin,vmax可限制最大最小值,extent控制x,y座標軸,origin用以調整座標軸原點
plt.colorbar() #叫出色條colorbar


plt.subplot(4, 4, 15) 
cont=plt.contour(x,y,V,100) #最後一個數字為等高線密度設定
plt.clabel(cont) #加上數字標記等高線















