import numpy as np
import matplotlib.pyplot as plt
from CornerPlot import CustomCornerPlot, DoubleCustomCornerPlot

Parameters = ["T0", "Tinf", "Gam", "P0", "MR1", "MR2", "MR3", "MR4", "MR5"]

Mean1 = [300, 100, 5.0, 1.0, 0.1, 0.1, 0.05, 0.05, 0.1]
Sigma1 = [10, 5, 0.25, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01]

Mean2 = [315, 105, 5,0, 1.0, 0.09, 0.09, 0.06, 0.06, 0.15]
Sigma2 = [12, 6, 0.25, 0.05, 0.02, 0.02, 0.02, 0.02, 0.02]

DataPoints = 1000

np.random.seed(42)
Data1 = np.zeros((len(Parameters), DataPoints))
Data2 = np.zeros((len(Parameters), DataPoints))

for count, Param in enumerate(Parameters):
    Data1[count, :] = np.random.normal(Mean1[count], Sigma1[count], DataPoints) 
    Data2[count, :] = np.random.normal(Mean2[count], Sigma2[count], DataPoints) 	
print("The shape of the data is given by:", np.shape(Data1))

CustomCornerPlot(Data1, Parameters)
DoubleCustomCornerPlot(Data1, Data2, Parameters)




