# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:43:56 2021

@author: 陳忨詠
"""

import numpy as np

def QR_decomposition(A):
    n=len(A[0])
    uu=[A[:,[0]]]
    qq=[A[:,[0]]/np.linalg.norm(A[:,[0]])]
    for i in range(1,n):
        u=A[:,[i]]
        for j in range(i):
            u=u-np.array([A[:,i]]).dot(qq[j])*(qq[j])
        q=u/np.linalg.norm(u)
        uu.append(u)
        qq.append(q)
        
    Q=qq[0]
    for i in range(len(qq)-1):
        Q=np.column_stack((Q,qq[i+1]))
        
    R=np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if i==j:
                R[i][j]=np.linalg.norm(uu[i])
            elif j>i:
                R[i][j]=qq[i].T.dot(A[:,[j]])
    return Q,R
A=np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]])
Q,R=QR_decomposition(A)
print("Q=",Q)
print("R=",R)
print("QR=",Q.dot(R))




def QR_algorithm(A):
    Q,R=QR_decomposition(A)
    n=len(A[0])    
    QQ=[]
    RR=[]
    QQ.append(Q)
    RR.append(R)
    Qii=np.transpose(Q)    
    ak=Qii.dot(A).dot(Q)
    akk=ak.copy()
    for i in range(n):
        akk[i][i]=0
    abak=np.abs(akk)
    maxak=np.max(abak)
    v=Q
    j=0
    while maxak>10**(-6):
        An=RR[j].dot(QQ[j])       
        Qn,Rn=QR_decomposition(An)
        QQ.append(Qn)
        RR.append(Rn)
        Qni=np.transpose(Qn)
        ak=Qni.dot(ak).dot(Qn)
        akk=ak.copy()
        for i in range(0,n):
            akk[i][i]=0
        abak=np.abs(akk)
        maxak=np.max(abak)      
        j=j+1
        v=v.dot(QQ[j])
    return ak,v

ak,v=QR_algorithm(A)
EVS=[]
n=len(A[0])
for i in range(0,n):
    EV=ak[i][i]
    EVS.append(EV)
   
print("eigenvalues=",EVS)
print("eigenvectors=",v)
answer=np.linalg.eigh(A) #檢查過為正確







