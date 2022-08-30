# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:55:02 2019

@author: 陳忨詠
"""

txt_r=open("number.txt",'r') #打開number.txt檔案為讀取模式，並記錄於txt_r
integer_r=txt_r.read() #讀取file的內容
txt_r.close()    #讀取完後關閉檔案
integer_r=float(integer_r) #轉換成int
a=integer_r**2 #再平方
a2=str(a)#再轉換回來
print(a)


txt_w=open("numbersquare.txt",'w')    #開啟numbersquare.txt文字檔為寫入模式，並記錄在numbersquare_w中，若沒有此檔案，則會新增一個
txt_w.write(a2)   #將string寫入文字檔中
txt_w.close() #關閉文字檔





import numpy as np
npy_r=np.load("originalSequence.npy")  #讀取originalSequence.npy內容進npy_r

n=[1,1]  #先建一個list且每項值為前2項加前1項
ans=1
for i in range(1,19):
      
    ans=ans+n[-2]
    n.append(ans)
    
np.save("PrimeSequence",n)  #將n list 存入新建的 PrimeSequence.npy檔中
print(n)




import pickle
p_r=open("originalList.pickle",'rb')    #開啟 originalList.pickle檔案為讀取模式，紀錄於p_r
lis=pickle.load(p_r)    #讀取p_r之內容
p_r.close() #關閉

print(len(lis))#知有20項

for i in range(20):   #把lis的20項小list加起來
    newlist=newlist+lis[i]
    
print(newlist)


p_w=open("newList.pickle",'wb')    #新建或開啟 pickle檔案為寫入模式，紀錄於p_w
pickle.dump(newlist,p_w) #將li 寫入p_w
p_w.close() #關閉





    
