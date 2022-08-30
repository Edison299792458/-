# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:07:25 2020

@author: 陳忨詠
"""

import random as r
import matplotlib.pyplot as plt

N=10000


x1=[]  #x1y1是用來存取園內的點座標
y1=[]
x2=[]  #x2y2是用來存取園外的點座標
y2=[]



for i in range(N):
    
    random_number=r.random()    #生成0~1隨機浮點數字

    x=random_number
   
   

    
    random_number=r.random()    #生成0~1隨機浮點數字

    y=random_number



    if (x**2 + y**2)**0.5 <= 1:     #假設座標點距離原點小於等於1的話就是在原裡面
        x1.append(x)   
        y1.append(y)   
  
    else:                         #否則再外面
        x2.append(x)
        y2.append(y)
        
plt.scatter(x1,y1,color='r')    
plt.scatter(x2,y2,color='b')
plt.show()


pi=(len(x1)+len(y1))*2/10000   #園內點與10000的比例就知道pi

print("pi=",pi)


import numpy as np


m=100  #每次走100步


b=1000  #1000次

g=[]  #建立list把每100步距離原點的距離記錄下來
D=0
for i in range(b):
    for j in range(m):
        p=r.randint(1,2)   #產生2就前進  1就後退

        if p==2:
            D=D+1
    
        elif p==1:
            D=D-1
    g.append(D)
    

   
a=sum(g)/len(g)
print("1000次後距離原點",D)
print("每100步後距離原點的平均值",a)






