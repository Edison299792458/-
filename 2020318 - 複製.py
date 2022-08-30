# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:06:05 2020

@author: 陳忨詠
"""

from matplotlib import pyplot as plt, animation as ani

f=plt.figure(facecolor='white')
xx=[i for i in range(100)]
yy=[xx[i] for i in range(100)]

def fun(fram):
    plt.clf()
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.scatter(xx[fram],yy[fram],c='b')

animate=ani.FuncAnimation(fig=f,func=fun,interval=60,frames=100)