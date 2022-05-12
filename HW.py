
import math
from statistics import harmonic_mean, mean,stdev
from random import choices
import matplotlib.pyplot as plt
inputarr=[1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40]
N=len(inputarr)
def getharmonicmean(arr):
    #Harmonic Mean
    XH=N/sum([xi for xi in inputarr])
    print(XH)

    #Psedues values
    Yi=[]
    for index,val in enumerate(inputarr):
        value=0
        for jindex,jval in enumerate(inputarr):
            if jindex!=index:
                value+=1/(inputarr[jindex])
        
        Yi.append((N-1)/value)
    print(Yi)

    Ybar=sum(Yi)/N
    print(Ybar)

    SH=math.sqrt((N-1)*sum([(Yi[index]-Ybar)**2 for index in range(len(Yi))]))
    print(SH)
    return XH,SH



XH,SH=getharmonicmean(inputarr)
alpha=0.1
constval=1.782
c1_jack=XH - 1.782*(SH/math.sqrt(N))
c2_jack=XH + 1.782*(SH/math.sqrt(N))

print("Jack Method:",c1_jack,c2_jack)
list_mean_c1=[]
list_mean_c2=[]
list_std1=[]
list_std2=[]
list_k=[]
for k in range(10,301,10):
    c1_20,c2_20=[],[]
    for _ in range(20):
        sample_arr=[]
        for iteration in range(k):
            arr=choices(inputarr,k=N)
            hm=harmonic_mean(arr)
            sample_arr.append(hm)
        sample_arr.sort()
        idx_c1=int(0.025*len(sample_arr))
        idx_c2=int(0.975*len(sample_arr))
        c1,c2=sample_arr[idx_c1],sample_arr[idx_c2]
        #print(c1,c2)
        c1_20.append(c1)
        c2_20.append(c2)
    list_k.append(k)
    list_mean_c1.append(mean(c1_20))
    list_mean_c2.append(mean(c2_20))
    list_std1.append(stdev(c1_20))
    list_std2.append(stdev(c2_20))
print(list_k)
print(list_mean_c1)
print(list_mean_c2)
print(list_std1)
print(list_std2)

plt.scatter(list_k, list_mean_c1)
#plt.scatter(list_k, list_mean_c2)
#plt.scatter(list_k, list_std1)
#plt.scatter(list_k, list_std2)

plt.show()

