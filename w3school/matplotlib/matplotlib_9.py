import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# Barras
# plt.bar(x,y)
# plt.show()

# Draw 4 horizontal bars:
# plt.barh(x, y)
# plt.show()


# Draw 4 green bars:
plt.bar(x, y, color = "#4CAF50", width=.5)
plt.show()
