cores = ['preta', 'azul', 'branca']
tamanhos = ['P', 'M', 'G']

produto = [(tam, cor) for tam in tamanhos 
                      for cor in cores
                      if tam != 'P' and cor != 'azul']

print(produto)