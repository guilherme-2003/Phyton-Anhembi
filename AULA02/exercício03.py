# Faça um algoritmo que leia o salário de um funcionário. Sabendo que o salário do funcionário teve um aumento 
# de 25%, mostre o novo salário.

salario = float(input('Digite o salário de funcionário: '))

novo_salario = (salario * 0.25) + salario

print("O novo salário do funcionário é de R$%.2f" % novo_salario)