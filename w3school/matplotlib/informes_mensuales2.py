from turtle import color
import matplotlib.pyplot as plt
import numpy as np

# Horas publicadores
x = np.array(["Sep", "Oct", "Nov", "Dic", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul"])
y = np.array([371, 452, 355, 413, 454, 443, 324, 370, 281, 375, 379])

plt.plot(x, y, linewidth = '2.5', color="#3CCF4E", marker = 'o', ms = 8, mfc = '#187498')

plt.title("INFORMES PUBLICADORES 2022")
plt.xlabel("MES")
plt.ylabel("TOTAL HORA MES")


plt.show()