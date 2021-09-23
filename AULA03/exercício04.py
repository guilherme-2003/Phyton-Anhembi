# Faça um algoritmo que receba a idade de um nadador e imprima sua categoria seguindo as regras: 
# – Bebê: menores de 5 anos. – Infantil A: 5 a 7 anos. – Infantil B: 8 a 10 anos. – Juvenil A: 11 a 13 anos.
# – Juvenil B: 14 a 17 anos. – Sênior: 18 anos ou mais.

idade = int(input("Digite a idade do nadador: "))

if idade < 5:
    print("Categoria Bebê!")
elif idade < 8:
    print("Categoria Infantil A!")
elif idade < 11:
    print("Categoria Infantil B!")
elif idade < 14:
    print("Categoria Juvenil A!")
elif idade < 18:
    print("Categoria Juvenil B!")
else:
    print("Categoria Sênior!")