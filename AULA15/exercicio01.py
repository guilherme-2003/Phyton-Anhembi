def ler_numero() -> int:
    n = int(input('Digite um número qualquer: '))
    return n

def eh_primo(n:int) -> bool:
    for i in range(2,n):
        if n % i == 0:
            return False

n = ler_numero()
while(n != 0):
    if eh_primo(n):
        print(f'{n} é primo')
    else:
        print(f'{n} não é primo')
    n= ler_numero()