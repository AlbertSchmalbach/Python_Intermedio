import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Convierta los datos en un conjunto de puntos
data = list(zip(x, y))
# print(data) 
# [(4, 21), (5, 19), (10, 24), (4, 17), (3, 16), (11, 25), (14, 24), (6, 22), (10, 21), (12, 21)]

# Calcule el vínculo entre todos los diferentes puntos
linkage_data = linkage(data, method='ward', metric='euclidean')

# Finalmente, traza los resultados en un dendrograma
dendrogram(linkage_data)

plt.show()