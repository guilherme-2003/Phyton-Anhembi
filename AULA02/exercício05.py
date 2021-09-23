# Construir um algoritmo que leia o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
# – A idade dessa pessoa. – Quantos anos ela terá em 2030. 

ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento
idade_2030 = 2030 - ano_nascimento

print(f"Você tem {idade} anos e em 2030 terá {idade_2030} anos")
