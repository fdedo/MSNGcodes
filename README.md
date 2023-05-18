# MSNGcodes
Some codes used in the paper  "F. De Domenico, G. Livan, G. Montagna et al., Modeling and simulation of financial returns under non-Gaussian distributions, Physica A (2023)".

In this repository you can find a couple of codes written for the aforementioned paper. 

In _berryesseen.py_ the computation of the Monte Carlo bound for the Berry-Esseen theorem is implemented. 
To run the code, _tldrandomnumbers.txt_ is provided as well. This file stores 10^8 random numbers extracted from the Truncated Lévy distribution with zero mean and variance equal to one over the bounded region [-30,30], with parameter alpha = 1.5, lambda = 0.18, gamma = 0.4.

In mfpt.py  
