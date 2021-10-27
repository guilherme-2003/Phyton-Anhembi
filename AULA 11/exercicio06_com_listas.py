n_linhas = 15
n_colunas = 5

matriz = []

for l in range(n_linhas):
    linha = []
    for c in range(n_colunas):
        linha.append(0)
    matriz.append(linha)

matriz[0][0] = 10
matriz[10][4] = 3
matriz[2][2] = 1

for linha in matriz:
    print(linha)