# Criar uma função chamado encontrar_max – sua função deve receber dois números (int) como parâmetro de entrada;
# – e deve retornar o maior valor entre esses números. • Para testar seu programa: – Leia dois números do 
# usuário. – chame a função passando esses números. – imprima o valor retornado pelo sua função.

def encontrar_max(num1: int, num2: int) -> int:
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    eh_maior = encontrar_max(num1, num2)

    print("O maior número é", eh_maior)

main()