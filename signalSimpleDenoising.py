import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat


# load the file with data
matfile = loadmat('denoising_codeChallenge.mat')

originalSignal = matfile['origSignal'][0]
filteredSignal = matfile['cleanedSignal'][0]

fig, axs = plt.subplots(2, 1)
axs[0].plot(originalSignal, 'red')
axs[1].plot(filteredSignal, 'black')
# plt.plot(originalSignal, 'red', filteredSignal, 'black')
plt.show()
