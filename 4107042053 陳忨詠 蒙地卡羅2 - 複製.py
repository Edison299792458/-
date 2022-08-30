# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:59:24 2020

@author: 陳忨詠
"""

import random as r
import matplotlib.pyplot as plt

N=10000


x1=[]
y1=[]
x2=[]
y2=[]



for i in range(N):
    
    random_number=r.random()    #生成0~1隨機浮點數字

    x=random_number
   
   

    
    random_number=r.random()    #生成0~1隨機浮點數字

    y=random_number



    if (x**2 + y**2)**0.5 <= 1:   
        x1.append(x)   
        y1.append(y)   
  
    else:
        x2.append(x)   
        y2.append(y) 
    
p=(((len(x1)+len(y1))*2)/10000)
print(p)
s=(len(x1)/(len(x2)+len(x1))


plt.scatter(x1,y1,color='r')
plt.scatter(x2,y2,color='b')





plt.show()                        #畫出來吧!

