import numpy as np


# DESVIACION STANDAR

speed1 = [86,87,88,86,87,85,86]

# La desviación estándar es: 0.9

speed2 = [32,111,138,28,59,77,97]

# La desviación estándar es: 37.85

x = np.std(speed1)

print('La desviación estándar de speed1', x)

y = np.std(speed2)

print('La desviación estándar de speed2', y)

# VARIANZA

z = np.var(speed2)

print('El valor de la varianza para speed2', z)