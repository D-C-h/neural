import matplotlib.pyplot as plt
#for plotting

import numpy as np
#scintific computation library 



import sklearn.datasets

#generate data using sklearn


# Generate a dataset and plot it
np.random.seed(0)

X, y = sklearn.datasets.make_moons(200, noise=0.20)

plt.scatter(X[:,0], X[:,1], s=40, c=y, cmap=plt.cm.Spectral)

plt.show()

