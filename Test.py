import numpy as np
from scipy.stats import gaussian_kde
from matplotlib.colors import LogNorm, SymLogNorm, PowerNorm
import matplotlib.pyplot as plt

Num = 1e5
x1 = np.concatenate((np.random.normal(-5,1,int(Num//2)), np.random.normal(5,1,int(Num/2))))
x2 = np.random.normal(0,2,int(Num))

DataSlice = [x1, x2]

NBins = 30
counts,xbins,ybins=np.histogram2d(x1,x2,bins=NBins)
Levels = np.percentile(counts,[68,96,99])
print(Levels)

plt.figure()
plt.hist2d(x1,x2, cmap='gist_earth_r', bins = NBins, norm=PowerNorm(gamma=0.5))
plt.contour(counts.transpose(),Levels,extent=[xbins.min(),xbins.max(),
    ybins.min(),ybins.max()],linewidths=2,cmap="gray",
    linestyles='-')
plt.axis("equal")
plt.show()
