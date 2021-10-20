tabela = {'alface': 0.45, 'batata': 1.20, 'tomate': 2.30, 'feijão': 1.50}

print(tabela['alface'])
print(tabela['tomate'])

tabela['ovo'] = 6.00 # O elemento ovo é adicionado ao dicionário
tabela['feijão'] = 2.00

print(tabela['ovo']) # Mostrará 6
print(tabela['feijão']) # Mostrará 2
print(tabela['brocolis']) # Mostrará um erro, pois a chave não existe
