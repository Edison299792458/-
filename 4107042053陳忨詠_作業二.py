# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:34:42 2019

@author: 陳忨詠
"""



import numpy as np      #引入numpy及sympy模組
from sympy import *
x = Symbol('x')         #設定變數
m = Symbol('m')
r = Symbol('r')

ans1=integrate((2*m*x**3/r**2),(x,0,r))   #積圓柱
ans2=ans1.subs([(r,5),(m,1)])             #代入數值




ans3=integrate((2*m*x**3/r**2),(x,0,r))  #積圓盤
ans4=ans3.subs([(r,5),(m,1)])            #代入數值



ans5=integrate(((3*m/(4*r**3))*(r**4-2*x**2*r**2+x**4)),(x,0,r)) #積球體
ans6=ans5.subs([(r,5),(m,1)])                                    #代入數值



ans7=integrate((6*m*x**3*(r-x)/r**3),(x,0,r))  #積圓錐
ans8=ans7.subs([(r,5),(m,1)])                  #代入數值



m=1       #圓柱數值積分
r=5
h=4
dx=0.0001
I=0
x=0
while x<r:
    x=x+dx
    I=(2*m*x**3/r**2)*dx+I
    




m=1      #圓盤數值積分
r=5
h=4
dx=0.0001
II=0
x=0



while x<r:
    x=x+dx
    II=(2*m*x**3/r**2)*dx+II
    




m=1      #球體數值積分
r=5
h=4
dx=0.0001
III=0
x=0



while x<r:
    x=x+dx
    III=((3*m/(4*r**3))*(r**4-2*x**2*r**2+x**4))*dx+III
    




m=1     #圓錐數值積分
r=5
h=4
dx=0.0001
IIII=0
x=0
while x<r:
    x=x+dx
    IIII=((6*m*x**3*(r-x)/r**3))*dx+IIII
    


print("1.實心圓柱轉動慣量式:",ans1)
print("  帶入數值結果:",ans2)
print("  數值積分結果:", I)

print("2.薄圓盤轉動慣量式:",ans3)
print("  帶入數值結果:",ans4)
print("  數值積分結果:", II)

print("3.實心球轉動慣量式:",ans5)
print("  帶入數值結果:",ans6)
print("  數值積分結果:", III)

print("4.圓椎轉動慣量式:",ans7)
print("  帶入數值結果:",ans8)
print("  數值積分結果:", IIII)






