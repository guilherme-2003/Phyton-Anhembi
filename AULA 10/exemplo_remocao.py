info_pessoas = {'João': {'idade': 27, 'sexo': 'masculino'},
'Fernando': {'idade': 18, 'sexo': 'feminino'},
'Aline': {'idade': 20, 'sexo': 'feminino'}}

del info_pessoas['João']
print(info_pessoas.pop('Fernando')) # Mostra na tela a idade e sexo do Fernando
print(info_pessoas) # Mostra apenas dados da Aline
