""" Crie um dicionário matriz onde as chaves são representadas por tuplas. – Cada tupla é um par de inteiros, representando a linha e a coluna da matriz. – Crie uma matriz de tamanho 10 ˆ 10 
com os seguintes elementos (0, 0) = 2, (1, 3) = 8, (4, 3) = 6. Os demais elementos são 0. – Tente criar a mesma matriz utilizando listas dentro de listas e compare o tamanho delas."""

n_linhas = 15
n_colunas = 5

matriz = {}
matriz[(0, 0)] = 10
matriz[(10, 4)] = 3
matriz[(2, 2)] = 1

for l in range(n_linhas):
    for c in range(n_colunas):
        if  (l, c) in matriz:
            print(matriz[(l, c)], end= ' ') # end= é um parâmetro opcional para indicar como um print deve terminar
        else:
            print(0, end= ' ')
    print()

# isso é um exemplo de matriz esparsa, onde partes vazias de uma matriz não são armazenadas, nesse caso, apenas substituidas por 0