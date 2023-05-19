import numpy as np
import random

#Computation of the firt mean passage time (mFPT). This variable gives information about
#the first time a stochastic process hits a specific threshold U starting from a fixed initial value.

#parameters
S0 = 1 #asset price at time zero
sigma = 1 #volatilty
dt = 0.001 #discrete time increment
iterations = 11
N = iterations - 1 #N=10, 50, 100, 500, 1000 number of iterations
M = int(1.0e5) #number of simulations
size = (iterations-1) * M
U = 1 #threshold U = ±1, ±3

data_i =[]
data_time = []
lnS = np.ndarray(shape = (iterations, M))


#TLD random numbers are extracted from a file containing 10^8 deviates previously generated.
#Shuffling and reshaping allows to pick once each number in the file.
#Comment the lines below for the Gaussian simulation.

data_tld = np.genfromtxt(fname='/Users/fedededo/Desktop/TESI/tldrandomnumbers.txt')
#data_tld = np.genfromtxt(fname='/path/tldrandomnumbers.txt')
random.shuffle(data_tld)
data_i= data_tld[0:size]
matrix = np.reshape(data_i, (iterations-1, M))

#Iteration procedure
#Enter np.random.normal() as random number for the Gaussian scenario
#and matrix[i-1,j] for the non-Gaussian one.

for j in range(0, M):
      lnS[0, j] = np.log(S0)
      for i in range(1, iterations):
        lnS[i,j] = lnS[i-1,j] +  sigma * np.sqrt(dt) * matrix[i-1,j] #np.random.normal()

#Scaled variables are compared to threshold ±U (see Eq. (23) of the paper).
#When the threshold is hit for the first time at iteration i, time t =i *dt is recorded.
for j in range(0, M):
      for i in range(1,iterations):
            if (lnS[i,j]/np.sqrt(i*dt))>=U or (lnS[i,j]/np.sqrt(i*dt)) <= -U:
                  data_time.append(i*dt)
                  break

#Computation of mFPT
mfpt = np.mean(data_time)

#Number of events hitting the threshold and mean first passage time are printed
print(f"{len(data_time)}, {round(mfpt,5)}")
