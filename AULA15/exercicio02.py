import re

cpf = input('Digite o CPF: ')
expressao =  r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}'
if re.match(expressao, cpf) is not None:
    print('CPF é válido')
else:
    print('CPF inválido')