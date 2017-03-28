# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 19:24:00 2017

@author: Sandesh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

bar_width=1.5
df=pd.read_csv('D:/py/wheat.data.txt')
s1=pd.concat([df.area,df.perimeter],axis=1)
s2=pd.concat([df.groove,df.asymmetry],axis=1)
df.plot.scatter(x='area',y='perimeter',marker='^')
df.plot.scatter(x='groove',y='asymmetry',marker='+')
df.plot.scatter(x = 'compactness', y = 'width', marker = 'o')

plt.show()