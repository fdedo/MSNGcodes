import numpy as np
import random
from scipy import stats

#Computation of Berry-Esseen Monte Carlo bound as explained in the paper

#parameters
S0 = 1 #asset price at time zero
sigma = 1 #volatilty
dt = 0.001 #discrete time increment
iteration = 11
N = iteration - 1 #N=10,20,50,100,200,500,1000 number of iterations
time = dt * (iteration-1)
M = int(1.0e5) #number of simulations
size = M * (iteration-1)

data_i = []
data_f = []
lnS = np.ndarray(shape = (iteration, M))

#TLD random numbers are extracted from a file with 10^8 deviates previously generated.
#Shuffling and reshaping allows to pick once each number in the file.
#Comment the lines below for the Gaussian simulation.
data_tld = np.genfromtxt(fname='/path/tldrandomnumbers.txt')
random.shuffle(data_tld)
data_i= data_tld[0:size]
matrix = np.reshape(data_i, (iteration-1, M))

#Iteration procedure. For the Gaussian scenario,  X = sigma * np.sqrt(dt) * np.random.normal();
#for the non-Gaussian one, X = sigma * np.sqrt(dt) * matrix[i-1,j], as explained in the paper.
for j in range(0, M):
      lnS[0, j] = np.log(S0)
      for i in range(1, iteration):
        lnS[i,j] = lnS[i-1,j] +  sigma * np.sqrt(dt) * matrix[i-1,j]#np.random.normal()

#Scaled sum variable as reported in Eq. (22) of the paper.
for j in range(0, M):
      for i in [N]:
            data_f.append(lnS[i,j]/np.sqrt(N*dt))

#Kolmogorov-Smirnov distance, namely the Monte Carlo bound of the Berry-Esseen theorem.
print(stats.kstest(data_f, stats.norm.cdf))
