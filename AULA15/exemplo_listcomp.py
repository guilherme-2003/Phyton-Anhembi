nomes = ['gustavo', 'carlos', 'carla', 
         'ailton', 'josé', 'alfredo']

nomes_formatados = [nome.upper() 
                    for nome in nomes 
                    if nome[0] == 'c']
print(nomes_formatados)