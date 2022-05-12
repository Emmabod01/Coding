#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
from statistics import harmonic_mean, mean,stdev
import matplotlib.pyplot as plt

IPC_data=[1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40]
n=len(IPC_data)

def JackKKnifeHM(arr):
    #Harmonic Mean
    xH=n/sum([Xi for Xi in IPC_data])
    print(xH)

    #Psedues values
    Yi=[]
    for index,val in enumerate(IPC_data):
        value=0
        for jindex,jval in enumerate(IPC_data):
            if jindex!=index:
                value+=1/(IPC_data[jindex])
        
        Yi.append((n-1)/value)
    print(Yi)

    Ybar=sum(Yi)/n
    print(Ybar)

    sH=math.sqrt((n-1)*sum([(Yi[index]-Ybar)**2 for index in range(len(Yi))]))
    print(sH)
    return xH,sH



xH,sH=JackKKnifeHM(IPC_data)

#confidence interval of 90 percent, constant value from the t-table
constval=1.782
C1_jackknife=xH - 1.782*(sH/math.sqrt(n))
C2_jackknife=xH + 1.782*(sH/math.sqrt(n))

print(" Using Jackknife's technique C1 & C2 are:",C1_jackknife,C2_jackknife,"respectively")


# In[ ]:




