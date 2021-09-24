def somar(n1: int , n2: int) -> int:
    resultado = n1 + n2
    return resultado

def main():
    print("Realizando a soma de dois numeros...")
    resultado = somar(10, 50)
    print("Fim da soma")
    print("Soma dos parâmetros:", resultado)

main()