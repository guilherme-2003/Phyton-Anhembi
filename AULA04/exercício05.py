# Crie uma função chamada ispar: – sua função deve receber um número inteiro como parâmetro de entrada e deve
# retornar: True -> se o número for par: False -> se o número for ímpar. Para testar sua função:
#–leia um número do usuário. – chame a função ispar passando esse número como parâmetro e imprima:
# “número par” caso o retorno da função seja True. “número impar” caso o retorno da função seja False.

def ispar(num: int) -> int:
    if num % 2 ==0:
        return True
    else:
        return False

def main():
    num = int(input("Digite um número: "))

    if ispar(num):
        print("Número par")
    else:
        print("Número ímpar")

main()
