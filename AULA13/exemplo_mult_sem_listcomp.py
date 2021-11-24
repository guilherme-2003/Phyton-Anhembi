cores = ['preta', 'azul', 'branca']
tamanhos = ['P', 'M', 'G']

produto = []
for tam in tamanhos :
    for cor in cores:
        if tam != 'P' and cor != 'azul':
            produto.append((tam, cor))

print(produto)