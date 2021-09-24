# Faça uma função sem retorno chamada somar: – sua função deve receber dois inteiros como parâmetros de entrada;
# – e deve imprimir a seguinte mensagem: ¨ “Soma dos parâmetros: <soma>”. – chame a sua função três vezes . . .
# – e passe valores diferentes como parâmetro para cada chamada da função.

def somar(num1: int, num2: int):
    resultado = num1 + num2
    print("Soma dos parâmetros: ", resultado)

somar(10, 10)
somar(100, 100) 
somar(1000, 1000)