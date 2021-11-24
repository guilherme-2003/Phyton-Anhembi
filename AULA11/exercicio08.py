""" Considere um sistema onde os dados são armazenados em dicionários. – Nesse sistema existe um dicionário principal e o dicionário de backup. – Cada vez que o dicionário principal atinge 
tamanho 5, ele imprime os dados na tela e apaga o seu conteúdo. • Crie um programa que insira dados em um dicionário, realizando o backup a cada dado e excluindo os dados do dicionário 
principal quando ele atingir tamanho 5."""

principal = {}
backup = {}

encerrar = False
while not encerrar: # laço while infinito
    opcao = int(input('Digite a opção desejada: \n'+
                        '1 - Inserir no dicionário\n'+ 
                        '2 - Imprimir dicionário\n'+
                        '3 - Sair do programa\n'+
                        '> '))

    if opcao == 1:
        nome = input('Digite seu nome: ')
        nota = float(input('Digite sua nota: '))

        principal[nome] = nota
        backup[nome] = nota

        # Limpar o dicionário e printar seu valor (não necessariamente nessa ordem)
        if len(principal) >= 5:
            print(principal)
            principal = {}

    elif opcao == 2:
        print(f'Principal: {principal}')
        print(f'Backup: {backup}')

    elif opcao == 3:
        encerrar = True

    else:
        print('Opção inválida!')

