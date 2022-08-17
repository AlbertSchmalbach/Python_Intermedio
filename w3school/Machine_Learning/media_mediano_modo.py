import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Media
x = numpy.mean(speed)

# Mediana
y = numpy.median(speed)

# Modo
z = stats.mode(speed)

print('Media: ', x)
print('Mediana: ', y)
print('Modo: ', z)
