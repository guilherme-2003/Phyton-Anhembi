palpite = int(input("Digite seu palpite: "))

if palpite == 15:
    print("O palpite está correto. Parabéns!")
elif palpite < 15:
    print("O palpite está abaixo do correto.")
else: # A última possibilidade épalpite > 15
    print("O palpite ultrapassou o correto.")