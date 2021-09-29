#Crie um programa que receba uma altura e imprima uma pirâmide de caracteres ‘*’ com a altura dada:

def imprimir_piramide(nivel_maximo: int):
    for nivel in range(nivel_maximo):
        print( (nivel + 1) * '*')

tamanho = int(input("Digite quantos níveis terá sua pirâmide: "))
imprimir_piramide(tamanho)