# Criar uma calculadora de operações básicas (soma, subtração, multiplicação e divisão). O algoritmo deve ler 
# dois números e o sinal correspondente à operação desejada. No final deve ser mostrado o resultado.

num1 = float(input("Digite o primeiro número: "))
operador = input("Digite a operação que deseja (*, /, +, -): ")
num2 = float(input("Digite o segundo número: ")) 

if operador == '*':
    multiplicar = num1 * num2
    print("O resultado da multiplicação é", multiplicar)
elif operador == '+':
    somar = num1 + num2
    print("O resultado da soma é", somar)
elif operador == '-':
    subtrair = num1 - num2
    print("O resultado da subtração é", subtrair)
elif operador == '/' and num2 != 0:
    dividir = num1 / num2
    print("O resultado da divisão é", dividir)
elif operador == '/' and num2 == 0:
    print("Não é possível dividir por 0!")
else:
    print("Operação inválida!")