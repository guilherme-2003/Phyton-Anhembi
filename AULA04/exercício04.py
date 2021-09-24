# Faça uma função para calcular e retornar a área de um triângulo. – sua função deve receber altura e base como 
# parâmetros de entrada. – e deve retornar a área do triângulo. • Para testar seu programa: 
# Leia dois números do usuário. chame a função passando esses números -imprima o valor retornado pela sua função

def area_triangulo(altura: float, base: float) -> float:
    calculo_area = (base * altura) / 2
    return calculo_area

def main():
    altura = float(input("Digite a medida da altura do triângulo: "))
    base = float(input("Digite a medida da base do triângulo: "))
    
    area = area_triangulo(altura, base)

    print(f"A área do triângulo é {area:.2f}")

main()