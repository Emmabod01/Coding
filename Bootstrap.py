 

# IPC Data

IPC_data = [1.01, 0.99, 0.78, 1.12, 1.20, 0.86, 0.65, 0.56, 0.87, 0.63, 0.70, 1.24, 1.40]
import statistics
import random
import array as arr

# Random sampling with replacement of K [10 - 300]
sample_k = [],

for k in range(10,300):
    
    sample_k = random.choices(IPC_data, k=10)
    

    #iterate each K 20 times
    
    
    xH = [],
    SD = [],
    sample_i = [],
    xH = arr.array('d', [])
    
    for i in range(1,20):

        sample_i == random.choices(sample_k, k=10)

       #computing the estimator (xH, S.D,) for each iteraion
        
        y = statistics.harmonic_mean(sample_i)
        xH.append(y)
        

        z = statistics.stdev(sample_i)
        SD.append(z)

        # sort harmonic mean in ascending order

        xH.sort()

        # 95 percent confidence interval
        # (1 - 0.95)/2 = 0.025 x 20 - approximate to 1 i.e 1st value
        # 1 - 0.025 = 0.975 x 20 - approximate to 19 i.e 19th value

        C1 = xH[1]
        C2 = xH[19]

    print("For value K =", k, "Harmonic mean =", xH, "Standard deviation =", SD, "Confidence interval C1 =", C1,"Confidence interval C1 =", C2)

print("All the values of K are", K)
      
     
    
        





        

        

        
