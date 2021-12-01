import datetime
import json

def salva_arquivo_log(lista_logs: str) -> None:
    with open('acessos.json', 'w') as arquivo:
        json.dump(lista_logs, arquivo, indent=4)
    print('Arquivo de log salvo com sucesso.')

def cria_dicionario_data_hora(nome:str) -> dict:
    data_hora = str(datetime.datetime.now())
    data, hora = data_hora.split(' ')
    dict_data_hora = {
        'nome': nome, 'data': data, 'hora': hora}
    return dict_data_hora

lista_logins = []
nome = ' '

while(nome != 'fim'):
    nome = input('Digite seu nome: ')
    login = cria_dicionario_data_hora(nome)
    lista_logins.append(login)

salva_arquivo_log(lista_logins)