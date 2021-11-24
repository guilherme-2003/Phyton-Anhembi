import numpy as np


# Matriz aleatória de 20 linhas e 5 colunas
mat_aleatoria = np.random.random((20,5)) * 100

# maximo_colunas tem 5 elementos 
maximo_colunas = np.max(mat_aleatoria, axis=0)

mat_normalizada = mat_aleatoria / maximo_colunas
print(mat_normalizada)
