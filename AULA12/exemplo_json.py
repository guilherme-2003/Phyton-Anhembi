import json

def salvar_para_json(informacoes: list) -> None:
    with open('nomes.json', 'w') as arquivo:
        json.dump(informacoes, arquivo, indent=4)

def ler_info_pessoas(n_pessoas: int) -> list:
    lista_pessoas = []

    for i in range(n_pessoas):
        nome = input("Digite o nome: ")
        idade = int(input('Digite a idade: '))
        salario = float(input('Digite o salário: '))
    
        dict_pessoas = {'nome': nome, 'idade': idade, 'salario': salario}
        lista_pessoas.append(dict_pessoas)
    return lista_pessoas

lista_pessoas = ler_info_pessoas(3)
salvar_para_json(lista_pessoas)
print("Arquivo salvo com sucesso")