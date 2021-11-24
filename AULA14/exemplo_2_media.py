import numpy as np

notas = np.array([10,8,4,9,10,8], dtype='float')
maiores_que7 = notas[notas > 7]

media = np.mean(maiores_que7)
print(media)