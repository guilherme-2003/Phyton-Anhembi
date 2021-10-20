nome_cpf = {
    'Gustavo': "19203847653",
    'Fernando': "00000000001",
    'Maria': "11111111111",
    'Celso': "22222222222"
}

nomes = list(nome_cpf.keys())
for nome in nomes:
    if nome[0] == 'C':
        del nome_cpf[nome]

print((nome_cpf))