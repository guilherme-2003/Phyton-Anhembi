#Faça um algoritmo para ler um número inteiro. Verificar se o número está no intervalo entre 50 (inclusive) e 
# 100 (inclusive), se estiver, imprimir "Pertence ao intervalo", senão imprimir "Não pertence ao intervalo".

num = int(input('Digite um número: '))

if num >= 50 and num <= 100:
    print("Pertence ao intervalo!")
else:
    print("Não pertence ao intervalo!")