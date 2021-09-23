# Faça um programa que receba dois números e diga: – se o primeiro número é maior que o segundo;
# – se o segundo é maior que o primeiro; – se os números são iguais.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro é maior que o segundo!")
elif num2 > num1:
    print("O segundo é maior que o primeiro!")
else:
    print("Os números são iguais!")