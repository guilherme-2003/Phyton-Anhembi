""" Faça um programa que recebe palavras do usuário até que ele insira uma linha em branco (string vazia). Após o usuário inserir essa linha em branco, 
você deve imprimir na tela cada palavra inserida pelo usuário. - Palavras repetidas não devem ser exibidas na tela. - As palavras devem ser impressas na ordem em que foram inseridas no programa. """

palavra = 'algo'
lista_palavras = []
lista_repetidas = []

while palavra != '':
    palavra = input('Digite uma palavra qualquer: ')
    if palavra == '':
        break

    lista_palavras.append(palavra)

for palavra in lista_palavras:
    if palavra not in lista_repetidas:
        print(palavra)
        lista_repetidas.append(palavra)