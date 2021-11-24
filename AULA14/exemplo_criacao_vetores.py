import numpy as np

vetor_zeros = np.zeros(10, dtype='int64')
print(vetor_zeros)

matriz_zeros = np.zeros((5,4), dtype='int')
print(matriz_zeros)

matriz_uns = np.ones((50,100), dtype='int')
print(matriz_uns)

matriz_qualquer = np.array([[1,3,4], [3,1,1]])
#retorna a forma da matriz
#nesse caso, duas linhas e três colunas

print(matriz_qualquer.shape)