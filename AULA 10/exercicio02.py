info_pessoas = {'João': {'idade': 27, 'sexo': 'masculino'},
'Fernando': {'idade': 18, 'sexo': 'feminino'},
'Aline': {'idade': 20, 'sexo': 'feminino'}}

info_pessoas['Gustavo'] = {'idade': 29,
                            'ano nascimento': 1992,
                            'sexo': 'masculino',
                            'altura': 1.75}

info_pessoas['Gabriel'] = {'altura': 1.78}

for nome in info_pessoas:
    if 'idade' in info_pessoas[nome]:
        idade = info_pessoas[nome]['idade']
        if idade >= 21:
            print(f"{nome} tem {idade} anos")