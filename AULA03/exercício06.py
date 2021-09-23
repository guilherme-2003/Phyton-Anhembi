# Determine se um ano lido é bissexto. Um ano é bissexto se for divisível por 400 ou se for divisível por 4 e 
# não for divisível por 100.

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print(f"{ano} é bissexto!")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto!")