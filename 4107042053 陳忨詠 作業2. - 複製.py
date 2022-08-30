# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:01:07 2021

@author: 陳忨詠
"""

import numpy as np
def LU_decomposition(A):
    q=0
    n=len(A[0])
    list=[A]
    list2=[]
    while q<n:    
        L = np.zeros([n,n],dtype=complex)
        for i in range(n):
            for j in range(n):
                if i==q and j==q:
                    L[i][j]=1
                elif i==j:
                    L[i][j]=A[q][q]                    
        for k in range(q+1,n):
            for j in range(n):
                if j==q:
                    L[k][j]=-A[k][q] 
                       
        L=L/A[q][q]
        A=L.dot(A)        
        list.append(A)
        list2.append(L)
        q=q+1
    l0=np.zeros([n,n],dtype=complex)   
    for z in range(n):
        for i in range(z,n):
            for j in range(n):
                if j==z:
                    l0[i][j]=list[z][i][z]  
    return A,l0,list2
A=np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]])
print(A)
U,L,list2=LU_decomposition(A)
print(U)
print(L)
print(L.dot(U))

def lulineq(A,v):    
    U,L,list2=LU_decomposition(A)
    n2=len(A[0])
    li=list2[n2-1]
    for i in range (1,n2):       
        li=li.dot(list2[n2-1-i])
    vp=li.dot(v)
    t=np.column_stack((U,vp))    
    n2=len(A[0])   
    x=[]
    x.append(t[n2-1,n2])
        
    for i in range(1,n2):
        s=0
        while s<i:
            t[n2-i-1,n2]=t[n2-i-1,n2]-t[n2-(i+1),n2-(s+1)]*x[s]
            s=s+1
        x.append(t[n2-i-1,n2])
    x=np.array(x)
    return x,li

A=np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]])
v=np.array([-4,3,9,7])
x,li=lulineq(A,v)

print(x)
print("x1=",x[3])
print("x2=",x[2])
print("x3=",x[1])
print("x4=",x[0])






#第二題的(b)
A=np.array([[1.5+1j,-1j,0],[-1j,1.5+1.5j,-0.5j],[0,-0.5j,1.5+0.5j]])
v=np.array([3,1.5,3])
x,li=lulineq(A,v)

print("x1=",x[2])
print("x2=",x[1])
print("x3=",x[0])



import cmath as cm
z=x[0]
print(cm.polar(z))
z1=x[1]
print(cm.polar(z1))
z2=x[2]
print(cm.polar(z2))









