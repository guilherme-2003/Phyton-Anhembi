# Ler dois números (ponto flutuante) e apresentá-los em ordem decrescente. Suponha que não sejam iguais.

from typing import NoReturn


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(num1) 
    print(num2)
elif num2 > num1:
    print(num2)
    print(num1)
else:
    print(f"Os números são iguais!")