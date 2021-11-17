""" • Faça um programa que simule um sorteio da Mega Sena.
• Crie um dict comprehension que possui as chaves: primeiro, segundo,
terceiro, quarto, quinto e sexto.
– Cada chave corresponde a um número sorteado de 1 a 60 (assuma que dois números
iguais não serão sorteados). """

import random

ordem = ['primeiro', 'segundo', 'terceiro', 
         'quarto', 'quinto', 'sexto']

sorteio = {n: random.randint(1,60)
           for n in ordem}

print(sorteio)