import datetime
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

print(lista_logins)