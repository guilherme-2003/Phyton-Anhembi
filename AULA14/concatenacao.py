import numpy as np

matriz1 = np.random.random((3,2))
matriz2 = np.random.random((3,2))

print('----- matriz 1 -----\n', matriz1)
print('----- matriz2 -----\n', matriz2)

# colocar as matrizes uma do lado da outra
# deveria ser (3,4)
horizontal = np.hstack((matriz1, matriz2))
print('----- hstack -----\n', horizontal)

# colocar as matrizes uma em cima da outra
# deveria ser (6,2)
vertical = np.vstack((matriz1, matriz2))
print('----- vstack -----\n', vertical)