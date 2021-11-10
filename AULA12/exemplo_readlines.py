arquivo = open('numeros.txt', 'r')

for linha in arquivo.readlines():
    print(linha.strip('\n')) 
arquivo.close()