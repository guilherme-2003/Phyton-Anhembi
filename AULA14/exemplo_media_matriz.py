import numpy as np

notas_matriz = np.array([[10,8,4],[9,10,8]])
print(notas_matriz)
media = np.mean(notas_matriz, axis=0)
print(media)