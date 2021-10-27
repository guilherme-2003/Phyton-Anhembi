""" Crie um programa que sorteie 100 números de 0 a 10. – Percorra todos esses números e crie um dicionário mostrando quantas vezes cada número aparece.
– Depois compare o resultado com a função Counter (disponível no módulo collections). """


import random
from collections import Counter #importa o Counter (contador) da coleção "collections"

contagem = {}

numeros_extenso = {0: 'zero', 1: 'um', 2: 'dois',

          3: 'tres', 4: 'quatro',

          5: 'cinco', 6: 'seis',

          7: 'sete', 8: 'oito',

          9: 'nove', 10: 'dez'}

for _ in range(100):

  aleatorio = random.randint(0, 10)
  num = numeros_extenso[aleatorio]

  if aleatorio in contagem:
    contagem[num] += 1
  else:
    contagem[num] = 1

print(contagem)

# Fazendo usando o Counter

lista_numeros = []
for _ in range(100):
    aleatorio = random.randint(0,10)
    num = numeros_extenso[aleatorio]
    lista_numeros.append(num)

nova_contagem = Counter(lista_numeros)
print(nova_contagem)