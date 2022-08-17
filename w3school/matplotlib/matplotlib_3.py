import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o')
# plt.show()

# plt.plot(ypoints, 'o--m')
# plt.show()

plt.plot(ypoints, marker = '*', ms = 20, mec = 'c', mfc = 'y')
plt.show()