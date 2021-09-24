# Crie uma função chamada faz_calculo com 3 parâmetros: -Um parâmetro obrigatório num1.
# –Um parâmetro obrigatório num2. –Um parâmetro opcional chamado operação com valor padrão ’+’. Teste sua função

def faz_calculo(num1: float, num2: float, operacao='+') -> float:
    
    print(f"{num1} {operacao} {num2}")

faz_calculo(num1=2, num2=5, operacao='*')