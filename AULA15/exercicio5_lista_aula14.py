import numpy as np

def normalizar(valores_coluna: np.ndarray):
  maximo = valores_coluna.max()
  minimo = valores_coluna.min()
  return (valores_coluna - minimo) / (maximo - minimo)

matriz = np.loadtxt('iris.data', delimiter=',')

n_colunas = matriz.shape[1]

for coluna in range(n_colunas):
  matriz[:, coluna] = normalizar(matriz[:, coluna])

print(matriz)