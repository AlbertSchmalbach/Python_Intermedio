import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
# Sintaxis más corta:
# plt.plot(ypoints, ls = ':')
# plt.plot(ypoints, color = 'r')
# Ancho de línea:
# plt.plot(ypoints, linewidth = '20.5')
#Varias lineas:
# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)
plt.show()