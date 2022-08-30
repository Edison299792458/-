# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:19:51 2020

@author: 陳忨詠
"""
import matplotlib.pyplot as plt
import numpy as np


x2=np.array([-0.0405+0.001*i for i in range(82)])   #x座標的範圍 (-0.0405~0.0405包含頭尾，共82個值)
y2=np.array([-0.0405+0.001*i for i in range(82)])   #y座標的範圍

u2=np.array([[0.0 for i in range(82)] for j in range(82)])  #向量的x分量 (共82*82個值是一個二維的array)
v2=np.array([[0.0 for i in range(82)] for j in range(82)])  #向量的y分量
#在建造array時請注意資料型態，若給他的初始值都是int，則是後將無法進行浮點數的運算


k=1
q=-1



for i in range(82):
    for j in range(82):
        if x2[j]==0 and y2[i]==0: #中心點位置無法定義sin與cos，因此需另外計算向量的值，設為零
            u2[i][j]=0
            v2[i][j]=0
        else:
            r=(x2[j]**2+y2[i]**2)**0.5
            E=k*q/r**2
            sin=y2[i]/r
            cos=x2[j]/r
            u2[i][j]=E*cos
            v2[i][j]=E*sin


plt.streamplot(x2, y2, u2,v2,color='g')
#streamplot函式，需丟入x (x座標範圍)、y (y座標範圍)、u (向量的x分量)、v (向量的y分量)
#須注意streamplot函式的輸入必須是array，另外可以改變color變數，使向量的顏色改變
x2=0
y2=0
plt.scatter(x2,y2,color='b')

plt.show()
