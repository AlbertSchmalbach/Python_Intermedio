import numpy
import matplotlib.pyplot as plt

# Cree una matriz que contenga 250 flotadores aleatorios entre 0 y 5:
# x = numpy.random.uniform(0.0, 5.0, 250)

# print(x)
# plt.hist(x, 5)
# plt.show()

# Cree una matriz con 100000 números aleatorios y muéstrelos usando un histograma con 100 barras:
x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()