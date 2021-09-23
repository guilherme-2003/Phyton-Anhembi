# Ler o salário de uma pessoa, calcular e imprimir o desconto do INSS de acordo com as seguintes regras:
# -> <= R$ 600,00: Isento 
# ->  > R$ 600,00 e <= R$ 1200,00: 20% 
# ->  > R$ 1200,00 e <= R$ 2000,00: 25% 
# ->  > R$ 2000,00: 30%

salario = float(input("Digite o seu salário: "))

if salario <= 600:
    print("Isento do desconto de INSS")
elif salario <= 1200:
    desconto = salario * 0.2
    print(f"Deconto de R${desconto:.2f} (20%)")
elif salario <= 2000:
    desconto = salario * 0.25
    print(f"Deconto de R${desconto:.2f} (25%)")
else:
    desconto = salario * 0.3
    print(f"Deconto de R${desconto:.2f} (30%)")