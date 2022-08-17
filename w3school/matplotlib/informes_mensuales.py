import matplotlib.pyplot as plt
import numpy as np

# Horas publicadores
x = np.array(["Sep", "Oct", "Nov", "Dic", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"])
y = np.array([371, 452, 355, 413, 454, 443, 324, 370, 281, 375, 379])

plt.bar(x,y, color='green')
plt.show()