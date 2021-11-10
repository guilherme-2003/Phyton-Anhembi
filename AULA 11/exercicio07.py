""" Elabore um algoritmo que preencha uma matriz 4 ˆ 4 de inteiros e depois faça: – Imprimir toda a matriz. – Trocar a segunda linha pela terceira. 
– Trocar a primeira pela quarta coluna. – Imprimir novamente a matriz """

import random

def printar_matriz(matriz: 'list[list[int]]'):
  for linha in matriz:
    for valor in linha:
      print(f'{valor:<5}', end=' ') # < 5 serve para completar com espaços em branco
    print()
  print()

n_linhas = 4
n_colunas = 4

matriz = []

for l in range(n_linhas):
  linha = []
  for c in range(n_colunas):
    aleatorio = random.randint(0, 100)
    linha.append(aleatorio)
  matriz.append(linha)

printar_matriz(matriz)

aux = matriz[1] # segunda linha
matriz[1] = matriz[2]
matriz[2] = aux

printar_matriz(matriz)

for l in range(n_linhas):
  aux = matriz[l][0]
  matriz[l][0] = matriz[l][3]
  matriz[l][3] = aux

printar_matriz(matriz)