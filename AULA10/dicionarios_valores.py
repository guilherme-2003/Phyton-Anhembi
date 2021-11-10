info_pessoas = {'João': {'idade': 27, 'sexo': 'masculino'},
'Fernando': {'idade': 18, 'sexo': 'feminino'},
'Aline': {'idade': 20, 'sexo': 'feminino'}}

for nome in info_pessoas:
    idade = info_pessoas[nome]['idade']
    sexo = info_pessoas[nome]['sexo']
    print(f'{nome} tem {idade} anos, sexo {sexo}.')

for info in info_pessoas.values():
    print(info)

