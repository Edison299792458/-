# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:01:57 2020

@author: 陳忨詠
"""

import pandas as pd
import matplotlib.pyplot as plt

excel=pd.read_excel('test.xlsx') #利用pandas 讀取excel檔案 


x=excel['x']
y=excel['y']
plt.plot(x,y)








import PyOrigin as P
import pandas as pd
import matplotlib.pyplot as plt

excel=pd.read_excel('test.xlsx')  #利用pandas 讀取excel檔案
x=excel['x']
y=excel['y']
plt.plot(x,y)

P.FindWorksheet('[Book1]Sheet1').Columns(0).SetData(x)   #將讀取的資料中column(0)變為oringin的x軸
P.FindWorksheet('[Book1]Sheet1').Columns(1).SetData(y)   #將讀取的資料中column(1)變為oringin的y軸


