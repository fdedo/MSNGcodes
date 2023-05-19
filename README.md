# MSNGcodes
Some codes used in the paper  "F. De Domenico, G. Livan, G. Montagna et al., Modeling and simulation of financial returns under non-Gaussian distributions, Physica A (2023)".

In this repository you can find a couple of codes written for the aforementioned paper. For a more extensive discussion of the topics, please see Section 4.3.

In _berryesseen.py_ the computation of the Monte Carlo bound for the Berry-Esseen theorem is implemented. 
To run the code, the file _tldrandomnumbers.txt_ is provided in an external Drive folder. This file stores 10^8 random numbers extracted from the Truncated Lévy distribution with zero mean and variance equal to one over the bounded region [-30,30], with parameter alpha = 1.5, lambda = 0.18, gamma = 0.4.

Drive folder: https://drive.google.com/file/d/1ecn7C_Qkfk-qEyw-OjZseTu8Qte5Di-c/view?usp=share_link

In _mfpt.py_ you can find an example of the computation of the firt mean passage time (mFPT). This variable gives information about
the first time a stochastic process hits a specific threshold U starting from a fixed initial value. 
As above, it is necessary to download the file _tldrandomnumbers.txt_ to correctly implement a comparison of the Gaussian and non-Gaussian scenario, as reported in the paper. 
