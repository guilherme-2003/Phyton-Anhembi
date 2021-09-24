# Crie uma função chamada fatorial: – A função recebe como parâmetro um número inteiro. – O fatorial é calculado 
# pela multiplicação de todos seus antecessores até o 1. Exemplo: Fatorial (5) = 5 * 4 * 3 * 2 * 1.
# – Use recursão para calcular o fatorial.

def fatorial(num: int) -> int:
    if num == 1:
        return 1
    else:
        fat = fatorial(num -1)
        return num * fat

def main():
    num = int(input("Digite um número: "))

    fator = fatorial(num)

    print(fator)

main()