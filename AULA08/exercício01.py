def swap(palavra1: str, palavra2: str):
    tamanho = len(palavra1)
    inicio = random.randint(0, tamanho-2)

    tmp = palavra2[inicio:] 
                                   # parte trocada da palavra
    palavra2 = palavra2[:inicio] + palavra1[inicio:] 
    palavra1[inicio] = palavra1[:inicio] + tmp

    print(palavra1)
    print(palavra2)

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

print(palavra1)
print(palavra2)