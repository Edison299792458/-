# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 12:53:37 2021

@author: 陳忨詠
"""

import numpy as np
import matplotlib.pyplot as plt
def dft(y):
    N=len(y)
    n = np.arange(N)
    n = np.expand_dims(n, axis=1)
    k = n
    m = n.T * k / N
    S = np.exp(-1j * 2 * np.pi * m)
    c=S.dot(y)
    return c,k


#1.(b) i

n=np.ones(500)
nn = np.expand_dims(n, axis=1)
p=n*(-1)
pp = np.expand_dims(p, axis=1)

sq=np.vstack((pp,nn))
c0,k0 = dft(sq)
plt.figure()
c0=np.abs(c0)

plt.plot(k0,c0)

#1.(b) ii
swag=[]

for i in range(1000):
    swag.append(i)
sawg=np.array(swag,float)
swag=np.expand_dims(swag, axis=1)
c2,k2 = dft(swag)
plt.figure()
c2=np.abs(c2)
plt.plot(k2,c2)

#1.(b) iii

sine=[]
for i in range(1000):
    sinw=np.sin((np.pi*i)/1000)*np.sin((20*np.pi*i)/1000)
    sine.append(sinw)

sine=np.array(sine,float)
sine=np.expand_dims(sine, axis=1)
c3,k3 = dft(sine)
plt.figure()
c3=np.abs(c3)
plt.plot(k3,c3)

#1.(c) 

with open('pitch.txt', 'r') as pp:
    t= pp.readlines()

pit=np.array(t,float)
pit=np.expand_dims(pit, axis=1)
c4,k4 = dft(pit)
plt.figure()
c4=np.abs(c4)
plt.plot(k4,c4)



#2.(a)
print("周期約100個月")

#2.(b)
list1=[]
list2=[]
list3=[]
list4=[]
with open('sunspots.txt', 'r') as ff:
    i= ff.readlines()
    for a in i:
        list1 .append(a.split())
for i,j in list1:
    list2.append(float(i))
    list3.append(float(j))
    
    

plt.figure()
plt.subplot(2,1,1)
plt.plot(list2,list3)
x=np.array(list3,float)
x=np.expand_dims(x, axis=1)
c,k = dft(x)
for i in c:
    mX = np.abs(i)
    mX=mX**2
    list4.append(mX)

plt.subplot(2,1,2)
plt.plot(k,list4)
plt.show()