from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np


stats = loadmat('stats/stats_step_4000.mat')['stats']

for s in stats:
    for t in np.transpose(s, (2, 0, 1)):
        plt.imshow(t)
        plt.colorbar()
        plt.show()
