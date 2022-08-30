# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:52:21 2020

@author: 陳忨詠
"""

import random as r
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
