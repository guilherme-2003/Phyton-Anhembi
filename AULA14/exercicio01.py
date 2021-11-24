import numpy as np

n_linhas = int(input('Digite o número de linhas: '))
n_colunas = int(input('Digite o número de colunas: '))

matriz_aleatoria = np.random.random((n_linhas, n_colunas))

print(matriz_aleatoria)
print('----- Transposta -----')
print(matriz_aleatoria.T)