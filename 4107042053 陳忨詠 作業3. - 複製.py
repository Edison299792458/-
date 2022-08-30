# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:20:35 2021

@author: 陳忨詠
"""
#第一題
#PA=LU
import numpy as np

def plu(A):
    tA=A.copy()
    n=len(A[0])
    list1=[]
    list2=[]
    pivots=[]
    for c in range(n):
        max_b = c + np.argmax(np.abs(tA[c:, c]))
        P=np.eye(n)
        P[[c, max_b]] = P[[max_b, c]]
        list2.append(P)
        tA[[c, max_b]] = tA[[max_b, c]]
        L0 = np.zeros([n,n])
        for i in range(n):
            for j in range(n):
                if i==c and j==c:
                    L0[i][j]=1
                elif i==j:
                    L0[i][j]=tA[c][c]
                elif j==c:
                    L0[c+1:,[j]]=-tA[c+1:,[c]]
        L0=L0/tA[c][c]
        tA=L0.dot(tA)
        list1.append(L0)
        pivots.append(c)
    PP=np.eye(n)
    for i in reversed(pivots):
        PP=PP.dot(list2[i])
    U=np.eye(n)
    for i in reversed(pivots):
        U=U.dot(list1[i]).dot(list2[i])
    U=U.dot(A)
    labcd=[]
    
    for j in range(n):
        la=np.eye(n)
        for i in range(n-1,j,-1):
            la=la.dot(list2[i])
        la=la.dot(list1[j])
        for i in range(j+1,n):
            la=la.dot(list2[i])
        labcd.append(la)
    tb=A.copy()
    l1=[]
    PA=PP.dot(tb)
    l1.append(PA)
    for i in range(n):
        PA=labcd[i].dot(PA)
        l1.append(PA)
        
    L=np.zeros([n,n])
    for z in range(n):
        for i in range(z,n):
            for j in range(n):
                if j==z:
                    L[i][j]=l1[z][i][z] 
                    
   
    
    
    
    
    return PP,U,labcd,L
A=np.array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]])
P,U,labcd,L=plu(A)




print("P=",P)
print("L=",L)
print("U=",U)
pa=P.dot(A)
print("PA=",P.dot(A))
lU=L.dot(U)
print("LU=",lU)


def plulineq(A,v):    
    P,U,labcd,L=plu(A)
    v=P.dot(v)
    n2=len(A[0])
    li=labcd[n2-1]
    for i in range (1,n2):       
        li=li.dot(labcd[n2-1-i])
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

A=np.array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]])
v=np.array([-4,3,9,7])
x,li=plulineq(A,v)


print(x)
print("x1=",x[3])
print("x2=",x[2])
print("x3=",x[1])
print("x4=",x[0])


answer=np.linalg.solve(A,v)
print(answer)   #驗證成功

#第二題
def banded(A,v,up,lower):
    t=np.column_stack((A,v))
    t=np.asarray(t,dtype=np.float64)
    n=len(t[0])
    n2=len(A[0])    
    u=up
    l=lower
    i=0
    j=0 
    while i < t.shape[0] and j < t.shape[1]:
        
        t[i] = t[i]/t[i, j]
        for k in range(l):
            if (i +k+ 1) < t.shape[0]:
                t[i+1+k,j:]=t[i+1+k,j:]-t[i,j:]*t[i+1+k,i]
            
        i += 1
        j += 1
    x=[]
    x.append(t[n2-1,n2])  
    for i in range(1,n2):
        s=0
        while s<i:
            t[n2-i-1,n2]=t[n2-i-1,n2]-t[n2-(i+1),n2-(s+1)]*x[s]
            s=s+1
        x.append(t[n2-i-1,n2])
  
    return t,x

A=np.array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]])
v=np.array([-4,3,9,7])
up=3
lower=3

s,x=banded(A,v,up,lower)
print(s)
print(x)




k=6
m=1
w=2
c=1
A = np.zeros([26,26])
for i in range(25):
    A[i][i+1]=-k
    A[i+1][i]=-k    
for Q in range(1,25):
    A[Q][Q]=(-m*w**2)+2*k

A[0][0]=(-m*w**2)+k
A[25][25]=(-m*w**2)+k

v=np.zeros([26,1])
v[0][0]=c


s,x=banded(A,v,up,lower)

 #x26在第一個 x1在最後一個

x.reverse()
print(x)

import matplotlib.pyplot as mat

d=range(1,27)
mat.scatter(d,x)
mat.show()



    
    
    
    
    
    
