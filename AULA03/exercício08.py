# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições 
# para aposentadoria são: – Ter no mínimo 65 anos. – Ou ter trabalhado pelo menos 30 anos. – Ou ter pelo menos 
# 60 anos e trabalhado pelo menos 25.

idade = int(input("Digite a sua idade: "))
tempo_serviço = int(input("Digite quantos anos você trabalhou: "))

if idade >= 65:
    print("Pode se aposentar por idade!")
elif tempo_serviço >= 30:
    print("Pode se aposentar por tempo de contribuição!")
elif idade >= 60 and tempo_serviço >= 25:
    print("Pode se aposentar por idade e tempo de contribuição")
else:
    print("Não pode se aposentar!")