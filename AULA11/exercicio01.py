""" Crie um programa que combine nomes de pessoas com seus respectivos RAs. O programa deve ler: 4 nomes separados por espaço. 4 RAs separados por espaço. Combine os nomes com os RAs usando 
a função zip. No final, mostre todas as tuplas com os nomes seguidos dos RAs. """


nomes_str = input("Digite a lista de nomes separada por espaço: ")
ras_str = input('Digite a lista de RA separada por espaço: ')

nomes = nomes_str.split(' ')
ras = ras_str.split(' ')

print(list(zip(nomes, ras))) #comando zip para combinar resultados, usando o list(zip) ele printa o valor em listas
