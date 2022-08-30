# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:46:16 2020

@author: 陳忨詠
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([-0.0405+0.001*i for i in range(82)])   #x座標的範圍 (-0.0405~0.0405包含頭尾，共82個值)
y=np.array([-0.0405+0.001*i for i in range(82)])   #y座標的範圍

u=np.array([[0.0 for i in range(82)] for j in range(82)])  #向量的x分量 (共101*101個值是一個二維的array)
v=np.array([[0.0 for i in range(82)] for j in range(82)])  #向量的y分量
#在建造array時請注意資料型態，若給他的初始值都是int，則是後將無法進行浮點數的運算

k=1
q1=-1
q2=1
q3=1
q4=-1

for i in range(82):
    for j in range(82):
        if x[j]==0.01 and y[i]==0.01 and x[j]==-0.01 and y[i]==-0.01 and x[j]==-0.01 and y[i]==0.01 and x[j]==0.01 and y[i]==-0.01: #中心點位置無法定義sin與cos，因此需另外計算向量的值，設為零
            u[i][j]=0
            v[i][j]=0
        else:
            r1=((x[j]+0.01)**2+(y[i]-0.01)**2)**0.5
            r2=((x[j]-0.01)**2+(y[i]-0.01)**2)**0.5
            r3=((x[j]+0.01)**2+(y[i]+0.01)**2)**0.5
            r4=((x[j]-0.01)**2+(y[i]+0.01)**2)**0.5
            E1=k*q1/r1**2
            sin1=(y[i]-0.01)/r1
            cos1=(x[j]+0.01)/r1
            E2=k*q2/r2**2
            sin2=(y[i]-0.01)/r2
            cos2=(x[j]-0.01)/r2
            E3=k*q3/r3**2
            sin3=(y[i]+0.01)/r2
            cos3=(x[j]+0.01)/r2
            E4=k*q4/r4**2
            sin4=(y[i]+0.01)/r2
            cos4=(x[j]-0.01)/r2
            u[i][j]=E1*cos1+E2*cos2+E3*cos3+E4*cos4   #電場為可線性疊加
            v[i][j]=E1*sin1+E2*sin2+E3*sin3+E4*sin4





plt.streamplot(x, y, u, v,color='g')
#streamplot函式，需丟入x (x座標範圍)、y (y座標範圍)、u (向量的x分量)、v (向量的y分量)
#須注意streamplot函式的輸入必須是array，另外可以改變color變數，使向量的顏色改變

x1=-0.01
y1=0.01
plt.scatter(x1,y1,color='b')

x2=0.01
y2=0.01
plt.scatter(x2,y2,color='r')

x3=-0.01
y3=-0.01
plt.scatter(x3,y3,color='r')

x4=0.01
y4=-0.01
plt.scatter(x4,y4,color='b')

plt.show()