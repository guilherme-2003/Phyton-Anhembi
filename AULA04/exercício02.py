# Faça uma função com retorno chamada media: – sua função deve receber três notas como parâmetros de entrada;
# – e deve retornar a média das três notas. Faça com que todo seu programa rode dentro de uma função main().
# – Deixe apenas a chamada do método main fora de alguma função.

def media(nota1: float, nota2: float, nota3: float) -> float:
    media = (nota1 + nota2 + nota3) / 3
    return media

def main():
    nota1 = float(input("Digite a primeira nota: ")) 
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    calculo_media = media(nota1, nota2, nota3)

    print(f"A média é {calculo_media:.2f}")

main()  
