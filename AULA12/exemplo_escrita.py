arquivo=open('numeros.txt', 'a')

for linha in range(1, 101):
    arquivo.write(f'{linha}\n')

arquivo.close